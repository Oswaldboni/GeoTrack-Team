# US-09.2 — Politique de hiérarchisation des données

## Objectif

Définir une stratégie de hiérarchisation des données de télémétrie GeoTrack afin de concilier performances d'accès, conservation sur deux ans et maîtrise des coûts de stockage.

## Principe du Data Tiering

Toutes les données de télémétrie n'ont pas les mêmes besoins de performance.

Les données récentes sont davantage utilisées pour :

- le suivi opérationnel ;
- l'affichage des positions ;
- les alertes ;
- l'analyse des trajets récents ;
- les tableaux de bord.

Les données plus anciennes sont principalement utilisées pour :

- la consultation de l'historique ;
- les analyses à long terme ;
- les rapports ;
- les besoins d'audit ou de traçabilité.

GeoTrack peut donc répartir les données entre plusieurs niveaux de stockage.

## 1. Données chaudes — Hot Tier

Période proposée :

**0 à 30 jours**

Ces données sont fréquemment consultées et doivent bénéficier d'un accès rapide.

Elles sont utilisées notamment pour :

- les opérations quotidiennes ;
- les trajets récents ;
- les alertes ;
- les analyses opérationnelles ;
- les tableaux de bord.

Le stockage utilisé pour cette catégorie privilégie les performances.

## 2. Données tièdes — Warm Tier

Période proposée :

**31 à 180 jours**

Ces données sont moins fréquemment consultées mais doivent rester accessibles sans procédure d'archivage complexe.

Ce niveau constitue un compromis entre :

- performances ;
- disponibilité ;
- coût de stockage.

## 3. Données froides — Cold Tier

Période proposée :

**181 jours à 2 ans**

Ces données sont rarement consultées mais doivent être conservées afin de respecter la politique de rétention de GeoTrack.

Le stockage froid privilégie :

- un coût réduit ;
- une capacité importante ;
- la conservation à long terme.

Un temps de récupération plus élevé peut être acceptable pour ces données.

## Cycle de vie proposé

```text
Création du message
        |
        v
   Hot Tier
   0 à 30 jours
        |
        v
   Warm Tier
   31 à 180 jours
        |
        v
   Cold Tier
   181 jours à 2 ans
        |
        v
Fin de la période de rétention
        |
        v
Suppression contrôlée ou prolongation autorisée
```

## Règles de transition

Les transitions sont exécutées automatiquement par une politique de cycle de vie. Chaque transfert doit être journalisé, vérifié et relançable. Une donnée ne doit être supprimée du niveau source qu'après confirmation de son intégrité et de sa disponibilité dans le niveau cible.

## Niveaux de service proposés

| Niveau | Délai d'accès visé | Usage principal |
|---|---|---|
| Hot | Secondes | Opérations et trajets récents |
| Warm | Secondes à minutes | Analyses historiques courantes |
| Cold | Minutes à heures | Audit et recherche rare |

Ces délais sont des objectifs de conception et doivent être validés avec la technologie choisie.

## Index et copies

Les index du niveau chaud peuvent être plus nombreux que ceux du niveau froid. Le coût des répliques, sauvegardes et index doit être compté séparément du volume brut. La réplication améliore la disponibilité, tandis que la sauvegarde protège contre la corruption et l'erreur humaine ; l'une ne remplace pas l'autre.

## Fin de rétention

Après deux ans, la suppression doit être contrôlée, traçable et conforme aux obligations validées par l'équipe. Un gel juridique, une enquête ou une règle métier peut prolonger la conservation d'un sous-ensemble précis.

## Critères de validation

- Une donnée change de niveau selon son âge sans perte d'intégrité.
- Une requête indique clairement si une restauration du niveau froid est nécessaire.
- Les comptes et sommes de contrôle sont vérifiés après transfert.
- La suppression après deux ans est journalisée et soumise à la politique approuvée.

## Conclusion

La hiérarchisation proposée concilie accès rapide aux données récentes et réduction du coût des données anciennes. Les périodes retenues restent des paramètres configurables à valider par les tests et les besoins métier.
