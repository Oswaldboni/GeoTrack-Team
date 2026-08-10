# US-10.3 — Reporting et export des données

## Objectif

Définir l'intégration des graphiques de reporting et de la fonctionnalité d'export des données dans le tableau de bord analytique GeoTrack.

Cette conception s'appuie sur les KPI définis dans GTB-77 et sur la maquette du tableau de bord réalisée dans GTB-78.

## Graphiques de reporting

Le tableau de bord doit permettre de représenter les principaux KPI de la flotte sous différentes formes visuelles.

Les représentations prévues comprennent :

- cartes de chiffres-clés pour les KPI principaux ;
- graphiques en ligne pour l'évolution du kilométrage et de la vitesse ;
- graphiques en barres pour les incidents et franchissements de zones ;
- listes synthétiques pour les événements et alertes récentes.

## Connexion aux données

Les graphiques doivent être alimentés à partir des données fournies par l'API ou les services backend de GeoTrack.

Le flux général est :

```text
Données de télémétrie
        |
        v
Backend / calcul des KPI
        |
        v
API
        |
        v
Tableau de bord
        |
        v
Graphiques et indicateurs
