# -*- coding: utf-8 -*-
"""
Lab Modellvalidierung & Bias — Datensatz-Generator und Kennzahlen-Berechnung
Kurs: KI-Manager:in (KIM)

Was dieses Skript tut (und warum):
1. Es erzeugt einen SYNTHETISCHEN Bewerber-Datensatz. Alle Personen und Zahlen sind erfunden.
2. In die HISTORISCHEN Einstellungsentscheidungen ist bewusst eine Voreingenommenheit
   (Bias) eingebaut: Männer und jüngere Bewerber wurden in der Vergangenheit systematisch
   bevorzugt. Ein Modell, das aus diesen Daten lernt, ÜBERNIMMT diese Diskriminierung.
3. Es berechnet alle Kennzahlen, die das Interaktiv-Tool anzeigt: Konfusionsmatrix,
   Precision/Recall/F1 über verschiedene Schwellenwerte, Fairness je Gruppe,
   Overfitting-Kurve sowie den Proxy-Leakage-Vergleich.

Abhängigkeiten: numpy, pandas, scikit-learn  (pip install scikit-learn)
"""
import numpy as np, pandas as pd, json
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(42)
N = 2000

# --- 1. Merkmale erzeugen ---
geschlecht = rng.integers(0, 2, N)          # 0 = weiblich, 1 = männlich
aelter     = rng.integers(0, 2, N)          # 0 = jünger (<40), 1 = älter (>=40)
fachscore  = np.clip(rng.normal(60, 15, N), 0, 100)      # Fachtest 0-100 (echtes Können)
interview  = np.clip(rng.normal(60, 15, N), 0, 100)      # Interview 0-100 (echtes Können)
erfahrung  = np.clip(rng.normal(8, 4, N) + aelter*4, 0, 35)  # Berufsjahre

# Proxy-Merkmal: Karrierelücke (Monate). Historisch bei Frauen im Schnitt größer.
# Es ist der "Stellvertreter", über den das Geschlecht ins Modell zurückleckt,
# selbst wenn man die Spalte Geschlecht weglässt.
karriere_luecke = np.clip(rng.normal(6, 5, N) + (1-geschlecht)*8, 0, 60)

# --- 2. Echtes Verdienst ("wer wäre wirklich gut?") ---
merit = 0.45*fachscore + 0.45*interview + 0.10*(erfahrung/35*100)
merit_z = (merit - merit.mean())/merit.std()

# --- 3. Historische, VOREINGENOMMENE Einstellungsentscheidung ---
# Echter Verdienst zählt (2.2*merit), ABER: Bonus für Männer (+0.9) und Jüngere (+0.5),
# und eine überzogene Bestrafung der Karrierelücke, die über ihren echten Wert hinausgeht.
logit = (-1.15 + 2.2*merit_z + 0.9*geschlecht + 0.5*(1-aelter) - 0.035*karriere_luecke)
p_hire = 1/(1+np.exp(-logit))
eingestellt = (rng.random(N) < p_hire).astype(int)

df = pd.DataFrame({
    "geschlecht": geschlecht, "aelter": aelter, "fachscore": fachscore.round(1),
    "interview": interview.round(1), "erfahrung_jahre": erfahrung.round(1),
    "karriere_luecke_monate": karriere_luecke.round(1), "eingestellt": eingestellt,
})
df.to_csv("/sessions/trusting-focused-mendel/mnt/Schulungsmaterial/KI-Manager/Lab_Modellvalidierung/bewerber_screening.csv", index=False)

base_rate = eingestellt.mean()

# --- 4. Hauptmodell (mit allen Merkmalen inkl. Geschlecht) ---
feat_all = ["geschlecht","aelter","fachscore","interview","erfahrung_jahre","karriere_luecke_monate"]
X = df[feat_all].values; y = df["eingestellt"].values
Xtr,Xte,ytr,yte,gtr,gte = train_test_split(X,y,df["geschlecht"].values,test_size=0.4,random_state=1,stratify=y)
sc = StandardScaler().fit(Xtr)
clf = LogisticRegression(max_iter=1000).fit(sc.transform(Xtr), ytr)
proba = clf.predict_proba(sc.transform(Xte))[:,1]

