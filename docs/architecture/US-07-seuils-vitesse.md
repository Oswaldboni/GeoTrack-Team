# US-07.1 — Configuration des seuils de vitesse

## Objectif

Définir les règles permettant à GeoTrack de déterminer la limite de vitesse applicable à chaque véhicule afin de détecter les dépassements.

## Seuil par type de route ou zone

GeoTrack doit pouvoir associer une limite de vitesse à un type de route ou à une zone géographique.

Exemples de règles :

- zone urbaine ;
- route secondaire ;
- autoroute ;
- zone privée ou interne à l'entreprise.

La valeur configurée constitue le seuil par défaut applicable lorsque le véhicule ne possède pas de règle spécifique.

## Seuil spécifique par véhicule

Un seuil particulier peut être associé à un véhicule lorsque ses contraintes d'exploitation nécessitent une limite différente.

Exemples :

- véhicule lourd ;
- véhicule transportant une charge particulière ;
- véhicule soumis à une politique interne plus restrictive.

## Priorité des règles

L'ordre de priorité proposé est le suivant :

1. seuil spécifique au véhicule ;
2. seuil défini pour le type de route ou la zone ;
3. seuil par défaut du système si aucune règle plus précise n'est disponible.

## Données utilisées

Pour déterminer si un dépassement est présent, GeoTrack utilise notamment :

- `vehicle_id`
- vitesse mesurée ;
- vitesse limite applicable ;
- type de route ou zone ;
- latitude ;
- longitude ;
- horodatage.

## Règle de détection

Si :

`vitesse_mesuree > vitesse_limite`

alors le système considère qu'un dépassement de vitesse est présent.

## Résultat attendu

Pour chaque message de télémétrie reçu, GeoTrack doit pouvoir déterminer la vitesse limite applicable afin que le service d'évaluation puisse comparer la vitesse réelle à cette limite et décider si une alerte doit être générée.
