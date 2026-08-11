# US-03.3 — Stratégie de buffering et de retry en cas de surcharge

## Objectif

Définir une stratégie permettant à GeoTrack de gérer les surcharges temporaires et les erreurs de traitement sans perdre les messages de télémétrie ni aggraver la saturation des services.

## 1. Buffering

Kafka est utilisé comme tampon entre les producteurs de messages et les services consommateurs.

Lorsque le débit entrant devient supérieur à la capacité instantanée de traitement, les messages restent temporairement disponibles dans le broker.

```text
Producteurs
    |
    v
+----------------+
|     Kafka      |
|    Buffer      |
+----------------+
    |
    v
Consommateurs
```

## 2. Politique de nouvelle tentative

Une erreur transitoire peut être retentée avec un délai croissant et une variation aléatoire afin d'éviter que tous les consommateurs recommencent simultanément.

Politique initiale proposée :

- maximum de 5 tentatives ;
- délais d'environ 1, 2, 4, 8 puis 16 secondes ;
- aucune nouvelle tentative automatique pour une erreur de validation permanente ;
- transfert dans une file de rejet après épuisement des tentatives.

Les valeurs devront être ajustées après les tests de charge.

## 3. Idempotence

Le consommateur doit pouvoir recevoir le même message plusieurs fois sans produire plusieurs événements métier. Un identifiant unique ou une clé formée de `vehicle_id`, de l'horodatage et d'un numéro de séquence permet de détecter les doublons.

## 4. Contre-pression

Lorsque le retard des consommateurs augmente, GeoTrack doit :

- augmenter le nombre de consommateurs dans les limites prévues ;
- ralentir ou refuser temporairement les producteurs non prioritaires ;
- préserver les messages déjà acceptés ;
- alerter l'équipe lorsque l'âge ou le volume du retard dépasse les seuils.

Le tampon n'est pas infini. Sa capacité et sa durée de rétention doivent être dimensionnées à partir du débit de pointe et du temps maximal de reprise.

## 5. Observabilité

Les métriques principales sont le nombre de messages en attente, l'âge du plus ancien message, le taux de tentatives, le nombre de messages en file de rejet, le débit producteur et le débit consommateur.

## Critères de validation

- Une panne temporaire d'un consommateur ne provoque pas la perte des messages acceptés.
- Un message invalide n'est pas retenté indéfiniment.
- Une retransmission ne produit pas de doublon métier.
- Une accumulation anormale déclenche une alerte.
- Le retour à la normale vide progressivement le retard sans saturer le stockage.

## Conclusion

Kafka fournit le tampon, mais la résilience dépend aussi de tentatives bornées, de l'idempotence, d'une file de rejet et de seuils de contre-pression mesurables.
