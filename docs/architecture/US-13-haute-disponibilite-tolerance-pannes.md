# US-13.2 — Plan de tolérance aux pannes et de haute disponibilité

## Objectif

Définir une stratégie permettant à GeoTrack de maintenir ses services critiques disponibles 24 h/24 et 7 j/7 malgré la défaillance d'un composant individuel.

## 1. Principes de haute disponibilité

L'architecture GeoTrack doit éviter les composants critiques reposant sur une seule instance.

La stratégie repose principalement sur :

- la redondance des services ;
- la répartition de charge ;
- la réplication des données ;
- le basculement automatique ;
- la persistance temporaire des messages ;
- la supervision continue ;
- les mécanismes de reprise.

## 2. Services d'ingestion

Le service d'ingestion reçoit continuellement les messages de télémétrie des véhicules.

Plusieurs instances du service doivent pouvoir fonctionner simultanément.

Si une instance devient indisponible, les autres instances doivent continuer à recevoir et traiter les messages.

## 3. Répartition de charge

Un mécanisme de répartition de charge distribue le trafic entre les instances disponibles.

Son rôle est notamment de :

- distribuer les connexions entrantes ;
- éviter la surcharge d'une instance ;
- détecter les instances indisponibles ;
- retirer une instance défaillante du trafic ;
- rediriger le trafic vers les instances disponibles.

## 4. Tolérance aux pannes du flux de messages

Une file ou un broker de messages permet de découpler la réception des données de leur traitement.

Si un service consommateur devient temporairement indisponible, les messages peuvent être conservés avant d'être traités après son retour.

Le broker doit lui-même disposer de mécanismes de réplication et de persistance afin de ne pas devenir un point de défaillance unique.

## 5. Haute disponibilité du stockage

Les données critiques ne doivent pas dépendre d'une seule instance de stockage.

La stratégie prévoit :

- la réplication des données ;
- plusieurs instances ou nœuds ;
- un mécanisme de basculement ;
- des sauvegardes régulières ;
- des procédures de restauration testées.

## 6. Basculement

Lorsqu'une instance critique devient indisponible, une instance ou une réplique disponible doit pouvoir prendre le relais.

Le basculement doit limiter autant que possible l'interruption visible pour les utilisateurs et les véhicules.

## 7. Supervision

La plateforme doit surveiller en continu :

- la disponibilité des services ;
- le taux d'erreur ;
- la latence ;
- le débit de messages ;
- l'état du broker ;
- l'état du stockage ;
- l'utilisation des ressources ;
- la taille des files d'attente.

Des alertes doivent être déclenchées lorsqu'un seuil critique est atteint.

## 8. Reprise automatique

Lorsque cela est possible, les services défaillants doivent pouvoir être redémarrés ou remplacés automatiquement.

Une instance remplacée doit pouvoir rejoindre de nouveau le système sans provoquer d'interruption générale.

## 9. Scénarios de panne

| Scénario | Réponse prévue |
|---|---|
| Panne d'une instance d'ingestion | Redirection du trafic vers les autres instances |
| Panne d'un nœud de traitement | Traitement poursuivi par les autres nœuds |
| Service consommateur indisponible | Conservation temporaire des messages dans le broker |
| Panne d'une instance de stockage | Basculement vers une réplique disponible |
| Surcharge d'une instance | Répartition de la charge sur les autres instances |
| Perte temporaire de connectivité | Reprise des communications lorsque la connexion revient |
| Défaillance détectée par la supervision | Déclenchement d'une alerte et procédure de reprise |

## 10. Sauvegarde et restauration

La réplication ne remplace pas les sauvegardes.

Des sauvegardes régulières doivent permettre de restaurer les données après une corruption, une erreur humaine ou un incident majeur.

Les procédures de restauration doivent être documentées et testées.

## 11. Architecture logique de résilience

Le flux logique peut être représenté ainsi :

Véhicules  
→ point d'entrée réparti  
→ plusieurs instances d'ingestion  
→ broker de messages répliqué  
→ plusieurs services de traitement  
→ stockage répliqué

La supervision observe l'ensemble de ces composants et déclenche les alertes nécessaires.

## Résultat attendu

La défaillance d'une instance individuelle ne doit pas provoquer l'arrêt complet de GeoTrack.

La combinaison de la redondance, de la réplication, du basculement, de la supervision et des procédures de reprise permet de soutenir l'exigence de haute disponibilité 24/7.
