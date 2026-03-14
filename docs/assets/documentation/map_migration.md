# Migration des bestehenden Map-Systems zu einer Zensical-konformen Leaflet-Integration

## Ziel der Aufgabe

Das bestehende Map-System des Projekts soll **architektonisch bereinigt und vollständig in das Zensical-Designsystem integriert werden**, ohne die funktionalen Eigenschaften der aktuellen Karten zu verlieren.

Insbesondere müssen weiterhin:

- mehrere unterschiedliche Karten existieren können
- jede Karte ihre **eigenen JSON-Datenquellen** nutzen
- Marker, Popups und Tooltips aus diesen JSON-Daten generiert werden
- Karten unabhängig voneinander initialisiert werden
- Karten einen stabilen **Fullscreen-Modus** besitzen
- Karten visuell konsistent mit dem **Zensical UI-System** sein

Die bestehende Implementierung funktioniert funktional, ist aber strukturell inkonsistent (globale IDs, inkonsistente Fullscreen-Logik, Hardcoded-Farben, Leaflet-Z-Index-Hacks, getrennte UI-Implementationen).

Ziel ist eine **robuste, modulare und wartbare Architektur**.

---

# Grundprinzipien der neuen Map-Architektur

Die neue Integration basiert auf folgenden Regeln.

## 1. Karten sind eigenständige Komponenten

Jede Karte ist eine eigenständige Komponente mit:

- eigenem Container
- eigener Initialisierung
- eigener Datenquelle
- eigener Marker-Logik

Es darf **keine globale Map-ID mehr geben**.

Stattdessen:

```

.book-map
.book-map__canvas

````

Beispiel:

```html
<div class="book-map" data-map="variation">
  <div class="book-map__canvas"></div>
  <button class="book-map__control book-map__control--fullscreen" aria-label="Karte im Vollbild öffnen"></button>
</div>
````

---

# Wichtige funktionale Anforderungen

Diese Funktionalitäten müssen **unverändert erhalten bleiben**.

## Mehrere Karten

Mehrere Karten können gleichzeitig existieren.

Beispiele:

* Herkunftssprachenkarte
* Variation-Karte
* Variation-Tempora-Karte
* Länderkarte

Jede Karte:

* nutzt eine eigene JSON-Datei
* besitzt eigene Marker
* besitzt eigene Popup-Struktur

Beispiele für JSON-Dateien:

```
data/languages.json
data/variation.json
data/tempora.json
data/countries.json
```

Die Migration darf **keine Annahmen über Datenstruktur zerstören**.

---

# Architektur der neuen Implementierung

Die neue Struktur besteht aus vier Ebenen.

```
MAP SYSTEM
│
├─ CSS Integration
│
├─ Map UI Controller
│
├─ Map Loader
│
└─ Individual Map Modules
```

---

# 1 CSS Integration

Alle Karten verwenden eine gemeinsame Zensical-Komponente.

### CSS-Komponente

```
.book-map
.book-map__canvas
.book-map__control
```

### Eigenschaften

* Token-basierte Farben
* kein Hardcoding von Farben
* kompatibel mit Light/Dark Mode
* kein globaler z-index Hack
* Fullscreen respektiert Header

### Designquellen

Alle Farben und Typografie kommen aus:

```
00_tokens.css
10_typography.css
```

Beispiele:

```
--book-bg
--book-surface-1
--book-border
--book-fg
--book-muted
--book-accent
--book-shadow
```

Es dürfen **keine festen Farben mehr verwendet werden** wie:

```
#1976d2
#666
#aaa
#eee
```

---

# 2 Map Container Regeln

Alle Karten folgen der gleichen Struktur.

```
.book-map
  ├─ .book-map__canvas
  └─ .book-map__control--fullscreen
```

### Standardhöhe

```
default: 22rem
variation: 40rem
variation_tempora: 31rem
```

Dies wird über `data-map` gesteuert.

---

# 3 Fullscreen System

Der Fullscreen-Modus muss stabil funktionieren.

### Anforderungen

