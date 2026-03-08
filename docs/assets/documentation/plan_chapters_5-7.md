# Überarbeitungsplan – Kapitel 5–7

## Vorbemerkung

Dieser Plan baut auf der abgeschlossenen Überarbeitung der Kapitel 1–4 auf und übernimmt alle dort etablierten Konventionen als verbindlichen Standard. Die Kapitel 5.1, 5.2, 5.3/5.4, 6 und 7 werden an diesen Standard angeglichen.

---

## Verbindliche Konventionen (aus der Überarbeitung Kap. 1–4)

### Anrede und Ton

- Durchgehend Du mit Großschreibung im Fließtext und in allen Admonitions
- Praxis-Boxen verwenden Du, nicht Sie (Originalkapitel 4 und 7 verwenden noch Sie)
- Ton: sachlich, ruhig, direkt; keine rhetorische Überhöhung, keine Meta-Kommentare über den Schreibprozess
- Kein werbender Gestus, keine wiederholte Rechtfertigung der eigenen Relevanz

### Anführungszeichen (strikt nach Stylesheet)

- Doppelte typographische Anführungszeichen für Zitate, Titel, Hervorhebungen in Anführungsfunktion: öffnend U+201E, schließend U+201C
- Einfache typographische Anführungszeichen für uneigentlichen Gebrauch, Distanzierung: öffnend U+201A, schließend U+2018
- Bedeutungsangaben nach fremdsprachigen Ausdrücken in einfachen Anführungszeichen ohne Kursivierung der Angabe: *fútbol* 'Fußball'
- Keine geraden Anführungszeichen im Fließtext (nur in YAML, Code, HTML-Attributen, Admonition-Syntax)

### Phonetische und linguistische Notation

- Grapheme in Backticks mit spitzen Klammern: `<b>`, `<v>`, `<h>`
- Phoneme in Backticks mit Schrägstrichen: `/b/`, `/θ/`, `/s/`
- Phonetische Realisierungen in Backticks mit eckigen Klammern: `[ˈkasa]`, `[β]`
- Konsequent durchhalten, auch in Admonitions und expand-Boxen

### Fettdruck

- Kein Fettdruck im Fließtext finaler Versionen
- Fettdruck in Admonitions nur für strukturelle Orientierung innerhalb von Listen (z.B. in regel-Boxen), nicht für Hervorhebungen im Fließtext
- Fettdruck innerhalb von expand-Boxen ebenfalls vermeiden; stattdessen Kursivierung oder Strukturierung durch Absätze
- Fettgedruckte Quasi-Überschriften (z.B. in Kap. 7) durch echte Markdown-Überschriften ersetzen

### Admonitions

Verfügbare Typen (gemäß admonitions.md):

| Typ | Funktion | Typische Form |
|-----|----------|---------------|
| `context` | Kontextrahmen, Begriffsklärung | `!!!` oder `???` |
| `regel` | Regeln, Merksätze, Übungstipps | `!!!` |
| `tip` | Didaktische Hinweise für Lehrkräfte | `!!!` |
| `expand` | Vertiefungen, Exkurse, Hintergründe | `???` |
| `hoermal` | Audiobeispiele (Ziel- vs. Lernendenaussprache) | `???` |
| `oton` | Stimmen aus der Praxis (Zitate) | `!!!` oder `???` |
| `praxis` | Konkrete Unterrichtsvorschläge | `!!!` oder `???` |
| `summary` | Kapitelzusammenfassung | `!!!` |
| `weiterlesen` | Literaturhinweise am Kapitelende | `???` |
| `cite` | Zitierhinweis | `!!!` |

Positionierungsregeln:

- Nie zwei Admonitions desselben oder ähnlichen Typs direkt nacheinander
- Nie mehr als zwei Admonitions zwischen zwei Fließtext-Absätzen
- Jede Admonition muss an ihrem optimalen inhaltlichen Ort stehen, nicht am nächstbesten
- Context-Boxen und expand-Boxen nicht direkt nebeneinander; wenn beides nötig ist, durch Fließtext trennen
- Praxis-Boxen maximal drei bis vier pro Kapitel; Inhalte vertiefen statt wiederholen

