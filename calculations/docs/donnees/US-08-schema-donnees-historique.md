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
- `speed`
- `direction`
- `timestamp`
- `vehicle_status`
- `diagnostic_data`

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
