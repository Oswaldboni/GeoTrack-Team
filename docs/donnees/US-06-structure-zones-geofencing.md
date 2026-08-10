# US-06.1 — Structure géométrique des zones de geofencing

## Objectif

Définir le modèle de données permettant de représenter les zones de geofencing configurables par les gestionnaires GeoTrack.

Deux formes géométriques sont prises en charge :

- polygone ;
- cercle.

Cette structure sert de base à la détection d'entrée et de sortie des véhicules, aux alertes et à l'historique des événements de geofencing.

## Modèle proposé

```text
Zone {
  id: UUID
  nom: string
  type: enum("POLYGON", "CIRCLE")
  couleur: string
  createdBy: userId
  createdAt: timestamp

  // si type = POLYGON
  points: [
    {
      latitude: float,
      longitude: float
    }
  ]

  // si type = CIRCLE
  centre: {
    latitude: float,
    longitude: float
  }

  rayon: float
}