### Expand-Boxen: Stil

- Möglichst in Fließtext statt Listen formulieren
- Fettdruck-Überschriften innerhalb von expand-Boxen vermeiden
- Beispiele in den Text integrieren, nicht als isolierte Aufzählungen

### Querverweise

- Querverweise auf andere Kapitel im Fließtext setzen, nicht gesammelt am Ende
- Querverweis direkt an der Stelle, wo ein Beispiel aus einem anderen Kapitel aufgegriffen wird
- Keine `{:target="_blank" rel="noopener noreferrer"}` mehr (wird global über JavaScript geregelt)
- Fehlerlinguistik als Querschnittskapitel: Alle Kapitel sollten mindestens einen Rückverweis auf Kap. 1 enthalten, wo inhaltlich passend

### Strukturelemente

- Jedes Kapitel endet mit: `!!! summary`, `??? weiterlesen` (nicht `??? expand`), Literatur in `<div class="literatur">`, `!!! cite`
- Cite-Box: Format „Hrsg." (nicht „Koord."), Jahreszahl 2026, aktueller Buchtitel und URL
- Impuls-Klasse (`<div class="impuls" markdown>`) für hervorgehobene Definitionen und Kernaussagen, die kein Zitat sind (statt Blockquote)

### Hoermal-Boxen: Neues Format

- Titel ohne „Hör mal:" (Icon übernimmt das)
- Struktur: `audio-comparison` > `audio-pair` für Ziel- vs. Lernendenaussprache
- Struktur: `audio-grid` für mehrere Beispiele desselben Phänomens
- `<p class="audio-label">` statt `<h4>`
- `<span class="example-ipa">` statt `<span class="example">`
- Fehlerhafte Formen mit `&#42;` (Sternchen als HTML-Entity)
- `class="zc-audio-src" data-zc-src=` statt direktem `src=`

---

## Kapitel 5.1 – Variation & Plurizentrik

Änderungsbedarf: gering

### Zu tun

