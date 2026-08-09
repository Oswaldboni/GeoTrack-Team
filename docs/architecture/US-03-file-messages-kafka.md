# US-03.2 — File de messages pour l'absorption des pics de trafic

## Objectif

Définir le mécanisme de messagerie permettant à GeoTrack d'absorber les variations et les pics temporaires du trafic de télémétrie sans coupler directement l'ingestion aux services de traitement.

## 1. Contexte

GeoTrack reçoit nominalement :

- 10 000 véhicules ;
- un message toutes les 5 secondes par véhicule ;
- soit environ 2 000 messages par seconde.

Ce débit représente une moyenne nominale.

Des pointes temporaires peuvent apparaître lors de reconnexions simultanées, de retransmissions ou de reprises après une perturbation réseau.

## 2. Problématique

Sans file de messages, le flux peut être directement dépendant de la capacité des services consommateurs :

```text
Véhicules
    |
    v
Ingestion
    |
    v
Traitement
