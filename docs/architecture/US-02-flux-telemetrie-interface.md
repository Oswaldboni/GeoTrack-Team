# US-02.2 — Flux de données entre télémétrie et interface utilisateur

## Objectif

Définir le flux de données permettant à GeoTrack d'acheminer efficacement les nouvelles positions des véhicules vers l'interface utilisateur afin de maintenir un affichage fluide et presque en temps réel.

## Flux général

Le flux proposé est le suivant :

```text
Véhicules
   |
   v
Service d'ingestion
   |
   v
Validation et traitement
   |
   v
Service de télémétrie
   |
   v
Service de diffusion temps réel
   |
   v
WebSocket
   |
   v
Interface GeoTrack
   |
   v
Mise à jour de la carte
