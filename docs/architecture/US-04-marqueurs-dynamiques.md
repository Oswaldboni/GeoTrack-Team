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