* Karte darf **nie über die Top-App-Bar gehen**
* Headerhöhe wird dynamisch berechnet
* Escape beendet Fullscreen
* Resize passt Karte neu an
* Scroll wird gesperrt

### CSS

Fullscreen nutzt:

```
position: fixed
top: var(--map-header-offset)
height: calc(100dvh - var(--map-header-offset))
```

### JS

Die Headerhöhe wird dynamisch ermittelt:

```
document.querySelector(".md-header")
```

und als CSS Variable gesetzt:

```
--map-header-offset
```

---

# 4 Map UI Controller

Ein gemeinsamer Controller verwaltet:

* Fullscreen
* Headerhöhe
* Resize
* Escape
* Button State

Datei:

```
map_ui.js
```

Der Controller exportiert eine Funktion:

```
MapUI.enableFullscreenUI(container, map, button)
```

Dieser Controller:

* setzt Button Icons
* setzt aria-labels
* invalidiert die Leaflet-Karte nach Resize

---

# 5 Map Initialisierung

Jede Karte initialisiert sich selbst.

Beispiel:

```
map_variation.js
map_tempora.js
map_languages.js
map_countries.js
```

Grundprinzip:

```
document.querySelectorAll(".book-map")
```

Dann anhand von `data-map` entscheiden.

Beispiel:

```
data-map="variation"
```

---

# 6 Datenquellen

Die bestehenden JSON-Dateien müssen unverändert nutzbar bleiben.

Beispielstruktur:

```
{
  "name": "Mexiko",
  "lat": 19.4326,
  "lng": -99.1332,
  "familie": "Romanisch",
  "hauptstadt": "Mexiko-Stadt"
}
```

Marker werden weiterhin so erzeugt:

```
L.marker([lat, lng])
```

Popup-Inhalte werden aus JSON generiert.

---

# 7 Popup-System

Popups bleiben semantisch gleich, werden aber visuell angepasst.

Popup-Struktur:

```
.popup-sprachenkarte
.popup-title
.popup-familie
.popup-hauptstadt
.popup-line
.popup-label
.popup-value
```

Die Klassen bleiben bestehen, damit JSON-Rendering weiterhin funktioniert.

---

# 8 Tooltip-System

Tooltips bleiben Leaflet Tooltips.

Styling wird vereinheitlicht:

```
.leaflet-tooltip
```

Eigenschaften:

* book font
* kleine UI Schrift
* dezente Hintergrundfläche
* Token-basierte Farben

---

# 9 Leaflet Z-Index

Globale Leaflet-Pane Hacks werden entfernt.

Stattdessen:

```
.book-map .leaflet-control-container
```

---

# 10 Migration der bestehenden Dateien

Die folgenden Dateien müssen migriert werden:

```
map.js
map_countries.js
map_variation_tempora.js
map_ui.js
```

Wichtige Änderungen:

### Entfernen

```
#map-container
#mapid
#fullscreen-btn
window.toggleFullscreen
```

### Ersetzen durch

```
.book-map
.book-map__canvas
.book-map__control
MapUI.enableFullscreenUI()
```

---

# 11 HTML Anpassung

Alle bisherigen Kartencontainer werden ersetzt.

Alt:

```
<div id="map-container">
  <div id="mapid"></div>
  <button id="fullscreen-btn"></button>
</div>
```

Neu:

```
<div class="book-map" data-map="variation">
  <div class="book-map__canvas"></div>
  <button class="book-map__control book-map__control--fullscreen"></button>
</div>
```

---

# 12 Kompatibilitätsanforderungen

Die Migration darf NICHT:

* bestehende JSON-Strukturen ändern
* Popup-Inhalte verändern
* Marker-Datenlogik verändern
* Datenquellen ändern

Die Migration darf nur:

* Containerstruktur modernisieren
* UI vereinheitlichen
* Fullscreen stabilisieren
* CSS tokenisieren

---

# 13 Zielzustand

Nach der Migration besitzt das System:

* ein **einheitliches Karten-Design**
* tokenbasierte Farben
* stabile Fullscreen-Funktion
* saubere Leaflet Integration
* modulare Kartenarchitektur
* JSON-basierte Datenquellen