def cm(y_true, y_pred):
    tp=int(((y_pred==1)&(y_true==1)).sum()); fp=int(((y_pred==1)&(y_true==0)).sum())
    fn=int(((y_pred==0)&(y_true==1)).sum()); tn=int(((y_pred==0)&(y_true==0)).sum())
    return tp,fp,fn,tn

sweep=[]
for t in np.round(np.arange(0.05,0.96,0.05),2):
    yp=(proba>=t).astype(int); tp,fp,fn,tn=cm(yte,yp)
    prec = tp/(tp+fp) if tp+fp else 0.0
    rec  = tp/(tp+fn) if tp+fn else 0.0
    f1   = 2*prec*rec/(prec+rec) if prec+rec else 0.0
    # Fairness je Geschlecht: Auswahlrate (demographic parity) und Recall (equal opportunity)
    def grp(gv):
        m=(gte==gv); ypg=yp[m]; ytg=yte[m]
        sel=ypg.mean() if len(ypg) else 0.0
        tpr=((ypg==1)&(ytg==1)).sum()/max((ytg==1).sum(),1)
        return round(float(sel),3), round(float(tpr),3)
    w_sel,w_rec=grp(0); m_sel,m_rec=grp(1)
    sweep.append({"t":float(t),"tp":tp,"fp":fp,"fn":fn,"tn":tn,
                  "precision":round(prec,3),"recall":round(rec,3),"f1":round(f1,3),
                  "sel_w":w_sel,"sel_m":m_sel,"rec_w":w_rec,"rec_m":m_rec})

# --- 5. Overfitting-Kurve (Entscheidungsbaum, wachsende Tiefe) ---
overfit={"depth":[],"train":[],"test":[]}
for d in range(1,16):
    t=DecisionTreeClassifier(max_depth=d,random_state=1).fit(Xtr,ytr)
    overfit["depth"].append(d)
    overfit["train"].append(round(t.score(Xtr,ytr),3))
    overfit["test"].append(round(t.score(Xte,yte),3))

# --- 6. Proxy-Leakage: Auswahlraten-Lücke je nach Merkmalssatz (Schwelle 0.5) ---
def parity_gap(features):
    Xs=df[features].values
    Xa,Xb,ya,yb,ga,gb=train_test_split(Xs,y,df["geschlecht"].values,test_size=0.4,random_state=1,stratify=y)
    s=StandardScaler().fit(Xa); c=LogisticRegression(max_iter=1000).fit(s.transform(Xa),ya)
    pr=c.predict_proba(s.transform(Xb))[:,1]; yp=(pr>=0.5).astype(int)
    sel_m=yp[gb==1].mean(); sel_w=yp[gb==0].mean()
    return round(float(sel_m-sel_w),3), round(float(sel_m),3), round(float(sel_w),3)

proxy={}
proxy["mit_geschlecht"]      = parity_gap(feat_all)
proxy["ohne_geschlecht"]     = parity_gap([f for f in feat_all if f!="geschlecht"])
proxy["ohne_gpluslucke"]     = parity_gap([f for f in feat_all if f not in ("geschlecht","karriere_luecke_monate")])

out={"base_rate":round(float(base_rate),3),"n_test":int(len(yte)),
     "sweep":sweep,"overfit":overfit,"proxy":proxy}
with open("/sessions/trusting-focused-mendel/mnt/Schulungsmaterial/KI-Manager/Lab_Modellvalidierung/kennzahlen.json","w") as f:
    json.dump(out,f,indent=1)

# --- Sanity-Ausgabe ---
print("Base rate (Einstellungsquote):", round(base_rate,3), "| Test-N:", len(yte))
print("\nSchwelle 0.50:")
row=[s for s in sweep if s['t']==0.5][0]
print("  P/R/F1:",row['precision'],row['recall'],row['f1'],"| Konfusion tp,fp,fn,tn:",row['tp'],row['fp'],row['fn'],row['tn'])
print("  Auswahlrate m/w:",row['sel_m'],row['sel_w'],"| Recall m/w:",row['rec_m'],row['rec_w'])
print("\nOverfitting test-acc je Tiefe:",overfit['test'])
print("\nProxy-Leakage (Auswahlraten-Lücke m-w):")
for k,v in proxy.items(): print("  ",k,"-> gap",v[0],"(m",v[1],", w",v[2],")")
