# US-05 — Conception UI/UX des filtres de véhicules

## Sous-tâche associée

**GTB-94 — Concevoir l’ergonomie (UI/UX) des filtres sur la maquette de la carte interactive**

## Objectif

Concevoir l’expérience utilisateur et la disposition visuelle des filtres définis dans GTB-93 afin qu’ils puissent être utilisés directement depuis la carte interactive GeoTrack.

La conception doit permettre au gestionnaire de filtrer rapidement les véhicules sans quitter la vue cartographique et sans masquer inutilement les informations importantes de la carte.

## Contexte

Cette sous-tâche s’appuie sur les critères de filtrage définis dans GTB-93.

Les filtres principaux sont :

- zone géographique ;
- statut actif ou inactif ;
- identifiant du véhicule.

Des filtres complémentaires pourront également être représentés lorsque les données sont disponibles :

- type de véhicule ;
- conducteur assigné.

Cette sous-tâche concerne uniquement la conception de l’interface et de l’expérience utilisateur.

L’implémentation technique du filtrage n’est pas couverte ici.

## Proposition d’ergonomie générale

Le mécanisme retenu repose sur un **panneau de filtres latéral rétractable** accessible directement depuis la carte.

Cette approche permet :

- de conserver une grande surface disponible pour la carte ;
- d’accéder rapidement aux critères de filtrage ;
- de masquer le panneau lorsqu’il n’est pas utilisé ;
- de conserver les filtres actifs pendant la consultation de la carte.

## État par défaut

Lorsque l’utilisateur ouvre la carte :

- tous les véhicules autorisés sont affichés ;
- aucun filtre n’est actif ;
- le panneau de filtrage peut être fermé par défaut ;
- un bouton ou une icône **Filtres** permet d’ouvrir le panneau.

Exemple conceptuel :

```text
+----------------------------------------------------------+
| GeoTrack                         [Filtres] [Recherche]    |
+----------------------------------------------------------+
|                                                          |
|                                                          |
|                    CARTE INTERACTIVE                     |
|                                                          |
|            • véhicule         • véhicule                 |
|                                                          |
|                         • véhicule                       |
|                                                          |
+----------------------------------------------------------+
