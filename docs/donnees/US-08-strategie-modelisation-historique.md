# US-08.4 — Stratégie de modélisation de l'historique des trajets

## 1. Objectif

Cette documentation présente la stratégie de modélisation retenue pour assurer le stockage, la conservation et la restitution de l'historique des trajets du système GeoTrack.

La stratégie doit répondre à trois contraintes principales :

- un volume élevé de télémétrie ;
- des recherches temporelles et géospatiales ;
- une conservation des données pendant deux ans.

## 2. Contexte de volumétrie

GeoTrack doit supporter une flotte de 10 000 véhicules transmettant chacun un message de télémétrie toutes les 5 secondes.

Cela représente :

- 2 000 messages par seconde ;
- 172 800 000 messages par jour ;
- 63 072 000 000 messages par année ;
- 126 144 000 000 messages sur deux ans.

Avec une hypothèse de 300 octets par message, le volume brut estimé sur deux ans est d'environ 37,84 To.

Une capacité supérieure doit être prévue afin de tenir compte des index, métadonnées, sauvegardes, réplications et marges opérationnelles.

## 3. Modèle de données

La stratégie repose sur la séparation des données relativement stables des véhicules et des données générées continuellement.

Les principales entités sont :

### Vehicle

Contient les informations générales et relativement stables du véhicule.

### Telemetry

Contient les données reçues périodiquement :

- position GPS ;
- vitesse ;
- direction ;
- horodatage ;
- état du véhicule ;
- informations de diagnostic.

### Trip

Représente un trajet reconstruit à partir des données de télémétrie.

### Geofence

Représente les zones géographiques utilisées pour les fonctionnalités de surveillance et de geofencing.

## 4. Relations principales

Les relations principales sont :

`Vehicle 1 ---- N Telemetry`

`Vehicle 1 ---- N Trip`

Chaque message de télémétrie est associé à un véhicule à l'aide de `vehicle_id`.

Chaque trajet est également associé au véhicule concerné.

## 5. Stratégie d'indexation

Trois mécanismes d'indexation principaux sont retenus.

### Index temporel

Un index sur `timestamp` permet d'optimiser les recherches effectuées sur une période donnée.

### Index véhicule-temporel

Un index composé sur :

`vehicle_id + timestamp`

permet de récupérer efficacement l'historique d'un véhicule entre deux dates et constitue l'index principal pour la restitution des trajets.

### Index géospatial

Un index sur les coordonnées géographiques permet :

- les recherches basées sur la position ;
- la détection des véhicules présents dans une zone ;
- les fonctionnalités de geofencing.

## 6. Restitution d'un trajet

La restitution d'un trajet suit les étapes suivantes :

1. identifier le véhicule ;
2. déterminer l'intervalle temporel recherché ;
3. rechercher les messages à l'aide de l'index `vehicle_id + timestamp` ;
4. récupérer les données correspondantes ;
5. les ordonner chronologiquement ;
6. utiliser les coordonnées GPS pour reconstruire le trajet.

## 7. Gestion du stockage à long terme

Compte tenu du volume généré, toutes les données ne doivent pas nécessairement conserver le même niveau d'accès pendant deux ans.

La stratégie pourra distinguer :

- les données récentes fréquemment consultées ;
- les données plus anciennes moins fréquemment utilisées ;
- les données archivées destinées principalement à la conservation à long terme.

La compression, l'agrégation et l'archivage pourront être utilisés afin de maîtriser les coûts de stockage.

Ces mécanismes seront détaillés dans la stratégie de rétention des données.

## 8. Compromis architecturaux

La stratégie retenue cherche un équilibre entre :

- performance des écritures ;
- rapidité des recherches ;
- capacité de stockage ;
- coût des index ;
- disponibilité des données ;
- évolutivité du système.

L'ajout d'index améliore les performances de lecture mais augmente l'espace utilisé et le coût des écritures. Les index doivent donc correspondre aux scénarios de requêtes réellement nécessaires.

## 9. Conclusion

La stratégie de modélisation proposée sépare les données stables des véhicules des données de télémétrie à fort volume.

L'utilisation d'index temporels, véhicule-temporels et géospatiaux permet d'optimiser la restitution des trajets et les recherches géographiques.

Cette architecture prépare également GeoTrack à la conservation de deux années de données et à la mise en place ultérieure d'une stratégie de hiérarchisation, de compression et d'archivage.
