# US-07.3 — Notification d'une alerte de vitesse

## Objectif

Définir le scénario de notification d'un dépassement de vitesse vers le tableau de bord du gestionnaire de flotte GeoTrack.

## Déclenchement de l'alerte

Lorsqu'un dépassement de vitesse est détecté par le service d'évaluation, un événement d'alerte est généré automatiquement.

Cet événement est transmis au mécanisme de notification du système.

## Contenu de l'alerte

L'alerte doit contenir au minimum :

- l'identifiant du véhicule ;
- la vitesse mesurée ;
- la vitesse limite applicable ;
- l'écart constaté ;
- la latitude ;
- la longitude ;
- l'horodatage ;
- le niveau de gravité si applicable.

## Scénario de notification

1. Le service d'évaluation détecte un dépassement.
2. Un événement d'alerte est généré.
3. L'événement est transmis au service de notification.
4. Le service de notification prépare le message destiné au tableau de bord.
5. Le tableau de bord reçoit l'alerte.
6. L'alerte est affichée de manière visible au gestionnaire de flotte.
7. L'événement est conservé dans l'historique des alertes.

## Affichage dans le tableau de bord

Le gestionnaire doit pouvoir identifier rapidement :

- le véhicule concerné ;
- la vitesse constatée ;
- la vitesse limite ;
- la position du véhicule ;
- l'heure du dépassement.

L'interface peut également utiliser un niveau de priorité afin de distinguer les dépassements importants des dépassements mineurs.

## Traçabilité

Chaque alerte doit être conservée afin de permettre :

- la consultation de l'historique ;
- l'analyse des comportements de conduite ;
- la production de rapports ;
- le suivi des incidents.

## Résultat attendu

Lorsqu'un dépassement de vitesse est détecté, le gestionnaire de flotte reçoit rapidement une alerte exploitable dans le tableau de bord GeoTrack, avec suffisamment d'informations pour identifier le véhicule et comprendre l'événement.
