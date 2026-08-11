# US-04.3 — Affichage dynamique des marqueurs de véhicules

## Objectif

Documenter le mécanisme d'affichage et de mise à jour dynamique des marqueurs de véhicules sur la carte GeoTrack.

Cette conception correspond à la sous-tâche Jira GTB-55.

## Bibliothèque utilisée

L'implémentation repose sur **Leaflet.js**.

La carte est initialisée sur une zone géographique et utilise les tuiles OpenStreetMap pour l'affichage cartographique.

## Distinction visuelle des statuts

Deux styles de marqueurs sont définis afin de distinguer rapidement l'état des véhicules :

- vert : véhicule actif ;
- gris : véhicule inactif.

Les marqueurs utilisent `L.divIcon()` afin de créer des icônes personnalisées.

Exemple conceptuel :

```javascript
const activeIcon = L.divIcon({
  className: 'marker-active'
});

const inactiveIcon = L.divIcon({
  className: 'marker-inactive'
});
```

## Registre des marqueurs

Les marqueurs sont conservés dans une structure indexée par `vehicle_id`. Une mise à jour modifie la position et l'apparence du marqueur existant au lieu de créer un nouvel objet.

```javascript
const markersByVehicleId = new Map();

function updateVehicleMarker(vehicle) {
  const marker = markersByVehicleId.get(vehicle.vehicle_id);

  if (marker) {
    marker.setLatLng([vehicle.latitude, vehicle.longitude]);
    marker.setIcon(vehicle.status === 'ACTIVE' ? activeIcon : inactiveIcon);
    return;
  }

  const created = L.marker(
    [vehicle.latitude, vehicle.longitude],
    { icon: vehicle.status === 'ACTIVE' ? activeIcon : inactiveIcon }
  );
  created.addTo(map);
  markersByVehicleId.set(vehicle.vehicle_id, created);
}
```

## Maîtrise du volume

Pour 10 000 véhicules, le rendu doit combiner le regroupement de marqueurs, le filtrage selon la zone visible et une fréquence de rafraîchissement bornée. Les positions intermédiaires peuvent être remplacées par la plus récente pour l'affichage, sans supprimer les données historiques persistées.

Le plugin de regroupement doit être testé avec la fréquence réelle de mise à jour. Le simple fait de pouvoir créer 10 000 marqueurs ne garantit pas un rendu fluide à 2 000 mises à jour par seconde.

## Ordre des événements

Chaque marqueur conserve l'horodatage ou le numéro de séquence de sa dernière mise à jour. Une donnée plus ancienne est ignorée afin d'éviter un retour en arrière après une reconnexion.

## Critères de validation

- Un véhicule correspond à un seul marqueur.
- Une nouvelle position déplace le marqueur existant.
- Un événement ancien est ignoré.
- Les statuts sont distinguables sans dépendre uniquement de la couleur.
- La carte reste utilisable avec 10 000 véhicules enregistrés lors du scénario de performance.

## Conclusion

L'utilisation d'un registre indexé, du filtrage et du regroupement évite les doublons et limite le coût du rendu. La performance doit être confirmée avec un test dans le navigateur, pas seulement par une maquette statique.
