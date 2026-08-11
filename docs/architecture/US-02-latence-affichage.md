# US-02.3 — Gestion de la latence d'affichage

## Objectif

Définir les mécanismes permettant à GeoTrack de maintenir une latence d'affichage compatible avec l'exigence de visualisation des positions en moins de quelques secondes.

## 1. Définition de la latence

La latence d'affichage correspond au délai entre la production d'une nouvelle position par un véhicule et sa disponibilité pour l'affichage dans l'interface GeoTrack.

Le délai de bout en bout peut être représenté ainsi :

```text
Véhicule
   |
   v
Transmission
   |
   v
Ingestion
   |
   v
Traitement
   |
   v
Diffusion temps réel
   |
   v
WebSocket
   |
   v
Interface utilisateur
   |
   v
Mise à jour de la carte
```

## 2. Budget de latence proposé

L'intervalle d'émission des véhicules est de 5 secondes. Il faut donc distinguer l'âge de la position et le temps de traitement après réception.

| Segment | Cible de conception au percentile 95 |
|---|---:|
| Ingestion et validation | 300 ms |
| File et traitement | 700 ms |
| Diffusion WebSocket | 500 ms |
| Mise à jour de l'interface | 500 ms |
| Total après réception | 2 s |

La cible proposée est une latence de traitement de bout en bout inférieure ou égale à 2 secondes au percentile 95 sous charge nominale. L'âge total d'une position peut approcher 7 secondes dans le pire cas courant : jusqu'à 5 secondes avant l'émission suivante, puis jusqu'à 2 secondes de traitement.

## 3. Mécanismes de réduction

- traitement asynchrone après validation ;
- partitionnement par `vehicle_id` ;
- diffusion des deltas plutôt que d'instantanés complets ;
- regroupement de mises à jour sur une courte fenêtre ;
- limitation du rendu aux véhicules visibles ;
- remplacement d'une position en attente par une position plus récente du même véhicule.

## 4. Mesure

Chaque message conserve son horodatage d'émission. Les composants ajoutent des horodatages de réception, de traitement et de diffusion. Le navigateur mesure enfin l'heure d'affichage. Les tableaux de bord suivent les percentiles 50, 95 et 99, pas seulement la moyenne.

## 5. Comportement en dégradation

Lorsque la cible n'est plus respectée, l'interface affiche l'âge de la dernière position. Le système privilégie la donnée la plus récente et peut abandonner des mises à jour d'affichage intermédiaires, sans supprimer la télémétrie persistée.

## Critères de validation

- Le percentile 95 après réception reste inférieur ou égal à 2 secondes au débit nominal.
- L'âge de la position est visible lorsqu'il dépasse le seuil accepté.
- Une position périmée ne remplace pas une position récente.
- La mesure distingue le temps réseau, le traitement et le rendu.

## Conclusion

La latence doit être mesurée de bout en bout avec des percentiles. La cible proposée tient compte de l'émission toutes les 5 secondes et évite de confondre fréquence de production et délai de traitement.
