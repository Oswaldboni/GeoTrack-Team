# US-02.1 — Rafraîchissement en temps réel des positions

## Objectif

Définir le mécanisme utilisé par GeoTrack pour mettre à jour rapidement les positions des véhicules dans l'interface utilisateur.

## Solutions étudiées

Deux approches principales sont considérées :

- polling HTTP ;
- WebSocket.

## 1. Polling HTTP

Avec le polling HTTP, le client interroge régulièrement le serveur pour demander les nouvelles positions.

Exemple :

```text
Client
  |
  |---- requête HTTP ----> Serveur
  |<--- positions --------|
  |
  | attente
  |
  |---- requête HTTP ----> Serveur
  |<--- positions --------|