Die Karten verhalten sich wie **native Zensical-Komponenten**.

---

# Ergebnis

Das Map-System wird:

* stabiler
* wartbarer
* designkonsistent
* skalierbar für weitere Karten



## Addendum: Verbindliche Spezifikationen für die sofort umsetzbare Migration

Dieses Addendum konkretisiert die Migration so, dass sie ohne Interpretationsspielraum umgesetzt werden kann.

---

# A. Verbindliche Migrationsziele

Die Migration ist erst dann korrekt abgeschlossen, wenn alle folgenden Ziele erfüllt sind:

1. Alle Karten verwenden eine **einheitliche Container-Architektur**.
2. Keine Karte verwendet mehr globale IDs wie:
   - `#map-container`
   - `#mapid`
   - `#fullscreen-btn`
3. Es existieren **keine globalen Fullscreen-Toggle-Funktionen** mehr wie:
   - `window.toggleFullscreen`
   - `window.toggleFullscreenVariation`
   - `window.toggleFullscreenTempora`
4. Jede Karte bleibt funktional eigenständig und kann weiterhin:
   - ihre eigene JSON-Datei laden
   - ihre eigenen Marker erzeugen
   - ihre eigenen Tooltip-/Popup-Inhalte rendern
5. Der Fullscreen-Modus bleibt immer **unterhalb der Top-App-Bar**.
6. Das Styling der Karten ist vollständig an das Zensical-System angebunden:
   - Farben nur über Tokens
   - Typografie nur über Buch-Variablen
   - Controls, Popups und Tooltips im gleichen visuellen System wie der Rest des Buches
7. Die Migration darf die bestehenden Datenmodelle **nicht brechen**.

---

# B. Verbindliche Architektur

## B1. Gemeinsame Struktur

Jede Karte basiert auf genau diesem HTML-Prinzip:

