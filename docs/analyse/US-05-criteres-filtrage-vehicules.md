# US-05 — Critères de filtrage des véhicules

## Sous-tâche associée

**GTB-93 — Définir les critères de filtrage des véhicules**

## Objectif

Définir précisément les critères de filtrage disponibles dans l’interface de cartographie et de gestion de flotte GeoTrack.

Ces filtres doivent permettre à un gestionnaire de retrouver rapidement un ou plusieurs véhicules selon différents attributs et de réduire le nombre de véhicules affichés sur la carte.

## Contexte

Cette définition sert de base à la conception et à l’implémentation du composant de filtrage associé aux US-04 et US-05.

Le mécanisme doit couvrir les besoins les plus courants d’un gestionnaire de flotte tout en restant compatible avec les données disponibles dans GeoTrack.

## Critères de filtrage retenus

| Filtre | Type | Description |
|---|---|---|
| Zone géographique | Sélection | Afficher uniquement les véhicules présents dans une zone géographique ou une zone de geofencing donnée |
| Statut | Actif / Inactif | Filtrer les véhicules selon leur état d’activité |
| Identifiant du véhicule | Recherche texte | Rechercher directement un véhicule à partir de sa plaque, de son numéro interne ou de son nom |
| Type de véhicule | Sélection | Filtrer les véhicules selon leur catégorie lorsque cette information est disponible |
| Conducteur assigné | Sélection | Filtrer les véhicules selon le conducteur ou la personne responsable lorsque cette information est disponible |

## Détail des filtres

### 1. Zone géographique

Le filtre par zone géographique permet au gestionnaire de sélectionner une zone prédéfinie.

Seuls les véhicules dont la dernière position connue se situe à l’intérieur de cette zone sont affichés.

Exemples :

- secteur nord ;
- secteur sud ;
- dépôt principal ;
- zone de livraison ;
- zone de geofencing personnalisée.

Ce filtre repose principalement sur les coordonnées géographiques du véhicule.

## 2. Statut

Le filtre par statut permet de distinguer principalement les véhicules actifs et inactifs.

### Actif

Un véhicule peut être considéré comme actif lorsqu’il :

- est actuellement en mouvement ;
- transmet régulièrement des données ;
- ou a transmis une nouvelle position récemment.

### Inactif

Un véhicule peut être considéré comme inactif lorsqu’il :

- est à l’arrêt depuis une période déterminée ;
- ne transmet plus de données depuis un certain délai ;
- ou est considéré comme hors ligne.

La définition technique exacte du délai permettant de passer d’un état actif à inactif pourra être configurée par le système.

## 3. Identifiant du véhicule

Une recherche textuelle permet de retrouver directement un véhicule.

La recherche peut porter sur :

- la plaque d’immatriculation ;
- le numéro interne du véhicule ;
- le nom ou libellé du véhicule.

Exemple :

```text
VH-00421
