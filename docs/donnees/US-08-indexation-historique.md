# US-08.3 — Index géospatiaux et temporels

## Objectif

Définir les index nécessaires pour optimiser les requêtes de restitution de l'historique des trajets et les recherches géospatiales dans GeoTrack.

## Index temporel

Un index sur le champ `timestamp` permet d'accélérer les recherches effectuées sur une période donnée.

Exemples de besoins :

- récupérer les données d'une journée ;
- récupérer les données d'une semaine ;
- filtrer les messages entre deux dates ;
- reconstruire un trajet dans l'ordre chronologique.

## Index composé par véhicule et temps

L'index principal proposé est un index composé sur :

`vehicle_id` + `timestamp`

Cet index permet de retrouver rapidement les données de télémétrie d'un véhicule particulier sur une période donnée.

Exemple de besoin :

- rechercher toutes les positions du véhicule V123 entre 08:00 et 12:00 ;
- reconstruire un trajet complet dans l'ordre chronologique.

Cet index évite de parcourir l'ensemble des données de télémétrie de la flotte.

## Index géospatial

Les coordonnées GPS doivent disposer d'un index géospatial.

Cet index permet notamment :

- de rechercher les véhicules présents dans une zone ;
- d'identifier les véhicules proches d'un point ;
- de supporter les traitements de geofencing ;
- d'optimiser les recherches basées sur la latitude et la longitude.

Les coordonnées peuvent être représentées sous forme d'un point géographique composé de la longitude et de la latitude.

## Requête de restitution d'un trajet

La restitution d'un trajet suit le principe suivant :

1. identifier le véhicule avec `vehicle_id` ;
2. définir la période recherchée ;
3. utiliser l'index composé `vehicle_id` + `timestamp` ;
4. récupérer les messages correspondants ;
5. trier les résultats par ordre chronologique ;
6. utiliser les coordonnées GPS pour reconstruire le trajet.

## Index proposés

| Index | Champs | Utilisation principale |
|---|---|---|
| Index temporel | `timestamp` | Recherche par période |
| Index véhicule-temporel | `vehicle_id`, `timestamp` | Historique d'un véhicule |
| Index géospatial | coordonnées GPS | Recherche par position et geofencing |

## Compromis

Les index améliorent les performances de lecture, mais ils présentent également certains coûts :

- consommation supplémentaire d'espace de stockage ;
- coût supplémentaire lors de l'écriture des messages ;
- maintenance des index lors de l'ajout de nouvelles données.

Compte tenu du volume élevé de télémétrie, seuls les index correspondant aux requêtes principales du système doivent être conservés.

## Conclusion

La combinaison d'un index temporel, d'un index composé par véhicule et temps, et d'un index géospatial permet d'optimiser les principaux scénarios de consultation de GeoTrack sans multiplier inutilement les index.
