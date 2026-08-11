# US-02.2 — Flux de données entre télémétrie et interface utilisateur

## Objectif

Définir le flux de données permettant à GeoTrack d'acheminer efficacement les nouvelles positions des véhicules vers l'interface utilisateur afin de maintenir un affichage fluide et presque en temps réel.

## Flux général

Le flux proposé est le suivant :

```text
Véhicules
   |
   v
Service d'ingestion
   |
   v
Validation et traitement
   |
   v
Service de télémétrie
   |
   v
Service de diffusion temps réel
   |
   v
WebSocket
   |
   v
Interface GeoTrack
   |
   v
Mise à jour de la carte
```

## Réduction du flux vers le navigateur

Le navigateur ne doit pas recevoir aveuglément les 2 000 messages par seconde de toute la flotte. Le service de diffusion applique :

- un filtrage selon les véhicules autorisés et la zone visible ;
- l'envoi de la dernière position connue plutôt que de toutes les positions intermédiaires ;
- un regroupement des mises à jour sur une courte fenêtre ;
- une limitation de fréquence adaptée à l'affichage ;
- une reprise par instantané après une reconnexion.

## Message de mise à jour

Chaque événement envoyé à l'interface contient au minimum `vehicle_id`, la position, la vitesse, le statut, l'horodatage et un numéro de version ou de séquence. L'interface ignore un événement plus ancien que la dernière position déjà affichée.

## Gestion des interruptions

1. L'interface détecte la perte de la connexion WebSocket.
2. Elle indique que les données peuvent être périmées.
3. Elle tente une reconnexion avec un délai progressif.
4. Après reconnexion, elle demande un instantané cohérent des véhicules visibles.
5. Les mises à jour en direct reprennent après l'instantané.

## Critères de validation

- Une position reçue est appliquée au bon marqueur sans recharger toute la carte.
- Un événement ancien ne remplace jamais une position plus récente.
- La perte de connexion est visible et la reprise ne duplique pas les marqueurs.
- Le flux envoyé au navigateur reste borné lorsque la flotte atteint 10 000 véhicules.
- Les droits d'accès sont appliqués avant la diffusion.

## Conclusion

Le flux temps réel repose sur un WebSocket, mais il est filtré et regroupé côté serveur. Cette décision protège le navigateur contre le volume brut de télémétrie tout en maintenant un affichage réactif.
