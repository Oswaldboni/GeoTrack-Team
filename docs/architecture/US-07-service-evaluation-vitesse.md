# US-07.2 — Service d'évaluation continue de la vitesse

## Objectif

Définir le fonctionnement du service GeoTrack chargé d'analyser en continu les messages de télémétrie afin de détecter les dépassements de vitesse.

## Entrées du service

Pour chaque message de télémétrie reçu, le service utilise notamment :

- `vehicle_id`
- vitesse mesurée ;
- latitude ;
- longitude ;
- horodatage ;
- type de route ou zone si disponible.

## Détermination de la vitesse limite

Le service détermine le seuil applicable selon l'ordre de priorité suivant :

1. seuil spécifique au véhicule ;
2. seuil associé au type de route ou à la zone ;
3. seuil par défaut du système.

## Logique d'évaluation

Pour chaque message reçu, le service compare :

`vitesse_mesuree`

avec :

`vitesse_limite`

Si :

`vitesse_mesuree > vitesse_limite`

alors un dépassement de vitesse est détecté.

Dans le cas contraire, aucun événement d'alerte n'est généré.

## Événement de dépassement

Lorsqu'un dépassement est détecté, le service prépare un événement contenant au minimum :

- identifiant du véhicule ;
- vitesse mesurée ;
- vitesse limite ;
- écart de vitesse ;
- latitude ;
- longitude ;
- horodatage.

## Traitement continu

Le service doit effectuer cette évaluation à chaque réception d'un nouveau message de télémétrie.

Le traitement suit le principe suivant :

1. réception d'un message de télémétrie ;
2. identification du véhicule ;
3. détermination du seuil applicable ;
4. comparaison entre vitesse réelle et vitesse limite ;
5. génération éventuelle d'un événement d'alerte ;
6. transmission de l'événement au mécanisme de notification.

## Pseudo-logique

```text
recevoir message de télémétrie
        |
        v
identifier le véhicule
        |
        v
déterminer le seuil applicable
        |
        v
vitesse_mesuree > vitesse_limite ?
        |
    oui | non
        | 
        v
générer événement d'alerte
        |
       non
        |
        v
ne générer aucun événement
```

## Réduction des alertes répétitives

Un véhicule peut envoyer plusieurs positions au-dessus de la limite pendant un même épisode. Le service crée une alerte à l'entrée dans l'état de dépassement, puis applique une période de silence ou attend le retour sous le seuil avant de créer une nouvelle alerte. La règle exacte doit être configurable.

Une petite marge de tolérance peut aussi être définie pour tenir compte des imprécisions de mesure. Cette marge est une décision métier et ne doit pas être ajoutée silencieusement.

## Ordre et idempotence

Le service ignore une télémétrie plus ancienne que la dernière position traitée pour le véhicule. L'identifiant de l'événement de dépassement permet d'éviter les doublons lors d'une retransmission.

## Performance et supervision

Le calcul doit être effectué au fil de l'eau et partitionné par `vehicle_id`. Les métriques suivent le débit traité, la latence d'évaluation, les erreurs, le nombre d'alertes et le retard du consommateur.

## Critères de validation

- Le seuil spécifique au véhicule est prioritaire sur les autres seuils.
- Une vitesse égale à la limite ne déclenche pas d'alerte.
- Un dépassement valide produit un événement complet.
- Des messages répétés pendant un même épisode ne créent pas une avalanche d'alertes.
- Une télémétrie plus ancienne ne modifie pas l'état courant.

## Conclusion

Le service évalue chaque message avec une règle de priorité explicite. La déduplication, l'ordre temporel et la gestion d'un épisode continu évitent des alertes incohérentes ou répétitives.
