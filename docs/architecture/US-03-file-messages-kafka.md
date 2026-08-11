# US-03.2 — File de messages pour l'absorption des pics de trafic

## Objectif

Définir le mécanisme de messagerie permettant à GeoTrack d'absorber les variations et les pics temporaires du trafic de télémétrie sans coupler directement l'ingestion aux services de traitement.

## 1. Contexte

GeoTrack reçoit nominalement :

- 10 000 véhicules ;
- un message toutes les 5 secondes par véhicule ;
- soit environ 2 000 messages par seconde.

Ce débit représente une moyenne nominale.

Des pointes temporaires peuvent apparaître lors de reconnexions simultanées, de retransmissions ou de reprises après une perturbation réseau.

## 2. Problématique

Sans file de messages, le flux peut être directement dépendant de la capacité des services consommateurs :

```text
Véhicules
    |
    v
Ingestion
    |
    v
Traitement
```

Cette liaison directe propage la panne ou le ralentissement d'un consommateur jusqu'au service d'ingestion.

## 3. Solution retenue

Kafka est retenu comme broker de messages entre l'ingestion et les traitements asynchrones.

```text
Véhicules → ingestion → topic Kafka → groupes de consommateurs → stockage et alertes
```

Le service d'ingestion publie rapidement le message validé. Les consommateurs traitent ensuite la télémétrie à leur rythme tout en partageant la charge.

## 4. Organisation proposée

- Topic principal : `telemetry.raw`.
- Clé de partition : `vehicle_id` pour conserver l'ordre par véhicule.
- Plusieurs partitions : à dimensionner par test de charge.
- Facteur de réplication : 3 lorsque trois brokers sont disponibles.
- Accusé de réception du producteur : confirmation par les répliques requises.
- File de rejet : `telemetry.dead-letter` pour les messages non traitables.

La durée de rétention du topic doit couvrir la durée maximale de panne que l'équipe souhaite absorber. Elle ne remplace pas la conservation métier de deux ans dans le stockage historique.

## 5. Consommateurs

Chaque fonction utilise un groupe de consommateurs distinct, par exemple le stockage, les alertes de vitesse, le geofencing et l'observabilité. Plusieurs instances d'un même groupe partagent les partitions et peuvent être ajoutées lorsque le retard augmente.

## 6. Garanties et limites

La livraison est conçue au moins une fois. Les consommateurs doivent donc être idempotents. Kafka améliore la résilience, mais ne supprime pas le besoin de superviser les partitions, la réplication, le retard et l'espace disque.

## Critères de validation

- Une interruption temporaire d'un consommateur n'empêche pas l'ingestion.
- Les messages d'un véhicule sont lus dans leur ordre de partition.
- Une panne d'un broker ne rend pas le topic indisponible lorsque les répliques sont saines.
- Le retard des consommateurs est mesuré et déclenche une alerte.

## Conclusion

Kafka découple l'ingestion des traitements et absorbe les pointes temporaires. Le partitionnement par véhicule, la réplication et l'idempotence rendent cette décision cohérente avec les besoins de volume et de disponibilité de GeoTrack.
