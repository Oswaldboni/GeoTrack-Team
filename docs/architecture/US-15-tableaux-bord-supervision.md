# US-15.2 — Tableaux de bord de supervision technique

## Objectif

Définir les tableaux de bord techniques permettant à l'équipe d'administration de surveiller GeoTrack et de détecter rapidement les anomalies affectant l'ingestion, l'infrastructure et le stockage.

## 1. Tableau de bord d'ingestion

Ce tableau de bord permet de surveiller le flux de télémétrie reçu par GeoTrack.

Les indicateurs principaux sont :

- nombre de messages reçus par seconde ;
- nombre de messages traités par seconde ;
- nombre de messages rejetés ;
- taux d'erreur d'ingestion ;
- latence moyenne de traitement ;
- évolution du débit dans le temps.

Une baisse importante du nombre de messages reçus ou une augmentation du taux d'erreur peut signaler une anomalie du pipeline d'ingestion.

## 2. Tableau de bord infrastructure

Ce tableau de bord permet de surveiller les ressources utilisées par les différents composants de GeoTrack.

Les indicateurs principaux sont :

- utilisation CPU ;
- utilisation mémoire ;
- espace disque utilisé et disponible ;
- disponibilité des services ;
- temps de réponse des services ;
- état des composants critiques.

## 3. Tableau de bord stockage

Ce tableau de bord permet de surveiller l'évolution du stockage des données de télémétrie.

Les informations principales sont :

- volume total de données stockées ;
- volume de nouvelles données ingérées ;
- espace de stockage disponible ;
- taux de croissance du stockage ;
- erreurs de lecture ou d'écriture ;
- état du système de stockage.

## 4. Tableau de bord des alertes techniques

Ce tableau de bord centralise les incidents détectés par les mécanismes de supervision.

Pour chaque alerte, les informations suivantes peuvent être affichées :

- type d'alerte ;
- composant concerné ;
- niveau de gravité ;
- heure de déclenchement ;
- valeur observée ;
- seuil configuré ;
- statut de l'alerte.

## 5. Niveaux de gravité

Les alertes peuvent être classées selon plusieurs niveaux :

- information ;
- avertissement ;
- critique.

Cette classification permet à l'équipe d'administration de prioriser les incidents nécessitant une intervention.

## 6. Visualisation avec Grafana

Grafana est utilisé pour regrouper les métriques collectées par Prometheus et les informations nécessaires à la supervision.

Les tableaux de bord doivent permettre :

- une lecture rapide de l'état général de GeoTrack ;
- l'observation de l'évolution des métriques ;
- l'identification des anomalies ;
- l'analyse d'un incident ;
- la consultation des alertes techniques.

## Résultat attendu

L'équipe d'administration dispose d'une vue centralisée permettant d'identifier rapidement une anomalie d'ingestion, une saturation des ressources, un problème de stockage ou une interruption d'un service GeoTrack.
