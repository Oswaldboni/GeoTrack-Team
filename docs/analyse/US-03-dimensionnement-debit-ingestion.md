# US-03 — Dimensionnement du débit d’ingestion

## Sous-tâche associée

**GTB-89 — Dimensionner le débit global requis (calculs du nombre de messages par seconde - MPS)**

## Objectif

Déterminer le débit nominal de télémétrie que l’architecture GeoTrack doit être capable d’ingérer pour une flotte de 10 000 véhicules.

Ce calcul sert de base au dimensionnement des composants d’ingestion, du système de messagerie et des services de traitement.

## Hypothèses de départ

Le dimensionnement repose sur les paramètres suivants :

- nombre de véhicules : **10 000** ;
- fréquence d’émission : **1 message toutes les 5 secondes par véhicule** ;
- fonctionnement : **24 heures sur 24, 7 jours sur 7**.

## Calcul du débit nominal

Le débit nominal est obtenu avec la formule suivante :

```text
Débit = nombre de véhicules / intervalle d'émission
