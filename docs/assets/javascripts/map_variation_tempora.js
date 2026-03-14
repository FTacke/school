// docs/assets/javascripts/map_variation_tempora.js
// Karte zur Tempusvariation.

(function () {
  const MAP_TYPE = 'variation_tempora';
  const DATA_PATH = 'assets/data/variation_tempora.json';

  function isCoordinatePair(value) {
    return Array.isArray(value) && value.length === 2 && value.every((item) => typeof item === 'number');
  }

  function getCoordinateList(rawCoordinates) {
    if (isCoordinatePair(rawCoordinates)) {
      return [rawCoordinates];
    }

    return Array.isArray(rawCoordinates) ? rawCoordinates.filter(isCoordinatePair) : [];
  }

  function getMarkerColor(usage) {
    if (!usage) {
      return 'hsl(209 74% 45%)';
    }

    if (usage.includes('Prototyp')) {
      return 'hsl(2 63% 49%)';
    }

    if (usage.includes('Neutralisierung')) {
      return 'hsl(29 92% 48%)';
    }

    if (usage.includes('Andenraum')) {
      return 'hsl(134 42% 38%)';
    }

    return 'hsl(209 74% 45%)';
  }

  function normalizeTemporaItem(raw) {
    const usage = raw['Verwendung der Tempora'] ?? '';
    const color = getMarkerColor(usage);

    return {
      title: raw.Land ?? '',
      subtitle: raw.Hauptstadt ?? '',
      perfectoCompuesto: raw['Perfecto compuesto'] ?? '',
      perfectoSimple: raw['Perfecto simple'] ?? '',
      usage,
      points: getCoordinateList(raw.Koordinaten),
      markerOptions: {
        color,
        fillColor: color,
        radius: 8,
        fillOpacity: 0.7,
        weight: 2
      }
    };
  }

  function buildPopupHtml(item) {
    return `
      <div class="popup-sprachenkarte">
        <div class="popup-title">${item.title}</div>
        <div class="popup-hauptstadt">${item.subtitle}</div>
        ${item.perfectoCompuesto ? `<div class="popup-line"><span class="popup-label">Perfecto compuesto:</span> <span class="popup-value">${item.perfectoCompuesto}</span></div>` : ''}
        ${item.perfectoSimple ? `<div class="popup-line"><span class="popup-label">Perfecto simple:</span> <span class="popup-value">${item.perfectoSimple}</span></div>` : ''}
        ${item.usage ? `<div class="popup-line"><span class="popup-label">Verwendung:</span> <span class="popup-value">${item.usage}</span></div>` : ''}
      </div>`;
  }

  function createTileLayer() {
    return L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: 'Map data © <a href="https://openstreetmap.org">OpenStreetMap</a>'
    });
  }

  function setInitialView(map, isMobile) {
    if (isMobile) {
      map.setView([-10, -65], 3);
      return;
    }

    map.setView([20, -40], 3);
  }

  function fitDesktopBounds(map, bounds) {
    const paddedBounds = bounds.pad(0.1);
    const targetZoom = map.getBoundsZoom(paddedBounds) + 1;
    map.setView(paddedBounds.getCenter(), targetZoom, { animate: false });
  }

  function initContainer(container) {
    if (!container || (window.MapUI && window.MapUI.isMapInitialized(container))) {
      return;
    }

    const mapCanvas = container.querySelector('.book-map__canvas');
    const fullscreenButton = container.querySelector('.book-map__control--fullscreen');

    if (!mapCanvas) {
      return;
    }

    const map = L.map(mapCanvas);
    const isMobile = window.MapUI ? window.MapUI.isMobileViewport() : window.matchMedia('(max-width: 599px)').matches;
    setInitialView(map, isMobile);

    createTileLayer().addTo(map);

    if (window.MapUI) {
      window.MapUI.enablePopupCloseUX(map);
      window.MapUI.enableResponsiveInvalidation(map);
      window.MapUI.enableFullscreenUI(container, map, fullscreenButton);
      window.MapUI.markMapInitialized(container);
    }

    const base = window.ZENSICAL_BASE_PATH || '/';
    fetch(`${base}${DATA_PATH}`)
      .then((response) => response.json())
      .then((regions) => {
        const bounds = L.latLngBounds([]);
        const markerLayer = L.layerGroup().addTo(map);

        regions.map(normalizeTemporaItem).forEach((item) => {
          item.points.forEach((point) => {
            const marker = L.circleMarker(point, item.markerOptions).addTo(markerLayer);
            const popupHtml = buildPopupHtml(item);

            if (window.MapUI) {
              window.MapUI.bindClickPopup(map, marker, popupHtml, 'corapan-popup');
            } else {
              marker.bindPopup(popupHtml);
            }

            bounds.extend(point);
          });
        });

        if (bounds.isValid() && !isMobile) {
          fitDesktopBounds(map, bounds);
        }
      })
      .catch((error) => {
        console.error('Fehler beim Laden der Variation-Tempora-Daten:', error);
      });
  }

  function initTemporaMaps() {
    document.querySelectorAll(`.book-map[data-map="${MAP_TYPE}"]`).forEach(initContainer);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTemporaMaps);
  } else {
    initTemporaMaps();
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(() => {
      initTemporaMaps();
    });
  }
})();

