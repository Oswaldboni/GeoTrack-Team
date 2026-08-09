# US-13.3 — Disaster Recovery Plan de GeoTrack

## Objectif

Définir les procédures de reprise permettant à GeoTrack de restaurer ses services critiques et ses données après un incident majeur.

Ce plan complète les mécanismes de haute disponibilité : la haute disponibilité vise à maintenir le service pendant certaines pannes, tandis que le Disaster Recovery Plan organise la restauration lorsque l'incident dépasse les mécanismes normaux de tolérance aux pannes.

## 1. Services critiques

Les éléments prioritaires pour la reprise sont :

- le point d'entrée de la télémétrie ;
- les services d'ingestion ;
- le broker ou la file de messages ;
- les services de traitement ;
- le stockage des données ;
- les API nécessaires à l'exploitation ;
- les mécanismes de supervision.

## 2. Principes de reprise

La stratégie repose sur :

- la détection rapide des incidents ;
- la redondance des composants ;
- la réplication des données ;
- le basculement vers des instances disponibles ;
- la persistance des messages ;
- les sauvegardes ;
- la restauration contrôlée ;
- la vérification de l'intégrité après reprise.

## 3. RPO et RTO

### RPO — Recovery Point Objective

Le RPO représente la quantité maximale de données que l'organisation accepte de perdre après un incident.

Pour GeoTrack, l'objectif proposé pour les données critiques de télémétrie est :

**RPO cible : inférieur ou égal à 5 minutes.**

Cet objectif suppose l'utilisation de mécanismes de persistance, de réplication et de sauvegarde adaptés.

### RTO — Recovery Time Objective

Le RTO représente la durée maximale visée pour restaurer un service après une interruption majeure.

Pour les services critiques de GeoTrack :

**RTO cible : inférieur ou égal à 30 minutes.**

Ces valeurs constituent des objectifs d'architecture proposés et devront être validées selon les contraintes opérationnelles réelles.

## 4. Scénarios de reprise

| Incident | Impact principal | Mécanisme de reprise | Objectif |
|---|---|---|---|
| Panne d'une instance d'ingestion | Réduction de capacité | Redirection vers les autres instances | Reprise immédiate |
| Panne d'un nœud de traitement | Traitement partiellement interrompu | Réaffectation aux autres nœuds | Quelques minutes |
| Broker indisponible | Interruption du flux de messages | Basculement vers une instance/réplique disponible | Limiter la perte de messages |
| Stockage principal indisponible | Écriture et lecture perturbées | Basculement vers une réplique | Restaurer rapidement l'accès |
| Corruption de données | Données inutilisables | Restauration depuis une sauvegarde valide | Respect du RPO |
| Incident majeur d'infrastructure | Plusieurs services indisponibles | Redéploiement et restauration contrôlée | Respect du RTO |
| Perte de connectivité | Interruption des échanges | Reprise après rétablissement du réseau | Rattraper les traitements en attente |

## 5. Procédure générale de reprise

### Étape 1 — Détection

La supervision détecte l'incident à partir notamment :

- des contrôles de disponibilité ;
- du taux d'erreur ;
- de la latence ;
- du débit ;
- de l'état des files de messages ;
- de l'état du stockage.

### Étape 2 — Qualification

L'équipe identifie :

- les composants touchés ;
- la gravité de l'incident ;
- les services encore disponibles ;
- le risque de perte ou de corruption des données.

### Étape 3 — Isolation

Si nécessaire, le composant défaillant est isolé afin d'éviter la propagation de l'incident.

### Étape 4 — Basculement

Lorsque des instances ou répliques sont disponibles, le trafic est redirigé vers les composants fonctionnels.

### Étape 5 — Restauration

Si les mécanismes de réplication ne permettent pas la reprise, les données sont restaurées depuis une sauvegarde valide.

### Étape 6 — Vérification

Avant le retour complet en production, l'équipe vérifie :

- l'intégrité des données ;
- le fonctionnement des services ;
- la reprise de l'ingestion ;
- le traitement des messages en attente ;
- les communications entre composants.

### Étape 7 — Retour au fonctionnement normal

Le trafic est progressivement rétabli et les composants restaurés sont réintégrés dans l'architecture.

### Étape 8 — Analyse après incident

L'incident doit être documenté afin d'identifier :

- la cause ;
- l'impact ;
- la durée ;
- les données éventuellement perdues ;
- les actions réalisées ;
- les améliorations nécessaires.

## 6. Sauvegardes

Les sauvegardes doivent être :

- régulières ;
- protégées contre les accès non autorisés ;
- chiffrées lorsque nécessaire ;
- séparées du stockage principal ;
- surveillées ;
- testées périodiquement.

Une sauvegarde non testée ne garantit pas qu'une restauration sera possible.

## 7. Tests du plan de reprise

Le Disaster Recovery Plan doit être testé périodiquement.

Les exercices peuvent inclure :

- simulation de panne d'une instance ;
- indisponibilité d'un service ;
- basculement vers une réplique ;
- restauration d'une sauvegarde ;
- simulation de perte d'un nœud ;
- vérification du traitement des messages accumulés.

Les résultats doivent être documentés afin d'améliorer progressivement le plan.

## 8. Responsabilités générales

Lors d'un incident majeur :

- la supervision détecte et signale l'incident ;
- l'équipe technique analyse la défaillance ;
- les responsables déclenchent les procédures de reprise appropriées ;
- l'intégrité des données est vérifiée avant le retour complet au service ;
- l'incident et les actions réalisées sont documentés.

## Conclusion

Le Disaster Recovery Plan complète la stratégie de haute disponibilité de GeoTrack.

La combinaison de la redondance, de la réplication, des sauvegardes, du basculement et de procédures de restauration testées permet de réduire l'impact des incidents majeurs et de restaurer les services critiques dans des délais définis.
