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
```

## Règles de validation

### Polygone

- Au moins trois sommets distincts sont requis.
- Le premier et le dernier point sont reliés pour fermer la forme.
- Les segments ne doivent pas s'auto-intersecter.
- Chaque latitude est comprise entre -90 et 90 et chaque longitude entre -180 et 180.

### Cercle

- Le centre contient une latitude et une longitude valides.
- Le rayon est strictement positif et exprimé en mètres.
- Les propriétés réservées au polygone sont absentes.

## Représentation géospatiale

Lorsque GeoJSON est utilisé, les coordonnées suivent l'ordre `[longitude, latitude]`. Cet ordre doit être documenté, car il est inverse de la présentation courante « latitude, longitude ».

Un index géospatial est appliqué à la géométrie pour limiter la recherche aux zones candidates proches d'une position.

## Cycle de vie

Une zone possède aussi un statut `ACTIVE` ou `INACTIVE` et des dates de modification. La désactivation conserve l'historique des événements existants sans continuer à produire de nouveaux franchissements.

## Critères de validation

- Une zone circulaire ou polygonale valide peut être créée.
- Une géométrie invalide est refusée avec un message précis.
- Une zone désactivée ne produit plus de nouvel événement.
- L'ordre des coordonnées GeoJSON est testé.
- Les modifications sont attribuées à un utilisateur et horodatées.

## Conclusion

Le modèle prend en charge les cercles et les polygones avec des contraintes explicites. La validation géométrique, le statut de la zone et l'index spatial préparent une détection fiable des franchissements.
