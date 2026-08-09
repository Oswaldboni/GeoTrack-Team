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
