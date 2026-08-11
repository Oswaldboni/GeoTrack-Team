# US-03.4 — Tolérance aux pannes lors des pics d'ingestion

## Objectif

Définir les mécanismes permettant à GeoTrack de continuer à accepter et traiter la télémétrie lorsqu'une panne survient pendant une période de forte charge.

## 1. Contexte

GeoTrack doit supporter un débit nominal d'environ :

**2 000 messages par seconde**

Ce débit peut temporairement augmenter lors :

- de reconnexions simultanées ;
- de reprises après une interruption réseau ;
- de retransmissions ;
- d'accumulations temporaires de télémétrie.

Une panne survenant pendant un pic peut réduire la capacité disponible au moment où le système en a le plus besoin.

L'architecture doit donc combiner scalabilité et tolérance aux pannes.

## 2. Principe général

La stratégie repose sur plusieurs niveaux de protection :

```text
Véhicules
    |
    v
Répartition de charge
    |
    v
+--------------------------+
| Instances d'ingestion    |
| I1     I2     I3         |
+--------------------------+
    |
    v
+--------------------------+
| Kafka                    |
| brokers + réplication    |
+--------------------------+
    |
    v
+--------------------------+
| Consumer group           |
| C1     C2     C3         |
+--------------------------+
    |
    v
Traitement / stockage
```

## 3. Comportement en cas de panne

| Panne | Réaction attendue | Risque résiduel |
|---|---|---|
| Une instance d'ingestion | Retrait du répartiteur et redirection | Capacité réduite |
| Un broker Kafka | Élection ou utilisation d'une réplique | Brève augmentation de latence |
| Un consommateur | Réaffectation de ses partitions | Accumulation temporaire |
| Le stockage | Conservation temporaire dans Kafka | Saturation si la panne dure trop longtemps |
| Le réseau d'un véhicule | Retransmission contrôlée après reconnexion | Doublons possibles, traités par idempotence |

## 4. Dimensionnement de la marge

Le débit nominal est de 2 000 messages par seconde. Le test de pointe doit vérifier au minimum un facteur proposé de 2, soit 4 000 messages par seconde pendant une période définie par l'équipe. Ce facteur est une hypothèse de test, pas une exigence confirmée du sujet.

La plateforme doit conserver une capacité suffisante après la perte d'une instance. Il est donc incorrect de dimensionner l'ensemble des instances exactement au débit nominal sans réserve.

## 5. Garanties de traitement

- Les messages sont persistés dans le broker avant leur acquittement définitif.
- Les consommateurs sont idempotents.
- Les tentatives sont bornées et les échecs permanents sont isolés.
- Les horodatages et identifiants de corrélation permettent de suivre un message.
- Le retard du broker et l'âge du plus ancien message sont supervisés.

## 6. Critères de validation

- La perte d'une instance d'ingestion n'arrête pas le flux complet.
- Un pic à 4 000 messages par seconde est absorbé sans perte lors du scénario de test convenu.
- Après le retour d'un composant, le retard est résorbé automatiquement.
- Une panne prolongée déclenche une alerte avant l'épuisement du stockage du broker.
- Aucun doublon métier n'est créé après retransmission.

## Conclusion

La tolérance aux pannes repose sur la redondance de chaque niveau, un broker répliqué et des traitements idempotents. La capacité résiduelle et la durée de rétention doivent être prouvées par des tests de panne et de charge combinés.
