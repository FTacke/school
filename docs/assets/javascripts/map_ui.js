// docs/assets/javascripts/map_ui.js
// Gemeinsame UI-Funktionen für alle Leaflet-Karten im Projekt
// CO.RA.PAN-Style: Responsive Click-Popups, keine Hover-Tooltips

/**
 * Erkennt, ob der Viewport mobil ist (max-width: 599px)
 * @returns {boolean}
 */
function isMobileViewport() {
  return window.matchMedia("(max-width: 599px)").matches;
}

/**
 * Standard-Popup-Optionen (CO.RA.PAN-Style)
 * @param {string} className - CSS-Klassenname für das Popup
 * @returns {object} Leaflet popup options
 */
function popupOptions(className) {
  const mobile = isMobileViewport();
  return {
    className: className || 'corapan-popup',
    closeButton: true,
    autoClose: true,
    closeOnClick: false, // wir steuern map-click selbst
    autoPan: true,
    keepInView: true,
    maxWidth: mobile ? 280 : 320,
    minWidth: mobile ? 180 : 200,
    autoPanPaddingTopLeft: mobile ? [20, 80] : [50, 100],
    autoPanPaddingBottomRight: mobile ? [20, 20] : [50, 50],
  };
}

/**
 * Bindet ein Click-Popup an einen Marker mit automatischem Pan
 * @param {L.Map} map - Leaflet Map-Instanz
 * @param {L.Marker} marker - Marker-Objekt
 * @param {string} html - HTML-Inhalt des Popups
 * @param {string} className - CSS-Klassenname für das Popup
 */
function bindClickPopup(map, marker, html, className) {
  marker.bindPopup(html, popupOptions(className));
  marker.on("click", (e) => {
    // Verhindere Map-Click-Event-Bubbling
    L.DomEvent.stopPropagation(e);
    // Pan zur Marker-Position
    map.panTo(e.latlng, { animate: true, duration: 0.3 });
    // Öffne Popup
    marker.openPopup();
  });
}

/**
 * Aktiviert globales UX für Popup-Schließen
 * - Click auf Karte schließt Popup
 * - Esc-Taste schließt Popup (Desktop)
 * @param {L.Map} map - Leaflet Map-Instanz
 */
function enablePopupCloseUX(map) {
  // Click auf freie Kartenfläche schließt Popup
  map.on("click", () => {
    map.closePopup();
  });

  // Esc schließt Popup (Desktop) - nur einmal pro Dokument binden
  if (!window.__mapUIEscHandlerBound) {
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        // Schließe alle offenen Popups in allen Maps
        document.querySelectorAll('.leaflet-popup-close-button').forEach(btn => btn.click());
      }
    });
    window.__mapUIEscHandlerBound = true;
  }
}

/**
 * Aktiviert robuste Resize/Orientation-Behandlung
 * @param {L.Map} map - Leaflet Map-Instanz
 */
function enableResponsiveInvalidation(map) {
  const handler = () => setTimeout(() => map.invalidateSize(), 200);
  window.addEventListener("resize", handler);
  window.addEventListener("orientationchange", handler);
}

/**
 * Verhindert doppelte Initialisierung einer Karte
 * @param {HTMLElement} container - Map-Container-Element
 * @returns {boolean} true wenn bereits initialisiert
 */
function isMapInitialized(container) {
  return container.dataset.mapInitialized === "true";
}

/**
 * Markiert einen Map-Container als initialisiert
 * @param {HTMLElement} container - Map-Container-Element
 */
function markMapInitialized(container) {
  container.dataset.mapInitialized = "true";
}

// Export für ES6-Module (falls verwendet)
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    isMobileViewport,
    popupOptions,
    bindClickPopup,
    enablePopupCloseUX,
    enableResponsiveInvalidation,
    isMapInitialized,
    markMapInitialized
  };
}

// Globaler Namespace für Nicht-Modul-Verwendung
window.MapUI = {
  isMobileViewport,
  popupOptions,
  bindClickPopup,
  enablePopupCloseUX,
  enableResponsiveInvalidation,
  isMapInitialized,
  markMapInitialized
};
