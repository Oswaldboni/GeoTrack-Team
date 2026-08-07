# US-07.2 — Service d'évaluation continue de la vitesse

## Objectif

Définir le fonctionnement du service GeoTrack chargé d'analyser en continu les messages de télémétrie afin de détecter les dépassements de vitesse.

## Entrées du service

Pour chaque message de télémétrie reçu, le service utilise notamment :

- `vehicle_id`
- vitesse mesurée ;
- latitude ;
- longitude ;
- horodatage ;
- type de route ou zone si disponible.

## Détermination de la vitesse limite

Le service détermine le seuil applicable selon l'ordre de priorité suivant :

1. seuil spécifique au véhicule ;
2. seuil associé au type de route ou à la zone ;
3. seuil par défaut du système.

## Logique d'évaluation

Pour chaque message reçu, le service compare :

`vitesse_mesuree`

avec :

`vitesse_limite`

Si :

`vitesse_mesuree > vitesse_limite`

alors un dépassement de vitesse est détecté.

Dans le cas contraire, aucun événement d'alerte n'est généré.

## Événement de dépassement

Lorsqu'un dépassement est détecté, le service prépare un événement contenant au minimum :

- identifiant du véhicule ;
- vitesse mesurée ;
- vitesse limite ;
- écart de vitesse ;
- latitude ;
- longitude ;
- horodatage.

## Traitement continu

Le service doit effectuer cette évaluation à chaque réception d'un nouveau message de télémétrie.

Le traitement suit le principe suivant :

1. réception d'un message de télémétrie ;
2. identification du véhicule ;
3. détermination du seuil applicable ;
4. comparaison entre vitesse réelle et vitesse limite ;
5. génération éventuelle d'un événement d'alerte ;
6. transmission de l'événement au mécanisme de notification.

## Pseudo-logique

```text
recevoir message de télémétrie
        |
        v
identifier le véhicule
        |
        v
déterminer le seuil applicable
        |
        v
vitesse_mesuree > vitesse_limite ?
        |
    oui | non
        | 
        v
générer événement d'alerte