```html
<div class="book-map" data-map="variation">
  <div class="book-map__canvas"></div>
  <button
    type="button"
    class="book-map__control book-map__control--fullscreen"
    aria-label="Karte im Vollbild öffnen"
    aria-pressed="false">
    <span class="material-icons" aria-hidden="true">fullscreen</span>
  </button>
</div>
````

### Regeln

* `.book-map` ist der äußere Kartencontainer.
* `.book-map__canvas` ist das Leaflet-Ziel.
* `.book-map__control--fullscreen` ist der Fullscreen-Button.
* Die konkrete Kartenart wird ausschließlich über `data-map` identifiziert.
* Es darf keine global eindeutige Map-ID vorausgesetzt werden.

---

# C. Datenquellen und JSON-Kompatibilität

## C1. Harte Anforderung

Die bestehenden Karten beziehen Informationen aus unterschiedlichen JSON-Dateien. Das muss vollständig erhalten bleiben.

Das heißt:

* jede Karte darf weiterhin ihre eigene Datei laden
* jede Karte darf weiterhin ihre eigene Datenstruktur haben
* die Migration darf keine Vereinheitlichung der JSON-Dateien erzwingen

## C2. Verpflichtende Lösung: Adapter-Prinzip

Jede Karte bekommt eine **eigene Datenadapter-Schicht**, damit unterschiedliche JSON-Strukturen sauber verarbeitet werden können.

Prinzip:

```js
function normalizeVariationItem(raw) { ... }
function normalizeCountryItem(raw) { ... }
function normalizeTemporaItem(raw) { ... }
```

Ziel der Adapter ist nicht, die Quelldatei zu verändern, sondern intern ein stabiles Objekt zu erzeugen, z. B.:

```js
{
  lat: ...,
  lng: ...,
  title: ...,
  tooltip: ...,
  popupHtml: ...,
  markerOptions: ...
}
```

## C3. Verboten

* JSON-Dateien umstrukturieren, nur damit die UI einfacher wird
* Popup-Informationen aus den Quelldaten entfernen
* bestehende fachliche Inhalte verkürzen oder ersetzen

---

# D. Verbindliche JS-Architektur

## D1. map_ui.js ist die einzige gemeinsame UI-Schicht

`map_ui.js` übernimmt ausschließlich UI-nahe Infrastruktur:

* Fullscreen
* Header-Offset
* Resize-Verhalten
* Escape-Handling
* Scroll-Lock
* Button-State
* `invalidateSize()` nach Layoutwechsel

Diese Datei darf **keine karteninhaltliche Logik** enthalten.

## D2. Einzelne Kartenmodule bleiben fachlich getrennt

Jedes Kartenmodul bleibt für seine eigene Fachlogik zuständig:

* Daten laden
* Daten normalisieren
* Marker erzeugen
* Layer definieren
* Popup-/Tooltip-Inhalte erzeugen

Beispiele:

* `map.js`
* `map_countries.js`
* `map_variation_tempora.js`

Falls sinnvoll, dürfen Dateien umbenannt oder neu geschnitten werden, aber die funktionale Trennung muss erhalten bleiben.

## D3. Keine globalen Inline-Handler

Verboten sind Muster wie:

```html
onclick="toggleFullscreen()"
```

oder globale UI-Steuerung über `window.*`.

Stattdessen müssen Events lokal gebunden werden.

---

# E. Verbindliche Fullscreen-Spezifikation

## E1. Zielverhalten

Fullscreen muss:

* die Karte über den Content legen
* **nicht** über Header / Top-App-Bar gehen
* mobil und desktop stabil sein
* bei Escape beendet werden
* bei Resize sauber nachziehen
* nach Aktivierung und Deaktivierung Leaflet korrekt neu berechnen

## E2. Header-Offset

Die Headerhöhe wird dynamisch bestimmt.

Vorgabe:

```js
const header = document.querySelector(".md-header");
```

Die Höhe wird in die CSS-Variable geschrieben:

```js
--map-header-offset
```

## E3. Scroll-Sperre

Im Fullscreen-Modus muss Seitenscrollen deaktiviert werden.

Vorgabe:

* Klasse auf `html` oder `body`, z. B. `.has-map-fullscreen`
* dort `overflow: hidden`

## E4. Leaflet Resize

Nach jedem Wechsel in oder aus Fullscreen muss `map.invalidateSize()` mehrfach verzögert ausgelöst werden, mindestens:

* direkt nach Umschalten
* kurz nach dem Layoutwechsel

Beispiel:

```js
setTimeout(() => map.invalidateSize(), 60);
setTimeout(() => map.invalidateSize(), 220);
```

---

# F. Verbindliche CSS-Spezifikation

## F1. Alle Farben und Schriften nur aus dem Zensical-System

Verwenden:

* `--book-bg`
* `--book-surface-1`
* `--book-border`
* `--book-border-strong` falls vorhanden
* `--book-fg`
* `--book-muted`
* `--book-accent`
* `--book-shadow`
* `--book-shadow-md` falls vorhanden
* `--book-font-ui`

Nicht verwenden:

* harte Hex-Farben
* eigene Font-Stacks für Karteninhalte
* eigene isolierte Schattenwelt

## F2. Verbindlicher CSS-Sollzustand

Die Migration soll diesen funktionalen CSS-Zustand herstellen:

```css
:root {
  --map-header-offset: 4.5rem;
  --map-radius: var(--book-radius);
  --map-border: var(--book-border);
  --map-bg: var(--book-surface-1);
  --map-panel-bg: color-mix(in srgb, var(--book-bg) 92%, white);
  --map-panel-fg: var(--book-fg);
  --map-panel-muted: var(--book-muted);
  --map-shadow: var(--book-shadow);
  --map-shadow-md: var(--book-shadow-md);
  --map-control-size: 2.5rem;
}

@media (max-width: 767px) {
  :root {
    --map-header-offset: 3.5rem;
    --map-control-size: 2.25rem;
  }
}

