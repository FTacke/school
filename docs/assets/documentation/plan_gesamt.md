# Plan Gesamtüberarbeitung – Linguistik im Spanischunterricht

## I. Systematische Uneinheitlichkeiten (kapitelübergreifend)

### 1. Anrede und Ton

Die Anrede der Leser:innen war nicht durchgängig einheitlich. Kapitel 1-4 sind diesbezüglich die Referenz und verwenden unpersönliche Formen und gelegentlich "Du" (großgeschrieben), in keinem Fall "Sie". Das muss für die letzten Kapitel noch geprüft und ggf. angepasst werden.

Lies dazu plan_chapters_5-7.md (jüngerer überarbeiteter Plan)

### 2. Admonition-Typen: Konsistenz und Funktionalität

Lies dazu plan_chapters_5-7.md (jüngerer überarbeiteter Plan)

### 3. Anführungszeichen

#### 1. Doppelte Anführungszeichen (Primärzitate)

**Verwendung:**
- Direkte Zitate
- Titel von Beiträgen im Fließtext
- Hervorhebungen in Anführungsfunktion

**Form:**

„Work in Progress & Peer Review“

**Unicode:**
- Öffnend: „  
  - U+201E  
  - HTML: `&bdquo;`
- Schließend: “  
  - U+201C  
  - HTML: `&ldquo;`

⚠ Nicht verwenden: `"` (gerade Anführungszeichen) im Fließtext.

---

#### 2. Einfache Anführungszeichen (Sekundär / uneigentlich)

**Verwendung:**
- Uneigentlicher Gebrauch
- Distanzierung
- Begriffsmarkierung innerhalb von Zitaten

**Form:**

‚für uneigentlichen Gebrauch im Text‘

**Unicode:**
- Öffnend: ‚  
  - U+201A  
  - HTML: `&sbquo;`
- Schließend: ‘  
  - U+2018  
  - HTML: `&lsquo;`

---

#### 3. Bedeutungsangaben nach fremdsprachigen Ausdrücken

**Verwendung:**
- Bedeutungsübersetzungen
- Glossierungen im Fließtext

**Form:**

*fútbol* ‘Fußball’

Regel:
- Fremdsprachiger Ausdruck kursiv
- Bedeutungsangabe in einfachen Anführungszeichen
- Keine doppelten Anführungszeichen

---

#### 4. Anführungszeichen in Admonitions

Hier für die Titelangaben immer rein gerade Anführungszeichen keine typographischen. Korrekt ist also nur:

??? expand "Titelangabe"


### 4. Fettdruck im Fließtext

Der MkDocs-Leitfaden schließt Fettdruck in finalen Textversionen aus, außer bei systematischen Kategorienmarkierungen. Mehrere Kapitel verwenden dennoch Fettdruck im Fließtext.

- Kap. 1 Fehlerlinguistik: *Lernendensprache*, *Kriterium der Korrektheit*, *Kriterium der Angemessenheit*, *Varietätenabweichungen* – teils funktional, teils dekorativ
- Kap. 4 Kreativität: sechs fettgedruckte Wortbildungsprozess-Bezeichnungen in der Auflistung; zahlreiche Fettdrucke in Expand-Boxen (*Rekursive Derivation*, *Parasynthese* etc.)
- Kap. 5.1 Plurizentrik: *Mexiko*, *Argentinien*, *Kolumbien*, *rezeptive Varietätenkompetenz* – teilweise funktional
- Kap. 7 Herkunftssprachen: *Lehrkräfte sensibilisieren:*, *Schüler:innen sensibilisieren:*, *Mehrsprachigkeit als Ressource:*, *Didaktische Konsequenz:* – als Quasi-Überschriften verwendet, verstößt gegen Barrierefreiheitsregel

