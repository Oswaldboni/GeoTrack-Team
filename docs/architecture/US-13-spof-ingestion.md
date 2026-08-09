# US-13.1 — Analyse des points de défaillance uniques de l'ingestion

## Objectif

Identifier les principaux Single Points of Failure (SPOF) de l'architecture d'ingestion GeoTrack et définir les mécanismes permettant de réduire leur impact sur la disponibilité du système.

## Contexte

GeoTrack reçoit en continu les données de télémétrie d'environ 10 000 véhicules.

Chaque véhicule transmet régulièrement ses informations de position et d'état.

L'architecture d'ingestion doit donc rester disponible même lorsqu'un composant individuel devient indisponible.

## Tableau des principaux SPOF

| Composant | Risque | Impact | Criticité | Mesure de mitigation |
|---|---|---|---|---|
| Point d'entrée unique | Panne du seul point d'accès | Interruption complète de l'ingestion | Critique | Répartition de charge entre plusieurs instances |
| Service d'ingestion unique | Arrêt de l'instance | Messages non traités | Critique | Plusieurs instances du service d'ingestion |
| Broker de messages unique | Panne du broker | Blocage ou perte temporaire du flux | Critique | Réplication du broker et mécanisme de basculement |
| Base de données unique | Indisponibilité du stockage | Impossible d'enregistrer la télémétrie | Critique | Réplication et basculement du stockage |
| Nœud de traitement unique | Défaillance matérielle ou logicielle | Interruption du traitement | Élevée | Déploiement sur plusieurs nœuds |
| Réseau unique | Rupture de connectivité | Perte temporaire des communications | Élevée | Redondance réseau et mécanisme de reprise |
| Système de supervision unique | Panne de la supervision | Incidents non détectés rapidement | Moyenne | Supervision redondante et alertes externes |

## 1. Point d'entrée unique

Un seul point d'entrée pour tous les messages de télémétrie constitue un risque important.

Sa défaillance peut empêcher tous les véhicules de transmettre leurs données.

### Mitigation

Mettre en place un mécanisme de répartition de charge entre plusieurs instances disponibles.

## 2. Service d'ingestion unique

Une seule instance du service d'ingestion constitue également un SPOF.

### Mitigation

Déployer plusieurs instances du service afin que la perte d'une instance ne provoque pas l'arrêt complet de l'ingestion.

## 3. Broker ou file de messages

Si l'architecture utilise un broker unique sans réplication, sa panne peut interrompre le flux entre l'ingestion et les services consommateurs.

### Mitigation

Utiliser un mécanisme de réplication, de persistance et de basculement automatique.

## 4. Stockage

Une base de données unique peut interrompre l'enregistrement des données lorsqu'elle devient indisponible.

### Mitigation

Prévoir :

- plusieurs répliques ;
- un mécanisme de basculement ;
- des sauvegardes ;
- une surveillance de l'état du stockage.

## 5. Nœuds de traitement

Les services critiques ne doivent pas dépendre d'un seul serveur ou d'une seule machine.

### Mitigation

Répartir les services sur plusieurs nœuds et permettre leur redémarrage ou remplacement automatique.

## 6. Supervision et reprise

Les mécanismes de supervision doivent détecter rapidement :

- la perte d'une instance ;
- l'augmentation du taux d'erreur ;
- une baisse du débit de messages ;
- une augmentation anormale de la latence ;
- l'indisponibilité d'un composant critique.

La plateforme doit pouvoir déclencher une procédure de reprise ou un basculement lorsqu'une défaillance est détectée.

## Principe de résilience

L'objectif principal est d'éviter qu'une défaillance unique entraîne l'arrêt complet du système.

L'architecture doit donc privilégier :

- la redondance ;
- la réplication ;
- la répartition de charge ;
- le basculement automatique ;
- la supervision ;
- les procédures de reprise.

## Résultat attendu

L'architecture d'ingestion GeoTrack doit continuer à fonctionner lorsqu'une instance individuelle devient indisponible, en s'appuyant sur des composants redondants et des mécanismes de reprise adaptés.
