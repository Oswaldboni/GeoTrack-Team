# US-01.2 — Spécification technique du protocole d'ingestion

## Objectif

Définir le mécanisme permettant à GeoTrack de recevoir en continu les messages de télémétrie transmis par les véhicules de la flotte.

## Charge attendue

GeoTrack doit gérer :

- 10 000 véhicules ;
- un message toutes les 5 secondes par véhicule ;
- un fonctionnement 24 h/24 et 7 j/7.

Le débit théorique est donc :

10 000 / 5 = **2 000 messages par seconde**

Le mécanisme d'ingestion doit être dimensionné pour supporter au minimum cette charge moyenne, avec une marge pour les pointes temporaires.

## Format des messages

Chaque message reçu doit respecter le schéma JSON défini dans US-01.1.

Les données principales comprennent notamment :

- identifiant du véhicule ;
- coordonnées GPS ;
- vitesse ;
- direction ;
- horodatage ;
- état du véhicule ;
- informations de diagnostic éventuelles.

## Flux d'ingestion proposé

Le traitement d'un message suit les étapes suivantes :

1. réception du message ;
2. validation du format JSON ;
3. vérification des champs obligatoires ;
4. contrôle des valeurs principales ;
5. rejet et journalisation si le message est invalide ;
6. acceptation du message s'il est valide ;
7. transmission vers le pipeline de traitement ;
8. stockage ou publication vers les composants consommateurs.

## Architecture logique

```text
Véhicule
   |
   v
Service d'ingestion
   |
   +--> Validation JSON
   |
   +--> Vérification des données
   |
   +--> Journalisation des erreurs
   |
   v
Pipeline de traitement
   |
   +--> Stockage
   |
   +--> Services temps réel
   |
   +--> Alertes et tableaux de bord
```

## Réponse du service

Le service retourne un résultat explicite :

- `202 Accepted` lorsque le message valide est pris en charge de manière asynchrone ;
- `400 Bad Request` lorsque le JSON ou les champs sont invalides ;
- `401 Unauthorized` ou `403 Forbidden` lorsque l'émetteur n'est pas autorisé ;
- `429 Too Many Requests` lorsque la limite d'admission est dépassée ;
- `503 Service Unavailable` lorsque la plateforme ne peut temporairement plus accepter le flux.

Chaque erreur doit inclure un code technique stable, un message compréhensible et un identifiant de corrélation, sans exposer de renseignement interne sensible.

## Fiabilité

- Le message validé est publié dans une file persistante avant le traitement métier.
- Un identifiant de message ou une clé d'idempotence empêche la création de doublons lors d'une retransmission.
- Les tentatives sont limitées et espacées par un délai croissant.
- Les messages durablement invalides sont isolés dans une file de rejet pour analyse.
- L'ordre est garanti au minimum pour les messages d'un même véhicule grâce à une clé de partition basée sur `vehicle_id`.

## Sécurité

Les communications doivent être chiffrées par TLS. L'identité de l'émetteur doit être vérifiée et les droits limités à l'envoi de télémétrie. Les secrets et certificats ne doivent jamais être intégrés au code ou au message.

## Critères de validation

- Le service accepte un message conforme au schéma JSON.
- Il rejette un message incomplet ou hors limites sans le transmettre au pipeline.
- Il supporte au moins 2 000 messages par seconde au débit nominal lors d'un test de charge.
- Une retransmission ne crée pas de doublon logique.
- Les erreurs et métriques sont observables avec un identifiant de corrélation.

## Conclusion

Le protocole retenu sépare l'admission rapide des messages de leur traitement. La validation, la file persistante, l'idempotence et la supervision permettent d'absorber la charge nominale tout en limitant les pertes et les doublons.
