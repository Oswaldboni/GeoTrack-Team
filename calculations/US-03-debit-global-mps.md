# US-03.1 — Dimensionnement du débit global requis

## Objectif

Calculer le débit nominal de messages de télémétrie que GeoTrack doit être capable de recevoir et traiter en continu.

## Données de départ

Le système GeoTrack doit gérer :

- 10 000 véhicules ;
- un message de télémétrie toutes les 5 secondes par véhicule ;
- un fonctionnement 24 h/24 et 7 j/7.

## Calcul du débit nominal

Le débit nominal est calculé avec la formule :

Débit = nombre de véhicules / intervalle d'émission

Donc :

10 000 / 5 = **2 000 messages par seconde**

Le débit nominal attendu est donc :

**2 000 MPS**

où MPS signifie Messages Per Second.

## Volumes dérivés

### Par minute

2 000 × 60 = **120 000 messages**

### Par heure

120 000 × 60 = **7 200 000 messages**

### Par jour

7 200 000 × 24 = **172 800 000 messages**

## Interprétation

Le débit de 2 000 MPS correspond au débit nominal théorique lorsque les messages sont répartis régulièrement dans le temps.

Dans un environnement réel, le trafic peut être moins régulier.

Des pointes peuvent apparaître notamment lors de :

- reconnexions simultanées de plusieurs véhicules ;
- retards réseau suivis d'une reprise ;
- retransmissions ;
- accumulation temporaire de messages ;
- variation du comportement des équipements.

## Débit nominal et débit de pointe

Le débit nominal constitue la base de dimensionnement.

Le débit de pointe doit être traité séparément avec une hypothèse explicite et justifiée.

Par exemple, un facteur de pointe pourra être appliqué lors des scénarios de charge afin de vérifier la capacité de l'architecture à absorber une hausse temporaire du trafic.

La valeur de ce facteur ne doit pas être considérée comme une exigence du sujet tant qu'elle n'a pas été définie et justifiée par l'équipe.

## Composants concernés

Le dimensionnement du débit influence directement :

- le point d'entrée ;
- le service d'ingestion ;
- le broker ou la file de messages ;
- les services de traitement ;
- le stockage ;
- les mécanismes de supervision.

## Résultat attendu

L'architecture GeoTrack doit supporter au minimum un débit nominal de **2 000 messages par seconde** en continu.

Les scénarios de charge devront ensuite vérifier la capacité à absorber des pointes supérieures sans perte de messages ni dégradation excessive du service.
