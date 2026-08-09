# US-04.1 — Choix de la bibliothèque de cartographie

## Objectif

Choisir la bibliothèque de cartographie utilisée par GeoTrack pour afficher les véhicules sur une carte et justifier ce choix.

## Choix retenu

**Leaflet**

## Justification

### Coût

Leaflet est open-source et gratuit.

Ce choix évite les coûts liés à une solution comme Mapbox lorsque le volume d'utilisation ou le nombre de chargements de cartes augmente.

Pour GeoTrack, qui doit gérer jusqu'à 10 000 véhicules et un rafraîchissement régulier de la carte, ce critère est important.

### Performance à grande échelle

Leaflet peut être utilisé avec le plugin :

`Leaflet.markercluster`

Ce plugin permet de regrouper les marqueurs proches afin de limiter le nombre d'éléments affichés simultanément sur la carte.

Cette approche permet de réduire la charge côté navigateur lorsqu'un grand nombre de véhicules doit être représenté.

### Simplicité d'intégration

Leaflet fournit une API JavaScript légère et bien documentée.

La bibliothèque possède également une large communauté, ce qui facilite :

- l'intégration ;
- la recherche de documentation ;
- le développement ;
- la maintenance.

### Adéquation avec les besoins de GeoTrack

GeoTrack a principalement besoin :

- d'un affichage 2D ;
- de marqueurs représentant les véhicules ;
- de mises à jour de position ;
- d'interactions simples avec la carte.

Ces besoins sont couverts par Leaflet sans nécessiter de fonctionnalités avancées de rendu 3D.

## Alternative étudiée : Mapbox

Mapbox offre notamment :

- un rendu visuel plus moderne ;
- des fonctions basées sur WebGL ;
- des possibilités de personnalisation plus avancées.

Cependant, son modèle de tarification et sa complexité supplémentaire ne sont pas jugés nécessaires pour les besoins actuels du projet.

## Compromis retenu

Leaflet offre moins de possibilités avancées de rendu que Mapbox, mais présente un meilleur compromis pour GeoTrack entre :

- coût ;
- simplicité ;
- performances ;
- besoins fonctionnels.

## Décision architecturale

**Leaflet est retenu comme bibliothèque de cartographie pour GeoTrack.**

Le plugin `Leaflet.markercluster` peut être utilisé lorsque le nombre de véhicules affichés simultanément devient important.

## Conclusion

Le choix de Leaflet permet de répondre aux besoins de cartographie de GeoTrack avec une solution légère, gratuite et suffisamment performante pour l'affichage 2D de la flotte.
