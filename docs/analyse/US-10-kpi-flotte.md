# US-10.1 — Indicateurs clés de performance de la flotte

## Objectif

Identifier et définir les KPI à afficher dans le tableau de bord GeoTrack afin de fournir aux gestionnaires une vue rapide et pertinente de l'état de la flotte.

Cette analyse sert de base à la conception de la maquette Figma du tableau de bord.

## KPI proposés

| KPI | Description | Calcul / source |
|---|---|---|
| Kilométrage total | Distance parcourue par véhicule ou par flotte sur une période | Somme des distances entre positions GPS successives |
| Vitesse moyenne | Vitesse moyenne d'un véhicule sur une période | Moyenne des vitesses instantanées enregistrées |
| Vitesse maximale | Pic de vitesse atteint sur une période | Maximum des vitesses instantanées |
| Nombre d'incidents | Nombre d'événements anormaux | Comptage des alertes ou incidents enregistrés |
| Temps d'activité | Temps pendant lequel le véhicule est en mouvement | Calcul à partir des positions GPS et de la vitesse |
| Temps d'inactivité | Temps pendant lequel le véhicule reste à l'arrêt | Calcul à partir des périodes où la vitesse est nulle |
| Franchissements de zone | Nombre d'entrées et sorties de zones de geofencing | Comptage des événements de US-06 |
| Taux de disponibilité de la flotte | Pourcentage de véhicules actifs ou correctement suivis | Véhicules avec données récentes / nombre total de véhicules |

## 1. Kilométrage total

Le kilométrage permet de mesurer l'utilisation réelle des véhicules sur une période.

Il peut être affiché :

- par véhicule ;
- par groupe de véhicules ;
- pour l'ensemble de la flotte.

Le calcul repose sur les positions GPS successives enregistrées dans l'historique.

## 2. Vitesse moyenne

La vitesse moyenne permet d'obtenir une vue synthétique du comportement d'un véhicule sur une période.

Elle peut être calculée à partir des vitesses instantanées disponibles dans les messages de télémétrie.

## 3. Vitesse maximale

La vitesse maximale permet d'identifier les pics de vitesse et de compléter l'analyse des alertes de dépassement.

Elle correspond à la valeur maximale observée sur la période analysée.

## 4. Nombre d'incidents

Les incidents peuvent inclure notamment :

- excès de vitesse ;
- franchissement de zone ;
- sortie de zone non autorisée ;
- arrêt prolongé ;
- autres alertes opérationnelles.

Le KPI correspond au nombre d'événements ou d'alertes enregistrés sur une période.

## 5. Temps d'activité et d'inactivité

Ces indicateurs permettent d'estimer la proportion du temps pendant laquelle un véhicule est en mouvement ou à l'arrêt.

Une approche initiale consiste à utiliser la vitesse :

```text
vitesse > 0  → véhicule actif
vitesse = 0  → véhicule à l'arrêt
```

Cette règle est seulement une première approximation. Pour réduire l'effet du bruit GPS, la version recommandée considère un véhicule actif au-dessus d'un seuil configurable, par exemple 5 km/h, pendant une durée minimale. Le seuil doit être validé par le métier.

## 6. Taux de disponibilité

Le taux est calculé ainsi :

```text
véhicules ayant une télémétrie récente / véhicules attendus × 100
```

La fenêtre définissant une donnée « récente » doit être indiquée dans le tableau de bord, par exemple deux intervalles d'émission plus une marge.

## 7. Franchissements de zone

Les entrées et sorties confirmées sont comptées séparément et peuvent être regroupées par véhicule, zone ou période. Les événements dédupliqués de US-06 constituent la source de référence.

## Qualité et unités

- Les distances sont calculées à partir de positions valides et ordonnées.
- Les données aberrantes ou manquantes sont signalées.
- Les unités sont affichées : km, km/h, minutes et pourcentage.
- Les périodes utilisent un fuseau horaire explicite.
- Les données de démonstration sont identifiées comme telles.

## Critères de validation

- Chaque KPI possède une définition, une formule, une unité et une source.
- Les mêmes filtres produisent les mêmes valeurs dans les graphiques et les exports.
- Une période sans données est distinguée d'une valeur égale à zéro.
- Le taux de disponibilité précise sa fenêtre de fraîcheur.

## Conclusion

Les KPI proposés couvrent l'utilisation, la vitesse, les incidents et la disponibilité. Leur valeur dépend de définitions stables et de règles de qualité communes à l'API, au tableau de bord et aux exports.
