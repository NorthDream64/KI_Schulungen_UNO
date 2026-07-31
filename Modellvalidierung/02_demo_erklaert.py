# -*- coding: utf-8 -*-
"""
Lab Modellvalidierung & Bias — didaktisches Demo-Skript (für Dozentenvorführung)
Kurs: KI-Manager:in (KIM)

Dieses Skript ist zum LIVE-VORFÜHREN gedacht: Es lädt den Datensatz, trainiert ein
einfaches Modell und ERKLÄRT in einfacher Sprache, was Precision, Recall, F1/F2,
Bias und Overfitting bedeuten. Keine Vorkenntnisse nötig — einfach ausführen:

    python3 02_demo_erklaert.py

Abhängigkeiten: pandas, scikit-learn  (matplotlib optional für Diagramme)
"""
import pandas as pd, numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("bewerber_screening.csv")
print("="*70)
print(f"Datensatz: {len(df)} Bewerber:innen · Einstellungsquote historisch: {df['eingestellt'].mean():.0%}")
print("Achtung: Die historischen Entscheidungen sind bewusst voreingenommen.")
print("="*70)

feat = ["geschlecht","alter_monate","fachscore","interview","erfahrung_jahre","karriere_luecke_monate"]
X, y = df[feat].values, df["eingestellt"].values
Xtr,Xte,ytr,yte,gtr,gte = train_test_split(X,y,df["geschlecht"].values,test_size=0.4,random_state=1,stratify=y)
sc = StandardScaler().fit(Xtr)
clf = LogisticRegression(max_iter=1000).fit(sc.transform(Xtr), ytr)
proba = clf.predict_proba(sc.transform(Xte))[:,1]

def konfusion(t):
    yp=(proba>=t).astype(int)
    tp=int(((yp==1)&(yte==1)).sum()); fp=int(((yp==1)&(yte==0)).sum())
    fn=int(((yp==0)&(yte==1)).sum()); tn=int(((yp==0)&(yte==0)).sum())
    return tp,fp,fn,tn,yp

def fbeta(p,r,b): d=b*b*p+r; return (1+b*b)*p*r/d if d else 0

print("\n--- 1) KONFUSIONSMATRIX & KENNZAHLEN (Schwelle 0.50) ---")
tp,fp,fn,tn,yp = konfusion(0.50)
prec, rec = tp/(tp+fp), tp/(tp+fn)
print(f"  Richtig empfohlen (TP): {tp:4d}   |  Übersehen  (FN): {fn:4d}")
print(f"  Fehlalarm       (FP): {fp:4d}   |  Richtig abgelehnt (TN): {tn:4d}")
print(f"\n  Precision = {prec:.0%}  → Von den Empfohlenen sind {prec:.0%} wirklich geeignet.")
print(f"  Recall    = {rec:.0%}  → Von allen Geeigneten findet das Modell {rec:.0%}.")
print(f"  F1        = {fbeta(prec,rec,1):.0%}  (Balance)   F2 = {fbeta(prec,rec,2):.0%}  (Recall zählt doppelt)")
print("  Merke: strenger (höhere Schwelle) → Precision steigt, Recall sinkt. Es ist eine Abwägung.")

print("\n--- 2) BIAS: dasselbe Modell, zwei Gruppen (Schwelle 0.50) ---")
for gv,name in [(1,'Männer  '),(0,'Frauen  ')]:
    m=(gte==gv); sel=yp[m].mean(); tpr=((yp[m]==1)&(yte[m]==1)).sum()/max((yte[m]==1).sum(),1)
    print(f"  {name}: Auswahlrate {sel:.0%}  ·  Recall {tpr:.0%}")
print("  → Männer werden häufiger empfohlen UND häufiger korrekt gefunden.")
print("    Das Modell hat die historische Bevorzugung gelernt. Fairness ist messbar.")

print("\n--- 3) PROXY-FALLE: reicht es, 'Geschlecht' wegzulassen? ---")
def gap(features):
    Xs=df[features].values
    Xa,Xb,ya,yb,ga,gb=train_test_split(Xs,y,df["geschlecht"].values,test_size=0.4,random_state=1,stratify=y)
    s=StandardScaler().fit(Xa); c=LogisticRegression(max_iter=1000).fit(s.transform(Xa),ya)
    yp=(c.predict_proba(s.transform(Xb))[:,1]>=0.5).astype(int)
    return yp[gb==1].mean()-yp[gb==0].mean()
print(f"  mit 'Geschlecht'                     : Lücke {gap(feat)*100:+.0f} Pp.")
print(f"  ohne 'Geschlecht'                    : Lücke {gap([f for f in feat if f!='geschlecht'])*100:+.0f} Pp. (immer noch da!)")
print(f"  ohne 'Geschlecht' + 'Karrierelücke'  : Lücke {gap([f for f in feat if f not in ('geschlecht','karriere_luecke_monate')])*100:+.0f} Pp.")
print("  → Weglassen allein hilft kaum: die Karrierelücke verrät das Geschlecht (Proxy).")

print("\n--- 4) OVERFITTING: auswendig lernen statt verstehen ---")
print("  Tiefe | Training | neue Daten | Diagnose")
for d in [1,2,4,6,8,12]:
    t=DecisionTreeClassifier(max_depth=d,random_state=1).fit(Xtr,ytr)
    tr,te=t.score(Xtr,ytr),t.score(Xte,yte)
    diag = "Underfitting" if d<=2 else ("gut" if tr-te<=0.06 else "OVERFITTING")
    print(f"   {d:4d} |  {tr:5.0%}   |   {te:5.0%}    | {diag}")
print("  → Wenn Training immer besser, neue Daten aber schlechter werden: Overfitting.")

# Optionale Diagramme
try:
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    ds=list(range(1,16)); trs=[]; tes=[]
    for d in ds:
        t=DecisionTreeClassifier(max_depth=d,random_state=1).fit(Xtr,ytr)
        trs.append(t.score(Xtr,ytr)); tes.append(t.score(Xte,yte))
    plt.figure(figsize=(6,3.5)); plt.plot(ds,trs,'-o',label='Trainingsdaten'); plt.plot(ds,tes,'-o',label='neue Daten')
    plt.xlabel('Komplexität (Baumtiefe)'); plt.ylabel('Trefferquote'); plt.legend(); plt.tight_layout()
    plt.savefig('overfitting_kurve.png',dpi=120)
    print("\n  Diagramm gespeichert: overfitting_kurve.png")
except Exception as e:
    print(f"\n  (matplotlib nicht verfügbar — Diagramm übersprungen: {e})")
