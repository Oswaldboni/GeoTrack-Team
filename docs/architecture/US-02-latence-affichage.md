# US-02.3 — Gestion de la latence d'affichage

## Objectif

Définir les mécanismes permettant à GeoTrack de maintenir une latence d'affichage compatible avec l'exigence de visualisation des positions en moins de quelques secondes.

## 1. Définition de la latence

La latence d'affichage correspond au délai entre la production d'une nouvelle position par un véhicule et sa disponibilité pour l'affichage dans l'interface GeoTrack.

Le délai de bout en bout peut être représenté ainsi :

```text
Véhicule
   |
   v
Transmission
   |
   v
Ingestion
   |
   v
Traitement
   |
   v
Diffusion temps réel
   |
   v
WebSocket
   |
   v
Interface utilisateur
   |
   v
Mise à jour de la carte
