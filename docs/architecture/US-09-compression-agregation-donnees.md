# US-09.3 — Stratégie de compression et d'agrégation des données anciennes

## Objectif

Définir une stratégie permettant de réduire les coûts de stockage des données historiques GeoTrack grâce à la compression et à l'agrégation, tout en préservant les informations nécessaires aux analyses.

## 1. Principe général

GeoTrack produit un volume important de données de télémétrie.

Pour 10 000 véhicules transmettant toutes les 5 secondes, le système reçoit environ 2 000 messages par seconde.

Avec le temps, toutes ces données n'ont pas besoin du même niveau de performance ni de la même granularité pour être analysées.

La stratégie proposée combine donc :

- hiérarchisation des données ;
- compression ;
- agrégation ;
- conservation selon la politique de rétention.

## 2. Compression des données

Les données transférées vers les niveaux de stockage tiède et froid doivent être compressées lorsque la technologie de stockage utilisée le permet.

La compression vise à :

- réduire l'espace occupé ;
- diminuer les coûts de stockage ;
- réduire certains volumes de transfert ;
- conserver les données historiques avec une empreinte plus faible.

La méthode de compression exacte dépendra de la technologie de stockage retenue.

## 3. Agrégation des données

Pour certaines analyses historiques, il n'est pas nécessaire de parcourir chaque message individuel de télémétrie.

Des données agrégées peuvent être calculées périodiquement.

### Agrégations quotidiennes proposées

Pour chaque véhicule et chaque journée, GeoTrack peut calculer :

- distance totale parcourue ;
- vitesse moyenne ;
- vitesse maximale ;
- nombre de trajets ;
- durée totale d'utilisation ;
- nombre d'alertes ;
- nombre d'événements importants.

## 4. Granularité selon l'ancienneté

### Données récentes

Les données du Hot Tier conservent leur granularité complète afin de supporter les opérations et analyses récentes.

### Données intermédiaires

Les données du Warm Tier peuvent conserver les données brutes tout en disposant également d'agrégats permettant d'accélérer les requêtes historiques.

### Données anciennes

Les données du Cold Tier privilégient la compression et les agrégats pour les analyses courantes.

Les données brutes restent soumises à la politique de rétention définie par GeoTrack.

## 5. Exemple d'agrégat

Un enregistrement journalier pourrait contenir :

```json
{
  "vehicle_id": "VH-000123",
  "date": "2026-08-07",
  "distance_km": 286.4,
  "average_speed_kmh": 54.2,
  "max_speed_kmh": 108.7,
  "trip_count": 12,
  "operating_minutes": 415,
  "alert_count": 3
}
