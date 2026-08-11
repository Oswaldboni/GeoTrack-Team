# US-02.1 — Rafraîchissement en temps réel des positions

## Objectif

Définir le mécanisme utilisé par GeoTrack pour mettre à jour rapidement les positions des véhicules dans l'interface utilisateur.

## Solutions étudiées

Deux approches principales sont considérées :

- polling HTTP ;
- WebSocket.

## 1. Polling HTTP

Avec le polling HTTP, le client interroge régulièrement le serveur pour demander les nouvelles positions.

Exemple :

```text
Client
  |
  |---- requête HTTP ----> Serveur
  |<--- positions --------|
```

Le polling est simple à mettre en œuvre, mais il génère des requêtes même lorsqu'aucune position pertinente n'a changé. Un intervalle court augmente la charge, tandis qu'un intervalle long augmente la latence.

## 2. WebSocket

Avec WebSocket, une connexion persistante permet au serveur d'envoyer les nouvelles positions lorsqu'elles sont disponibles.

```text
Client <==== connexion WebSocket persistante ====> Serveur
Client <----------- mises à jour filtrées -------- Serveur
```

Cette approche réduit les requêtes répétitives et permet une diffusion bidirectionnelle presque en temps réel. Elle exige toutefois une gestion explicite des reconnexions, de l'authentification, de la reprise et de la limitation du débit envoyé au navigateur.

## Comparaison

| Critère | Polling HTTP | WebSocket |
|---|---|---|
| Latence | Dépend de l'intervalle | Faible après réception |
| Requêtes inutiles | Fréquentes | Limitées |
| Mise en œuvre initiale | Simple | Plus complexe |
| Reconnexion | Naturelle à chaque requête | À gérer explicitement |
| Adaptation au suivi en direct | Moyenne | Bonne |

## Décision

WebSocket est retenu pour les mises à jour en direct. Une API HTTP reste utilisée pour l'authentification, les instantanés initiaux, les filtres et la récupération après reconnexion.

Le serveur ne diffuse pas le flux brut de toute la flotte. Il filtre, regroupe et limite les mises à jour selon les droits, la zone visible et la capacité de l'interface.

## Critères de validation

- La connexion est authentifiée et limitée aux données autorisées.
- Une reconnexion récupère un instantané avant de reprendre les deltas.
- Les marqueurs ne sont ni dupliqués ni ramenés à une position ancienne.
- La fréquence de rendu reste stable avec 10 000 véhicules enregistrés.

## Conclusion

WebSocket répond mieux au besoin de réactivité, à condition d'être complété par une API HTTP et par une stratégie de reconnexion, de filtrage et de contrôle du débit.
  |
  | attente
  |
  |---- requête HTTP ----> Serveur
  |<--- positions --------|