.md-typeset .book-map {
  position: relative;
  inline-size: 100%;
  block-size: 22rem;
  margin: 1.25rem 0;
  border: 1px solid var(--map-border);
  border-radius: var(--map-radius);
  overflow: clip;
  background: var(--map-bg);
  box-shadow: var(--map-shadow);
  isolation: isolate;
  z-index: 0;
}

.md-typeset .book-map[data-map="variation"] {
  block-size: 40rem;
}

.md-typeset .book-map[data-map="variation_tempora"] {
  block-size: 31rem;
}

.md-typeset .book-map__canvas {
  inline-size: 100%;
  block-size: 100%;
  background: var(--map-bg);
}

.md-typeset .book-map .leaflet-control-container {
  z-index: 20;
}

.md-typeset .book-map .leaflet-control-zoom a,
.md-typeset .book-map .book-map__control {
  inline-size: var(--map-control-size);
  block-size: var(--map-control-size);
  display: inline-grid;
  place-items: center;
  border: 1px solid var(--book-border);
  border-radius: 0.7rem;
  background: var(--map-panel-bg);
  color: var(--book-fg);
  box-shadow: var(--map-shadow);
  backdrop-filter: blur(6px);
  transition:
    background-color 140ms ease,
    border-color 140ms ease,
    box-shadow 140ms ease,
    transform 140ms ease;
}

.md-typeset .book-map .leaflet-control-zoom a:hover,
.md-typeset .book-map .book-map__control:hover {
  border-color: var(--book-border-strong);
  box-shadow: var(--map-shadow-md);
}

.md-typeset .book-map .leaflet-control-zoom a:focus-visible,
.md-typeset .book-map .book-map__control:focus-visible {
  outline: none;
  box-shadow: var(--map-shadow), var(--book-focus);
}

.md-typeset .book-map__control--fullscreen {
  position: absolute;
  inset-inline-end: 0.75rem;
  inset-block-start: 0.75rem;
  z-index: 30;
  padding: 0;
  cursor: pointer;
}

.md-typeset .book-map.is-fullscreen {
  position: fixed !important;
  inset-inline: 0 !important;
  inset-block-start: var(--map-header-offset) !important;
  inline-size: 100vw !important;
  block-size: calc(100dvh - var(--map-header-offset)) !important;
  max-inline-size: none !important;
  margin: 0 !important;
  border-radius: 0 !important;
  border: 0 !important;
  box-shadow: none !important;
  z-index: 2600 !important;
}

.md-typeset .book-map.is-fullscreen .book-map__canvas {
  block-size: 100% !important;
}

.md-typeset .book-map.is-fullscreen::before {
  content: "";
  position: fixed;
  inset: 0;
  background: color-mix(in srgb, black 18%, transparent);
  z-index: -1;
}

.md-typeset .leaflet-popup-content-wrapper {
  border: 1px solid var(--book-border);
  border-radius: 0.9rem;
  background: var(--map-panel-bg);
  color: var(--book-fg);
  box-shadow: var(--map-shadow-md);
}

.md-typeset .leaflet-popup-content {
  margin: 0;
  padding: 0.9rem 1rem;
  font-family: var(--book-font-ui);
  font-size: 0.92rem;
  line-height: 1.5;
  max-inline-size: min(22rem, calc(100vw - 3rem));
  max-block-size: min(24rem, 52dvh);
  overflow: auto;
}

.md-typeset .leaflet-popup-tip {
  background: var(--map-panel-bg);
}

.md-typeset .leaflet-popup-close-button {
  color: var(--book-muted);
  inline-size: 2rem;
  block-size: 2rem;
  font-size: 1.1rem;
  padding: 0.25rem 0.4rem;
}

.md-typeset .leaflet-popup-close-button:hover {
  color: var(--book-fg);
}

.md-typeset .popup-sprachenkarte {
  font-family: var(--book-font-ui);
  color: var(--book-fg);
}

.md-typeset .popup-title {
  display: block;
  margin: 0 0 0.35rem 0;
  font-size: 0.98rem;
  line-height: 1.2;
  font-weight: 700;
  color: var(--book-accent);
}

