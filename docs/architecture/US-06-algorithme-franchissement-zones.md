# US-06.2 — Algorithme de détection de franchissement de zones

## Objectif

Définir l'algorithme permettant de déterminer en quasi temps réel si un véhicule se trouve à l'intérieur ou à l'extérieur d'une zone de geofencing, puis de détecter les événements d'entrée et de sortie.

Cette conception s'appuie sur le modèle de zones défini dans US-06.1.

## 1. Cas d'une zone circulaire

Une zone circulaire est définie par :

- un centre ;
- un rayon exprimé en mètres.

Pour déterminer si un véhicule se trouve dans la zone, la distance entre sa position GPS et le centre est calculée.

Pour des coordonnées géographiques, la formule de Haversine peut être utilisée.

La règle est :

```text
distance(position_vehicule, centre_zone) <= rayon
