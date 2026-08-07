# US-15.3 — Seuils des alertes techniques

## Objectif

Définir les seuils de supervision permettant à GeoTrack de détecter automatiquement les anomalies techniques et d'alerter l'équipe d'administration.

## 1. Surveillance de l'ingestion

Le pipeline d'ingestion constitue un composant critique de GeoTrack.

Une alerte doit pouvoir être déclenchée lorsque :

- le débit de messages diminue anormalement ;
- le nombre de messages rejetés augmente ;
- le taux d'erreur d'ingestion augmente ;
- la latence de traitement devient anormalement élevée ;
- aucun message n'est reçu alors que des véhicules sont censés transmettre leur télémétrie.

Les seuils définitifs devront être ajustés selon les performances observées en exploitation.

## 2. Utilisation CPU

Seuils initiaux proposés :

- inférieur à 80 % : fonctionnement normal ;
- supérieur ou égal à 80 % pendant une période prolongée : avertissement ;
- supérieur ou égal à 90 % pendant une période prolongée : critique.

L'utilisation d'une durée minimale permet d'éviter de générer une alerte pour un simple pic temporaire.

## 3. Utilisation mémoire

Seuils initiaux proposés :

- inférieur à 80 % : fonctionnement normal ;
- supérieur ou égal à 80 % : avertissement ;
- supérieur ou égal à 90 % : critique.

Une consommation mémoire durablement élevée peut indiquer une saturation ou un problème applicatif.

## 4. Capacité de stockage

La supervision doit également surveiller l'espace de stockage disponible.

Seuils proposés :

- plus de 20 % d'espace disponible : fonctionnement normal ;
- moins de 20 % d'espace disponible : avertissement ;
- moins de 10 % d'espace disponible : critique.

Cette surveillance est particulièrement importante en raison du volume élevé de données de télémétrie conservées par GeoTrack.

## 5. Disponibilité des services

Les services critiques doivent faire l'objet d'une surveillance continue.

L'indisponibilité confirmée d'un composant critique doit entraîner une alerte critique.

Les composants concernés peuvent notamment inclure :

- le service d'ingestion ;
- le service de traitement de la télémétrie ;
- le stockage ;
- les services nécessaires au tableau de bord ;
- les composants de supervision.

## 6. Taux d'erreur

Une augmentation inhabituelle du nombre d'erreurs ou de messages rejetés doit déclencher une alerte.

Le seuil exact doit être déterminé en fonction du comportement normal observé du système.

Cette approche évite de définir arbitrairement une valeur qui ne correspondrait pas aux conditions réelles d'exploitation.

## 7. Niveaux de gravité

Les alertes techniques sont classées selon trois niveaux principaux.

### Information

Événement utile à la supervision mais ne nécessitant pas nécessairement une intervention immédiate.

### Avertissement

Dégradation pouvant évoluer vers un incident si aucune action n'est entreprise.

### Critique

Incident ou risque important nécessitant une intervention rapide de l'équipe d'administration.

## 8. Synthèse des seuils initiaux

| Indicateur | Avertissement | Critique |
|---|---|---|
| CPU | ≥ 80 % de manière prolongée | ≥ 90 % de manière prolongée |
| Mémoire | ≥ 80 % | ≥ 90 % |
| Espace disponible | < 20 % | < 10 % |
| Service critique | Dégradation détectée | Indisponibilité confirmée |
| Ingestion | Dégradation anormale | Interruption ou anomalie majeure |
| Taux d'erreur | Hausse inhabituelle | Niveau compromettant le service |

## 9. Ajustement des seuils

Ces valeurs constituent des seuils initiaux de conception.

Elles devront être ajustées à partir :

- des métriques réellement observées ;
- des performances normales de GeoTrack ;
- des tests de charge ;
- des objectifs de disponibilité ;
- des retours d'exploitation.

Cette adaptation permet de réduire les fausses alertes tout en conservant une détection suffisamment rapide des incidents.

## Résultat attendu

L'équipe d'administration doit être alertée lorsqu'une métrique sort durablement de sa plage normale afin de pouvoir identifier et traiter une anomalie avant qu'elle n'affecte fortement la disponibilité ou les performances de GeoTrack.
