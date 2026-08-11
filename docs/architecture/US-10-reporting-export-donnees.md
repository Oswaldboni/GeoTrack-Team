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
```

## Filtres et cohérence

La période, le véhicule et la zone sont transmis à l'API avec un fuseau horaire explicite. Tous les KPI et graphiques d'une même vue doivent utiliser exactement les mêmes filtres. L'interface affiche l'heure de la dernière mise à jour et l'unité de chaque mesure.

## Export

L'utilisateur peut demander un export CSV des données tabulaires filtrées. Un export PDF peut être proposé pour une vue de synthèse. Pour un volume important, l'export est préparé de manière asynchrone afin de ne pas bloquer l'interface.

Le fichier d'export doit inclure :

- la période et le fuseau horaire ;
- les filtres appliqués ;
- la date de génération ;
- les unités ;
- une définition courte des colonnes ;
- un identifiant de rapport.

## Sécurité et traçabilité

Les mêmes règles RBAC que pour l'écran sont appliquées à l'export. Le serveur recalcule les droits et ne se fie pas aux filtres fournis par le navigateur. La création, le téléchargement et l'expiration d'un export sensible sont journalisés.

## Gestion des erreurs

Une absence de données produit un état vide explicite, pas un graphique trompeur. Une erreur partielle est signalée et le dernier résultat connu ne doit pas être présenté comme actuel sans avertissement.

## Critères de validation

- Les cartes, graphiques et exports utilisent les mêmes filtres.
- Un utilisateur ne peut exporter que les véhicules qu'il peut consulter.
- Le CSV s'ouvre correctement et contient les unités et métadonnées.
- Une demande volumineuse n'immobilise pas le tableau de bord.
- L'état vide et l'échec de chargement sont clairement distingués.

## Conclusion

Le reporting repose sur des KPI calculés côté serveur et sur des filtres cohérents. L'export est traçable, sécurisé et adapté au volume demandé.
