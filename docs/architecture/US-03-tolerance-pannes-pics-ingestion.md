# US-03.4 — Tolérance aux pannes lors des pics d'ingestion

## Objectif

Définir les mécanismes permettant à GeoTrack de continuer à accepter et traiter la télémétrie lorsqu'une panne survient pendant une période de forte charge.

## 1. Contexte

GeoTrack doit supporter un débit nominal d'environ :

**2 000 messages par seconde**

Ce débit peut temporairement augmenter lors :

- de reconnexions simultanées ;
- de reprises après une interruption réseau ;
- de retransmissions ;
- d'accumulations temporaires de télémétrie.

Une panne survenant pendant un pic peut réduire la capacité disponible au moment où le système en a le plus besoin.

L'architecture doit donc combiner scalabilité et tolérance aux pannes.

## 2. Principe général

La stratégie repose sur plusieurs niveaux de protection :

```text
Véhicules
    |
    v
Répartition de charge
    |
    v
+--------------------------+
| Instances d'ingestion    |
| I1     I2     I3         |
+--------------------------+
    |
    v
+--------------------------+
| Kafka                    |
| brokers + réplication    |
+--------------------------+
    |
    v
+--------------------------+
| Consumer group           |
| C1     C2     C3         |
+--------------------------+
    |
    v
Traitement / stockage