.md-typeset .popup-familie,
.md-typeset .popup-hauptstadt {
  margin: 0 0 0.25rem 0;
  font-size: 0.84rem;
  line-height: 1.35;
  color: var(--book-muted);
  font-style: italic;
}

.md-typeset .popup-herkunft,
.md-typeset .popup-line {
  margin-top: 0.45rem;
}

.md-typeset .popup-label {
  color: var(--book-muted);
  font-size: 0.82rem;
}

.md-typeset .popup-value {
  color: var(--book-fg);
  font-weight: 650;
  font-size: 0.82rem;
  margin-inline-start: 0.25rem;
}

.md-typeset .leaflet-tooltip {
  border: 1px solid var(--book-border);
  border-radius: 0.55rem;
  background: var(--map-panel-bg);
  color: var(--book-fg);
  box-shadow: var(--map-shadow);
  font-family: var(--book-font-ui);
  font-size: 0.78rem;
  line-height: 1.3;
  padding: 0.35rem 0.5rem;
}

body.has-map-fullscreen {
  overflow: hidden;
}

@media (max-width: 599px) {
  .md-typeset .leaflet-popup-content {
    max-inline-size: calc(100vw - 2rem);
    max-block-size: 56dvh;
    padding: 0.8rem 0.9rem;
  }

  .md-typeset .popup-title {
    font-size: 0.92rem;
  }
}

body[data-md-color-scheme="slate"] .md-typeset .book-map,
body[data-md-color-scheme="slate"] .md-typeset .leaflet-popup-content-wrapper,
body[data-md-color-scheme="slate"] .md-typeset .leaflet-tooltip,
body[data-md-color-scheme="slate"] .md-typeset .book-map .leaflet-control-zoom a,
body[data-md-color-scheme="slate"] .md-typeset .book-map .book-map__control {
  background: color-mix(in srgb, var(--book-surface-1) 90%, black);
  color: var(--book-fg);
  border-color: var(--book-border);
}
```

## F3. Was explizit entfernt werden muss

Folgendes muss aus dem Altbestand entfernt oder ersetzt werden:

* globale Pane-Z-Index-Überschreibungen wie:

  * `.leaflet-tile-pane { z-index: ... !important; }`
  * `.leaflet-marker-pane { z-index: ... !important; }`
  * `.leaflet-popup-pane { z-index: ... !important; }`
* globale `transform: none !important`
* globale `filter: none !important`
* globale `perspective: none !important`
* `transition: all`
* harte Sonderregeln pro alter ID-Struktur

---

# G. Verbindliche JS-Spezifikation für map_ui.js

`map_ui.js` soll mindestens diese API bereitstellen:

```js
window.MapUI = {
  enableFullscreenUI,
  syncMapHeaderOffset
};
```

Sollverhalten:

```js
function getHeaderOffset() {
  const header = document.querySelector(".md-header");
  return header ? Math.ceil(header.getBoundingClientRect().height) : 72;
}

function syncMapHeaderOffset() {
  document.documentElement.style.setProperty("--map-header-offset", `${getHeaderOffset()}px`);
}

