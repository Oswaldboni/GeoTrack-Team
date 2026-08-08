# US-01.2 — Spécification technique du protocole d'ingestion

## Objectif

Définir le mécanisme permettant à GeoTrack de recevoir en continu les messages de télémétrie transmis par les véhicules de la flotte.

## Charge attendue

GeoTrack doit gérer :

- 10 000 véhicules ;
- un message toutes les 5 secondes par véhicule ;
- un fonctionnement 24 h/24 et 7 j/7.

Le débit théorique est donc :

10 000 / 5 = **2 000 messages par seconde**

Le mécanisme d'ingestion doit être dimensionné pour supporter au minimum cette charge moyenne, avec une marge pour les pointes temporaires.

## Format des messages

Chaque message reçu doit respecter le schéma JSON défini dans US-01.1.

Les données principales comprennent notamment :

- identifiant du véhicule ;
- coordonnées GPS ;
- vitesse ;
- direction ;
- horodatage ;
- état du véhicule ;
- informations de diagnostic éventuelles.

## Flux d'ingestion proposé

Le traitement d'un message suit les étapes suivantes :

1. réception du message ;
2. validation du format JSON ;
3. vérification des champs obligatoires ;
4. contrôle des valeurs principales ;
5. rejet et journalisation si le message est invalide ;
6. acceptation du message s'il est valide ;
7. transmission vers le pipeline de traitement ;
8. stockage ou publication vers les composants consommateurs.

## Architecture logique

```text
Véhicule
   |
   v
Service d'ingestion
   |
   +--> Validation JSON
   |
   +--> Vérification des données
   |
   +--> Journalisation des erreurs
   |
   v
Pipeline de traitement
   |
   +--> Stockage
   |
   +--> Services temps réel
   |
   +--> Alertes et tableaux de bord