1. Fettdruck im Fließtext prüfen und entfernen: Ländernamen, Schlüsselbegriffe wie *rezeptive Varietätenkompetenz*
2. In *Wer mehr wissen will*: Fettdruck bei Autorennamen entfernen; `??? expand` zu `??? weiterlesen` ändern
3. Kongruenzfehler korrigieren: *seiner* → *ihrer* (Bezug auf *Lernende*)
4. Verweis auf *variation_klassenraum.md* prüfen: Kapitel existiert nicht in den Projektdateien. Entweder erstellen oder Verweis entfernen/umleiten
5. Querverweis auf Fehlerlinguistik ergänzen, wo die Bewertung von Varietätenunterschieden thematisiert wird (Kap. 1 behandelt das jetzt explizit in „Nicht jede Abweichung ist ein Fehler")
6. Anführungszeichen systematisch prüfen (Bedeutungsangaben in einfache typographische Anführungszeichen)
7. Cite-Box aktualisieren: „Hrsg.", 2026, neuer Buchtitel und URL

---

## Kapitel 5.2 – Aussprachevariation

Änderungsbedarf: gering

### Zu tun

1. Hoermal-Boxen an neues Format anpassen (audio-pair/audio-grid, neue CSS-Klassen, kein „Hör mal:" im Titel)
2. Verweis auf *variation_klassenraum.md* prüfen (s.o.)
3. Einzelne Bullet-Listen in didaktischen Empfehlungen in Fließtext umwandeln
4. Gegebenenfalls Straffung der längsten Abschnitte prüfen (486 Zeilen, längstes Kapitel)
5. Querverweis auf Fehlerlinguistik ergänzen, z.B. beim *seseo*: Verweis darauf, dass im Kap. 1 explizit thematisiert wird, dass Varietätenunterschiede keine Fehler sind
6. `??? expand "Wer mehr wissen will"` zu `??? weiterlesen` ändern
7. Anführungszeichen und phonetische Notation prüfen (Backticks konsequent)
8. Cite-Box aktualisieren

---

## Kapitel 5.3 – Variation in der Anrede (neu: eigenständiges Kapitel)

Änderungsbedarf: mittel (Herauslösung und Vervollständigung)

### Status

Der Anrede-Abschnitt aus dem bisherigen Kap. 5.3 wird zu einem eigenständigen Kapitel. Die vorhandenen Abschnitte (Voseo, Vosotros vs. Ustedes, Fazit) sind inhaltlich auf dem Niveau der Referenzkapitel.

### Zu tun

1. Eigene Einleitung schreiben: motivierend, problemorientiert, im Stil der überarbeiteten Kapitel. Möglicher Aufhänger: die Frage, ob ein:e Lernende:r, die *vos* oder *ustedes* verwendet, korrigiert werden sollte
2. Querverweis auf Fehlerlinguistik (Abschnitt „Nicht jede Abweichung ist ein Fehler"), wo *ustedes* bereits als Beispiel steht
3. Summary-Box ergänzen
4. Weiterlesen-Box ergänzen
5. Literaturliste erstellen
6. Cite-Box erstellen
7. Admonitions prüfen: Die vorhandene context-Box zu *vosotros* in Hispanoamerika ist gut platziert
8. Anführungszeichen, phonetische Notation und Fettdruck prüfen

---

## Kapitel 5.4 – Variation in der Grammatik (Rest des bisherigen 5.3)

Änderungsbedarf: hoch (unfertig)

### Status

Das Kapitel ist beta. Die vorhandenen Abschnitte (Tempusvariation *he cantado* vs. *canté*) sind sehr gut. Drei Abschnitte sind als Platzhalter vorhanden: Diminutive, Leísmo, Dequeísmo.

### Zu tun

1. Eigene Einleitung schreiben (die bisherige Einleitung von 5.3 kann als Basis dienen, muss aber an den neuen Zuschnitt angepasst werden)
2. Fehlende Abschnitte verfassen:
   - Diminutive: regionale Variation (*-ito/-ita* vs. *-ico/-ica* vs. *-ingo*), pragmatische Funktionen (Zuneigung, Ironie, Abschwächung). Querverweis auf Kap. 4 (Kreativität), wo Diminutive im Kontext der Derivation bereits behandelt werden
   - Leísmo: Beschreibung des Phänomens, geographische Verteilung, didaktische Implikationen
   - Dequeísmo/Queísmo: Beschreibung, soziale Bewertung, Umgang im Unterricht
3. Querverweis auf Fehlerlinguistik: Tempusvariation *comí* vs. *he comido* wird in Kap. 1 als Beispiel für Varietätenunterschiede behandelt
4. Summary-Box ergänzen
5. Weiterlesen-Box ergänzen
6. Literaturliste erstellen
7. Cite-Box erstellen
8. Anführungszeichen, Notation und Fettdruck prüfen

---

## Kapitel 6 – Sprachwandel

Änderungsbedarf: mittel

### Stärken

- Innovativer Ansatz (diachrone Betrachtung von der Gegenwart aus)
- Q&A-Format macht abstrakte Inhalte zugänglich
- Gute Verknüpfung von Theorie und konkreten Beispielen

### Zu tun

1. Summary-Box ergänzen (fehlt komplett, ist aber obligatorisch)
2. `??? expand "Wer mehr wissen will"` zu `??? weiterlesen` ändern (falls vorhanden; falls nicht, erstellen)
3. Querverweise ergänzen:
   - Auf Fehlerlinguistik: Die context-Box „Die Fehler von heute gehören manchmal zur Norm von morgen" wird in Kap. 1 jetzt explizit als expand-Box aufgegriffen – ein Rückverweis von Kap. 6 auf Kap. 1 wäre symmetrisch und sinnvoll
   - Auf Kap. 4 (Kreativität): Grammatikalisierung und Wortbildungswandel sind inhaltlich eng verbunden; ein Querverweis fehlt
   - Auf Kap. 5 (Variation): Sprachwandel erklärt viele Variationsphänomene; Querverweise auf *seseo*-Entwicklung, Tempusvariation etc. prüfen
4. Tippfehler korrigieren: *ingetraler* → *integraler*; *Sprachegemeinschaften* → *Sprachgemeinschaften*
5. Stil: Einzelne Passagen sind etwas akademischer als die Referenzkapitel. Prüfen, ob zugänglichere Formulierungen möglich sind, ohne den inhaltlichen Anspruch zu senken
6. Der Abschnitt zur Pluralbildung und zum Kasussystem ist sehr dicht – prüfen, ob Teile in eine expand-Box ausgelagert werden können
7. Fettdruck im Fließtext prüfen und entfernen
8. Anführungszeichen systematisch prüfen
9. Cite-Box aktualisieren

---

## Kapitel 7 – Herkunftssprachen

Änderungsbedarf: mittel

### Stärken

- Sehr relevantes Thema, guter Perspektivwechsel
- Interaktive Karte als Ressource hervorragend
- Systematische kontrastive Darstellung

### Zu tun

1. Anrede vereinheitlichen: Durchgehend Du. Alle praxis-Boxen von Sie auf Du umstellen. Die Fettdruck-Pseudo-Überschriften im Empfehlungsteil (*Lehrkräfte sensibilisieren:*, *Schüler:innen sensibilisieren:*, *Mehrsprachigkeit als Ressource:*) durch echte Markdown-Überschriften (###) ersetzen
2. Bibliographie-Format korrigieren: Vorname vor Nachname → Nachname, Vorname (wie in allen anderen Kapiteln)
3. Praxis-Boxen: Typ prüfen (`praxis` ist jetzt im Admonition-Leitfaden, aber Anzahl und Positionierung prüfen)
4. Fettdruck im Fließtext und im Empfehlungsteil systematisch entfernen
5. Querverweise ergänzen:
   - Auf Fehlerlinguistik: Kap. 1 verweist jetzt explizit auf Herkunftssprachen (Transfer, Artikelfehler, gerolltes R als positiver Transfer) – symmetrische Rückverweise einfügen
   - Auf Aussprachevariation: Verweis, dass sich lautliche Variation auch über Herkunftssprachen erschließen lässt
6. Listige Stellen in Fließtext umwandeln: Einzelne Abschnitte sind zu stark als Aufzählung gestaltet, besonders im kontrastiven Teil
7. Expand-Boxen: Fettdruck-Überschriften innerhalb der Boxen prüfen und entfernen; möglichst in Fließtext umgestalten
8. Anführungszeichen systematisch prüfen (Bedeutungsangaben in einfache typographische Anführungszeichen)
9. `??? expand "Wer mehr wissen will"` zu `??? weiterlesen` ändern
10. Cite-Box aktualisieren

---

## Priorisierung

| Priorität | Kapitel | Aufwand |
|---|---|---|
| 1 (hoch) | 5.4 Grammatische Variation (Fertigstellung, fehlende Abschnitte) | hoch |
| 2 (hoch) | 5.3 Variation in der Anrede (Herauslösung, Einleitung, Abschluss) | mittel |
| 3 (mittel) | 7 Herkunftssprachen (Anrede, Format, Fettdruck, Querverweise) | mittel |
| 4 (mittel) | 6 Sprachwandel (Summary, Querverweise, Stil) | gering–mittel |
| 5 (gering) | 5.1 Variation & Plurizentrik (Fettdruck, Querverweise) | gering |
| 6 (gering) | 5.2 Aussprachevariation (Hoermal-Format, Querverweise) | gering |

---

## Arbeitsablauf pro Kapitel

1. Kapitel vollständig lesen und Gesamtbewertung erstellen
2. Abgleich mit den verbindlichen Konventionen (dieser Plan, Abschnitt „Verbindliche Konventionen")
3. Strukturelle Entscheidungen treffen (Abschnitte umstellen, zusammenfassen, ergänzen?)
4. Abschnittsweise durchgehen: erst besprechen, dann formulieren
5. Admonitions prüfen: Typ, Positionierung, Dichte, Abstand zueinander
6. Querverweise setzen: an der inhaltlich passenden Stelle, nicht gesammelt
7. Anführungszeichen, Notation und Fettdruck im gesamten Kapitel prüfen
8. Cite-Box, Weiterlesen-Box und Summary aktualisieren
9. Abschließende Gesamtlektüre
