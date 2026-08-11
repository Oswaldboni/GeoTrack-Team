# Registre des risques GeoTrack

## Échelle

- Probabilité : 1 faible, 2 moyenne, 3 élevée.
- Impact : 1 faible, 2 moyen, 3 élevé.
- Criticité : probabilité × impact.

Les responsables indiqués sont des rôles. L'équipe doit remplacer ou compléter ces rôles par le membre concerné dans Jira.

| ID | Risque | P | I | Score | Réponse prévue | Indicateur | Responsable | État |
|---|---|---:|---:|---:|---|---|---|---|
| R-01 | Le pipeline ne soutient pas 2 000 messages/s | 2 | 3 | 6 | Test de charge progressif, partitionnement et mise à l'échelle | Latence p95 et retard | Architecture | Ouvert |
| R-02 | Un pic ou une reconnexion massive sature l'ingestion | 2 | 3 | 6 | Kafka, contre-pression et capacité de pointe testée | Débit entrant et file | Ingestion | Ouvert |
| R-03 | Une panne d'un composant arrête le système | 2 | 3 | 6 | Redondance, réplication et basculement | Disponibilité | Infrastructure | Ouvert |
| R-04 | Les doublons faussent les alertes ou le stockage | 2 | 3 | 6 | Identifiant unique et consommateurs idempotents | Taux de doublons | Données | Ouvert |
| R-05 | Les positions arrivent dans le désordre | 2 | 2 | 4 | Partition par véhicule et contrôle de séquence | Événements périmés | Temps réel | Ouvert |
| R-06 | Les faux franchissements créent trop d'alertes | 2 | 2 | 4 | Validation géométrique et stabilisation de frontière | Alertes annulées | Geofencing | Ouvert |
| R-07 | Le stockage réel dépasse l'estimation de 37,84 To | 2 | 3 | 6 | Mesure du message, index séparés, compression et marge | Croissance quotidienne | Données | Ouvert |
| R-08 | Une restauration échoue après un incident | 2 | 3 | 6 | Sauvegardes chiffrées et exercices de restauration | Dernier test réussi | Résilience | Ouvert |
| R-09 | Un utilisateur accède à une flotte non autorisée | 2 | 3 | 6 | MFA, RBAC et contrôle serveur sur chaque requête | Accès refusés | Sécurité | Ouvert |
| R-10 | Les secrets ou données sensibles apparaissent dans les logs | 2 | 3 | 6 | Journalisation structurée, filtrage et contrôle d'accès | Détection de secrets | Sécurité | Ouvert |
| R-11 | La carte devient inutilisable avec 10 000 véhicules | 2 | 2 | 4 | Filtrage de zone, regroupement et limitation du rendu | Images/s et mémoire | Interface | Ouvert |
| R-12 | Les livrables Jira et GitHub divergent | 2 | 3 | 6 | Revue croisée US, critères, fichiers et PR avant remise | US sans preuve | Équipe | Ouvert |

## Revue du registre

Le registre doit être revu à chaque planification et rétrospective. Un risque fermé conserve sa date de fermeture et la preuve qui justifie la décision. Un problème déjà survenu doit être suivi comme incident ou tâche, pas seulement comme risque.
