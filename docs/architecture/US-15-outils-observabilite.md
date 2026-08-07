# US-15.1 — Choix des outils d'observabilité

## Objectif

Définir les outils permettant de centraliser les logs, collecter les métriques et superviser l'état technique de la plateforme GeoTrack.

## Besoins d'observabilité

GeoTrack doit permettre à l'équipe d'administration de surveiller le fonctionnement de la plateforme et de détecter rapidement les anomalies.

L'observabilité doit couvrir notamment :

- les logs applicatifs ;
- les logs techniques ;
- les métriques d'ingestion ;
- les performances des services ;
- l'utilisation des ressources ;
- la disponibilité des composants.

## Centralisation des logs : Loki

Loki est proposé pour centraliser les logs produits par les différents composants de GeoTrack.

Les logs doivent permettre notamment d'identifier :

- les erreurs d'ingestion ;
- les erreurs applicatives ;
- les interruptions de service ;
- les événements techniques importants ;
- les erreurs de communication entre composants.

La centralisation évite de devoir consulter séparément les logs de chaque service.

## Collecte des métriques : Prometheus

Prometheus est proposé pour collecter et conserver les métriques techniques de GeoTrack.

Les principales métriques à surveiller sont :

- nombre de messages de télémétrie reçus par seconde ;
- nombre de messages traités ;
- taux d'erreur d'ingestion ;
- latence de traitement ;
- disponibilité des services ;
- utilisation CPU ;
- utilisation mémoire ;
- espace de stockage disponible ;
- nombre d'alertes techniques.

## Visualisation : Grafana

Grafana est proposé comme outil de visualisation.

Il permet de construire des tableaux de bord techniques à partir des métriques collectées et de faciliter la consultation des informations nécessaires à la supervision.

Les administrateurs peuvent ainsi disposer d'une vue centralisée de l'état de GeoTrack.

## Architecture d'observabilité proposée

Le principe général est le suivant :

```text
Services GeoTrack
      |
      +------ métriques ------> Prometheus
      |                            |
      |                            v
      |                         Grafana
      |
      +--------- logs ---------> Loki
                                   |
                                   v
                                Grafana
