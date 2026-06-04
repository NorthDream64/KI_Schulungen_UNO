# Quellen-Workflow — KI-Kurse

> Dieses Dokument beschreibt, wie neue Informationen und Quellen bewertet und eingeordnet werden.  
> Es gilt für alle drei Kurse: KI-Beauftragter (KIB), KI-Manager (KIM), Manager für angewandte KI-Transformation (MAT).  
> Letzte Aktualisierung: 2026-06-04

---

## Zwei Register — zwei Funktionen

### 1 · Neue_Quellen_Intake.md (lokal, Schulungsmaterial-Ordner)

**Funktion:** Ideensammlung. Neue Informationen, die didaktisches Potenzial haben, werden hier gesammelt und bewertet — bevor sie in Kursmaterialien eingebaut werden.

**Wann hierhin:**
- Interessante Studien, Artikel, Grafiken oder Use Cases mit Kurspotenzial
- Noch nicht verifizierte Preprints oder Working Papers
- LinkedIn-Posts, Unternehmensberichte, Konferenzbeiträge
- Neue KI-Tools oder Praxisbeispiele
- Diskussionsimpulse (auch mit Qualitätsvorbehalt)

**Qualitätsanspruch:** Niedrig bis mittel — auch Tier-3-Quellen sind erlaubt, müssen aber als solche gekennzeichnet sein. Entscheidend ist der **didaktische Wert**, nicht der akademische Rang.

**Format je Eintrag:**
- Bewertung: ✅ Aufnehmen / ⚠️ Mit Einschränkung / ⛔ Nicht aufnehmen
- Passend zu: Kurs + Tag
- Kurzbeschreibung, Kernargument, Einsatzform
- Qualitätsvorbehalt (falls nötig)
- Quelle + Urheber

---

### 2 · KI_News_Update.html (GitHub, öffentlich)

**Funktion:** Verbindliche Referenz. Dokumentiert den aktuellen, verifizierten Stand der KI-Gesetzgebung, Regulierung und technologischer Entwicklungen, die Kursinhalte direkt betreffen.

**Wann hierhin:**
- Änderungen an Gesetzen oder Normen (EU AI Act, DSGVO, ISO 42001 etc.)
- Neue oder geänderte Fristen mit direkter Kursrelevanz
- Offizielle Publikationen von Behörden (BSI, EDPB, NIST, EU-Kommission)
- Verifizierte Marktdaten aus Tier-1-Quellen (McKinsey, Stanford HAI, Gartner etc.)
- Neue Standards oder Leitlinien (ISO, NIST, BSI)

**Qualitätsanspruch:** Hoch — ausschließlich verifizierte, belegbare Informationen mit Quellenangabe. Keine Meinungen, Prognosen ohne Belege oder nicht peer-reviewte Aussagen als Fakten.

**Tier-1-Quellen (immer erlaubt):**
- Behörden und Regulierungsstellen: eur-lex.europa.eu, bsi.bund.de, edpb.europa.eu, nist.gov
- Offizielle Anbieter-Dokumentation: learn.microsoft.com, cloud.google.com, openai.com/research
- Anerkannte Standards-Organisationen: iso.org, nist.gov
- Peer-reviewte Publikationen und Hochschulinstitute (arXiv, PNAS, Stanford HAI, NBER)

**Nicht erlaubt:** Unternehmens-Blogs, Handelsmedien, Einzelperson-Blogs — es sei denn, als explizit gekennzeichneter Praxishinweis.

---

## Entscheidungslogik: Was kommt wohin?

```
Neue Information empfangen
        │
        ├─ Regulatorische Änderung (Gesetz, Norm, Frist)?
        │         └─ Ja + verifiziert + Tier-1-Quelle  →  KI_News_Update
        │
        ├─ Technologische Tatsache (neues Modell, Standard, offizielle Kennzahl)?
        │         └─ Ja + Primärquelle verfügbar        →  KI_News_Update
        │
        └─ Alles andere (Studie, Use Case, Diskussionsimpuls, Praxisbeispiel)?
                  └─ Didaktisches Potenzial vorhanden   →  Neue_Quellen_Intake
```

**Grenzfälle:**
- McKinsey-Bericht: Neue_Quellen_Intake (Praxisrelevanz) UND KI_News (wenn Kernzahlen als Marktdaten zitiert werden sollen)
- OpenAI Policy-Dokument: Neue_Quellen_Intake (Diskussionsimpuls), NICHT KI_News (keine neutrale Quelle)
- BSI-Veröffentlichung: KI_News (Behörde, Tier 1)
- LinkedIn-Infografik: Neue_Quellen_Intake (wenn didaktisch wertvoll), NIE KI_News

---

## Kursseparation

Inhalte dürfen **nie 1:1** zwischen Kursen übertragen werden. Differenzierung nach Perspektive und Tiefe:

| Kurs | Perspektive | Tiefe |
|------|-------------|-------|
| **KIB** | Compliance, Regulierung, operative Umsetzung | EU AI Act als Kerninhalt; Normen und Fristen detailliert |
| **KIM** | Strategie, Führung, organisationale Transformation | EU AI Act nur als Hintergrundkontext |
| **MAT** | Angewandte Transformation, Projektsteuerung | Praxis und Umsetzung im Vordergrund |

EU AI Act ist **nur im KIB** ein eigenständiger Themenblock. In KIM und MAT erscheint er ausschließlich als Hintergrundreferenz.

---

## Quellenprüfung vor jeder neuen Einheit

Vor dem Erstellen neuer Kursmaterialien immer zuerst:
1. `Neue_Quellen_Intake.md` lesen (neue didaktische Ideen)
2. `Quellen_und_Dokumente_KI-Kurse.md` lesen (geprüftes Quellenregister)
3. `KI_News_Update.html` prüfen (aktueller regulatorischer Stand)

Alle inhaltlichen Aussagen in Kursmaterialien müssen mit einer nachvollziehbaren Quelle belegt sein. URLs nur verwenden, wenn sie als direktes Ergebnis einer vorherigen Recherche vorlagen — keine konstruierten oder erinnerten URLs.

---

*Erstellt: 2026-06-04 · Maintainer: Uli Nord · Dozenten-Assistent: Claude (Anthropic)*