Empfehlung: Fettdruck systematisch reduzieren. In Kap. 7 die fettgedruckten Quasi-Überschriften durch echte Markdown-Überschriften (###) ersetzen. In Kap. 4 die nummerierte Liste der Wortbildungsprozesse ohne Fettdruck gestalten.

### 5. Kursivierung fremdsprachiger Beispiele

Überwiegend korrekt, aber mit Lücken: In Kap. 1 sind einige spanische Beispiele nicht kursiviert (v.a. in Tabellen). In Kap. 7 fehlt gelegentlich die Kursivierung bei Einzelwörtern.

### 6. Querverweise zwischen Kapiteln

Die Querverweise sind unterschiedlich dicht.

- Gut verlinkt: Aussprache → Orthographie, Aussprache → Aussprachevariation, Aussprache → Herkunftssprachen, Fehlerlinguistik → Variation
- Schwach verlinkt: Fehlerlinguistik → Aussprache/Orthographie (keine konkreten Beispiele aus diesen Kapiteln), Kreativität → Sprachwandel (naheliegend, fehlt), Sprachwandel → Kreativität (fehlt), Sprachwandel → Fehlerlinguistik (fehlt)
- Fehlend: Kap. 4 verweist nicht auf Kap. 6, obwohl Wortbildungswandel ein natürlicher Brückenpunkt wäre. Kap. 6 verweist nicht zurück auf Kap. 4.

Empfehlung: Siehe Abschnitt II und kapitelspezifische Empfehlungen.

### 7. Abkürzungen

Der MkDocs-Leitfaden schreibt Abkürzungen ohne Leerzeichen vor (z.B., d.h., u.a.). Dies wird überwiegend eingehalten, sollte aber in einem Durchlauf systematisch geprüft werden.

### 8. Bibliographie-Format

Das Format ist weitgehend konsistent. Zwei Abweichungen:

- Kap. 7 Herkunftssprachen: Bibliographie-Einträge mit Vorname vor Nachname (*Bernd Brehmer*, *Christiane Fäcke*) statt Nachname, Vorname – weicht vom Format aller anderen Kapitel ab.


### 9. Einleitungsstil (motivierende Kapitelanfänge)

Die motivierenden Einleitungen variieren in Qualität und Stil.

Lies dazu plan_chapters_5-7.md (jüngerer überarbeiteter Plan)


### 10. Fehlende Strukturelemente

- Kap. 5.3 (Grammatik-Variation): Noch im Beta-Zustand. Fehlende Abschnitte: Diminutive, Leísmo, Dequeísmo. Keine Zusammenfassungsbox, kein *Wer mehr wissen will*, keine Literaturliste.
- Kap. 6 Sprachwandel: Keine Zusammenfassungsbox (`summary`).

---

## II. Kohärenzstärkung: Fehlerlinguistik als roter Faden

### a) Inhalte aus Kap. 2–7 als Beispiele in Fehlerlinguistik einbinden

Das Kapitel Fehlerlinguistik beansprucht, das *zentrale Werkzeug* des Toolkits zu sein und *alle folgenden Kapitel zu begleiten*. Dieser Anspruch wird bisher nicht hinreichend durch konkrete Bezüge zu den Folgekapiteln eingelöst. Folgende Beispiele aus Kap. 2–7 könnten in Kap. 1 exemplarisch herangezogen werden:

- Aus Kap. 5.1/5.2 (Variation): Das *ustedes*-Beispiel (bereits vorhanden) könnte um die *seseo*-Frage ergänzt werden: Ist es ein Fehler, wenn eine Schülerin konsequent den *seseo* verwendet?
- Aus Kap. 7 (Herkunftssprachen): Transfer aus der Erstsprache als systematische Fehlerquelle – z.B. türkischsprachige Lernende und Artikelfehler, arabischsprachige Lernende und Vokale

### b) Kapitel 2–7: explizitere Rückverweise auf Fehlerlinguistik

Die folgenden Kapitel sollten an geeigneten Stellen auf Kap. 1 verweisen:

- Kap. 5.1 (Plurizentrik): Verweis auf Fehlerlinguistik bei Bewertung und Korrektur ist vorhanden – gut.
- Kap. 6 (Sprachwandel): Die Passage *Die Fehler von heute gehören manchmal zur Norm von morgen* bietet einen idealen Anknüpfungspunkt, der aber bisher nicht explizit auf Kap. 1 zurückverweist.
- Kap. 7 (Herkunftssprachen): Verweis auf Fehlerlinguistik ist vorhanden – gut.

---

## III. Kapitelspezifische Überarbeitungsbedarfe

### Kap. 1-4

Bereits überarbeitet. Lies die fertig überarbeiteten md-Files in den Projektdateien, damit du den Inhalt und Stil kennst.

---

Lies zu den folngenden Kapitel plan_chapters_5-7.md (jüngerer überarbeiteter Plan)

### Kap. 5.1 Variation & Plurizentrik (Änderungsbedarf: gering)

Bewertungsstufe: geringfügig

#### Stärken
- Stilistisch auf dem Zielniveau des Lehrbuchs
- Exzellente Integration der O-Ton-Admonition
- Konsequente didaktische Rahmung
- Gute Querverweise

#### Überarbeitungsbedarf

1. Fettdruck: Ländernamen (*Mexiko*, *Argentinien*, *Kolumbien*) und einzelne Schlüsselwörter (*rezeptive Varietätenkompetenz*) sind fett gesetzt – sollte im Hinblick auf die Fettdruck-Regel geprüft werden.
2. In *Wer mehr wissen will*: Autorennamen sind fett gedruckt (**Tacke (2011)**, **Reimann 2010 ff.**). Das widerspricht dem MkDocs-Leitfaden. In allen anderen Kapiteln sind Literaturverweise im Fließtext nicht fett gesetzt.
3. Kongruenzfehler: *Lernende, die eine amerikanische Form regelmäßig nutzen, sollten nicht korrigiert, sondern in **seiner** bewussten Formwahl bestärkt werden* → *ihrer*.
4. Verweis auf *Variation im Klassenraum* (variation_klassenraum.md): Dieses Kapitel existiert noch nicht in den Projektdateien, wird aber mehrfach verlinkt. Muss vor Publikation entweder erstellt oder die Verweise entfernt werden.

---

### Kap. 5.2 Aussprachevariation (Änderungsbedarf: gering)

Bewertungsstufe: geringfügig

#### Stärken
- Hervorragende Audiobeispiele aus dem CO.RA.PAN-Korpus
- Konsequente plurizentrische Perspektive
- Didaktisch vorbildlich strukturiert

#### Überarbeitungsbedarf

1. Das Kapitel ist mit 486 Zeilen das längste. Einzelne Abschnitte könnten gestrafft werden.
2. Verweis auf *variation_klassenraum.md*: Kapitel existiert nicht (s.o.).
3. Geringfügig: Einige Bullet-Listen in der didaktischen Empfehlung am Ende könnten in Fließtext umgewandelt werden.

---

### Kap. 5.3 Variation in Grammatik und Pragmatik (Änderungsbedarf: hoch – unfertig)

Bewertungsstufe: kritisch (beta)

#### Status

Das Kapitel ist als *beta* gekennzeichnet und noch unvollständig. Die vorhandenen Abschnitte (Tempusvariation, Anrede) sind inhaltlich auf dem Niveau der anderen Variationskapitel.

#### Fehlende Elemente

1. Drei Abschnitte sind als Platzhalter vorhanden, aber leer: Diminutive, Leísmo, Dequeísmo
2. Keine Zusammenfassungsbox
3. Kein *Wer mehr wissen will*
4. Keine Literaturliste
5. Kein `summary` vorhanden

#### Vorhandene Qualität

Die Abschnitte zu Tempusvariation und Anrede sind sehr gut geschrieben, differenziert und auf dem Niveau der Referenzkapitel. Die interaktive Karte zur Tempusvariation ist ein sehr gutes Element. Der Anrede-Abschnitt ist umfassend und vermeidet die typischen Vereinfachungen.

#### Entscheidung: Teilen

Die geplante Teilung in *5.3 Variation in der Anrede* und *5.4 Variation in der Grammatik* ist sinnvoll, da der Anrede-Abschnitt inhaltlich eigenständig und umfangreich genug ist.

---

### Kap. 6 Sprachwandel (Änderungsbedarf: mittel)

Bewertungsstufe: moderat

#### Stärken
- Innovativer Ansatz (Diachrone Betrachtung von der Gegenwart aus)
- Q&A-Format macht abstrakte Inhalte zugänglich
- Gute Verknüpfung von Sprachwandel-Theorie und konkreten Beispielen

#### Überarbeitungsbedarf

1. Fehlende Zusammenfassungsbox: Kap. 6 hat keine `summary`-Admonition. Das ist obligatorisch laut Kapitelarchitektur.
2. Fehlende Querverweise: Kein Verweis auf Kap. 1 (Fehlerlinguistik), obwohl die *Fehler von heute*-Box ein natürlicher Anknüpfungspunkt wäre. Kein Verweis auf Kap. 4 (Kreativität), obwohl Grammatikalisierung und Wortbildungswandel inhaltlich eng verbunden sind.
3. Tippfehler: *ingetraler* (Z. 43) → *integraler*; *Sprachegemeinschaften* (Z. 55) → *Sprachgemeinschaften*
4. Stil: Etwas akademischer als die Referenzkapitel. Einzelne Passagen könnten zugänglicher formuliert werden.
5. Expand-Box *Sprachwandel – linguistisch betrachtet*: Gut, aber einzelne Stellen etwas dicht. Könnte um ein bis zwei konkrete spanische Beispiele ergänzt werden.
6. Der Abschnitt zur Pluralbildung und zum Kasussystem ist inhaltlich sehr dicht und anspruchsvoll – für die Zielgruppe (Lehrkräfte) möglicherweise etwas zu detailliert. Könnte ggf. in eine Expand-Box ausgelagert werden.

---

### Kap. 7 Herkunftssprachen (Änderungsbedarf: mittel)

Bewertungsstufe: moderat

#### Stärken
- Sehr relevantes Thema, guter Perspektivwechsel
- Interaktive Karte als Ressource hervorragend
- Systematische kontrastive Darstellung