function enableFullscreenUI(container, map, button) {
  if (!container || !map || !button) return;

  const setState = (isFullscreen) => {
    container.classList.toggle("is-fullscreen", isFullscreen);
    document.body.classList.toggle("has-map-fullscreen", isFullscreen);

    button.setAttribute("aria-pressed", String(isFullscreen));
    button.setAttribute(
      "aria-label",
      isFullscreen ? "Vollbildmodus beenden" : "Karte im Vollbild öffnen"
    );

    button.innerHTML = isFullscreen
      ? '<span class="material-icons" aria-hidden="true">fullscreen_exit</span>'
      : '<span class="material-icons" aria-hidden="true">fullscreen</span>';

    syncMapHeaderOffset();
    setTimeout(() => map.invalidateSize(), 60);
    setTimeout(() => map.invalidateSize(), 220);
  };

  button.addEventListener("click", (e) => {
    e.preventDefault();
    e.stopPropagation();
    setState(!container.classList.contains("is-fullscreen"));
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && container.classList.contains("is-fullscreen")) {
      setState(false);
    }
  });

  window.addEventListener("resize", () => {
    syncMapHeaderOffset();
    if (container.classList.contains("is-fullscreen")) {
      map.invalidateSize();
    }
  });

  syncMapHeaderOffset();
}
```

---

# H. Verbindliche Vorgaben pro bestehender Datei

## H1. map.js

* auf container-lokale Selektoren umstellen
* keine globale ID-Initialisierung
* Leaflet an `.book-map__canvas` binden
* Datenlogik erhalten
* Popup-Markup erhalten
* Fullscreen über `MapUI.enableFullscreenUI(...)`

## H2. map_countries.js

Diese Datei ist besonders kritisch, weil sie bisher globaler arbeitet.

Pflicht:

* alle direkten `document.getElementById(...)`-Abhängigkeiten entfernen
* nur noch innerhalb des konkreten Containers arbeiten
* Fullscreen-Button nicht global suchen
* Karte ausschließlich im übergebenen Container initialisieren

## H3. map_variation_tempora.js

* gleiche Container-Architektur wie alle anderen Karten
* keine eigene Sonderlogik für Fullscreen außerhalb von `MapUI`
* die inhaltliche Marker-/Popup-Logik bleibt erhalten

## H4. map_ui.js

* nur gemeinsame UI- und Layout-Logik
* keine fachlichen Datenannahmen
* keine Kenntnis über konkrete JSON-Felder notwendig

---

# I. Accessibility-Spezifikation

Pflichtpunkte:

* Fullscreen-Button ist ein echtes `<button>`
* `aria-label` wechselt je nach Zustand
* `aria-pressed` wechselt je nach Zustand
* Controls haben sichtbaren `:focus-visible`-State
* Popups bleiben per Standard-Leaflet bedienbar
* keine rein visuellen Zustände ohne semantische Entsprechung

---

# J. Akzeptanzkriterien

Die Migration gilt nur dann als erfolgreich, wenn alle folgenden Prüfungen bestanden werden:

## J1. Funktional

* jede Karte lädt weiterhin ihre ursprüngliche JSON-Datei
* Marker erscheinen unverändert korrekt
* Tooltips erscheinen unverändert korrekt
* Popups zeigen weiterhin die vorgesehenen Informationen
* mehrere Karten können im Projekt parallel existieren

## J2. Layout

* keine Karte liegt unter oder über der Top-App-Bar
* Fullscreen funktioniert auf Desktop und Mobile
* Karten springen beim Wechsel nicht sichtbar kaputt
* keine abgeschnittenen Leaflet-Flächen
* keine überstehenden Controls

## J3. Design

* Controls wirken wie Zensical-Komponenten
* Popups und Tooltips passen zu Typografie und Farbwelt des Buches
* Light und Dark Mode funktionieren ohne harte Sonderfarben

## J4. Codequalität

* keine globalen IDs als Architekturprinzip
* keine globalen Fullscreen-Helfer
* keine globalen Leaflet-Z-Index-Hacks
* keine Hardcoded-Farben im Map-UI
* klare Trennung zwischen UI und fachlicher Kartenlogik

---

# K. Nicht verhandelbare Verbote

Die Umsetzung ist nicht akzeptabel, wenn einer der folgenden Punkte bestehen bleibt:

* globale Map-ID-Architektur
* Fullscreen mit `top: 0` trotz Header
* direkte Hardcoded-Farben im finalen Map-UI
* globale Leaflet-Pane-Z-Index-Hämmer
* Abhängigkeit auf genau eine Karte pro Seite
* Änderungen an JSON-Inhalten nur zur Vereinfachung der UI

---

# L. Erwartetes Endergebnis

Das Endergebnis soll kein notdürftig repariertes Legacy-System mehr sein, sondern eine saubere, modulare Zensical-Komponente.

Die Karten müssen sich danach anfühlen wie:

* systematisch eingebundene Buchbestandteile
* visuell konsistent
* technisch stabil
* erweiterbar für weitere Kartenarten
* kompatibel mit unterschiedlichen JSON-Datenquellen

