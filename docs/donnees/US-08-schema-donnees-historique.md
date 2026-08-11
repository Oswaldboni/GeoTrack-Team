# US-08.2 — Schéma de données pour l'historique des trajets

## Objectif

Définir une structure de données cohérente pour stocker les informations des véhicules, les messages de télémétrie, les trajets et les zones géographiques du système GeoTrack.

## Entités principales

### Vehicle

Représente un véhicule enregistré dans GeoTrack.

Attributs proposés :

- `vehicle_id`
- `plate_number`
- `serial_number`
- `status`
- `created_at`

### Telemetry

Représente un message de télémétrie reçu d'un véhicule.

Attributs proposés :

- `telemetry_id`
- `vehicle_id`
- `latitude`
- `longitude`
- `speed_kmh`
- `direction_deg`
- `timestamp`
- `status`
- `diagnostic`

### Trip

Représente un trajet effectué par un véhicule.

Attributs proposés :

- `trip_id`
- `vehicle_id`
- `start_time`
- `end_time`
- `start_location`
- `end_location`
- `distance`
- `average_speed`

### Geofence

Représente une zone géographique surveillée.

Attributs proposés :

- `geofence_id`
- `name`
- `geometry`
- `created_at`

## Relations principales

- Un véhicule peut générer plusieurs messages de télémétrie.
- Un véhicule peut effectuer plusieurs trajets.
- Les données de télémétrie sont associées à un véhicule grâce à `vehicle_id`.
- Les trajets sont associés à un véhicule grâce à `vehicle_id`.

Représentation simplifiée :

```text
Vehicle 1 ---- N Telemetry
Vehicle 1 ---- N Trip
```

## Cohérence avec le message d'ingestion

Les noms `speed_kmh`, `direction_deg`, `status` et `diagnostic` sont alignés sur le schéma canonique `schemas/telemetry-message.schema.json`. Cette convention évite une traduction différente des champs entre l'ingestion et le stockage.

`telemetry_id` peut être généré par la plateforme lors de l'ingestion. L'unicité logique d'un message doit aussi pouvoir être vérifiée avec le véhicule, l'horodatage et, si le protocole le fournit, un numéro de séquence.

## Contraintes d'intégrité

- `vehicle_id` doit référencer un véhicule existant.
- `latitude` doit être comprise entre -90 et 90.
- `longitude` doit être comprise entre -180 et 180.
- `speed_kmh` doit être positive ou nulle.
- `direction_deg` doit être comprise entre 0 et 359.
- `timestamp` doit être enregistré en UTC au format ISO 8601.
- `plate_number` et `serial_number` doivent être uniques.
- `end_time` d'un trajet doit être postérieur à `start_time`.

## Partitionnement proposé

La télémétrie représente la table la plus volumineuse. Elle doit être partitionnée par période, par exemple par jour ou par mois selon la technologie retenue. L'index principal est composé de `vehicle_id` et `timestamp`. Un index géospatial est ajouté sur la position.

## Conclusion

Le modèle sépare les données stables des véhicules, les événements de télémétrie à fort volume, les trajets reconstruits et les zones géographiques. Il reste cohérent avec le contrat JSON d'ingestion et avec les requêtes d'historique prévues dans US-08.
