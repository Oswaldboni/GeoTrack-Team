# Stratégie de validation GeoTrack

## Objectif

Vérifier les contrats de données, les fonctions métier, les performances, la résilience, la sécurité et les interfaces documentés dans le dépôt.

## Environnements

- Tests unitaires : fonctions isolées et schémas.
- Tests d'intégration : ingestion, broker, traitements et stockage.
- Tests système : flux complet jusqu'au tableau de bord.
- Tests de charge et de panne : environnement représentatif, sans données réelles sensibles.

## Matrice initiale

| ID | Scénario | Niveau | Résultat attendu | Preuve | État |
|---|---|---|---|---|---|
| T-01 | Valider un message conforme au JSON Schema | Unitaire | Message accepté | Rapport automatisé | À exécuter |
| T-02 | Rejeter latitude, vitesse ou champ obligatoire invalide | Unitaire | Rejet précis, aucune publication | Rapport automatisé | À exécuter |
| T-03 | Générer 10 000 messages avec le simulateur | Technique | Aucun échec de génération | Journal de commande | Vérifié localement |
| T-04 | Ingestion nominale à 2 000 messages/s | Charge | Aucune perte, latence dans la cible | Graphiques et logs | À exécuter |
| T-05 | Pointe proposée à 4 000 messages/s | Charge | Pic absorbé, retard résorbé | Graphiques Kafka | À exécuter |
| T-06 | Perte d'une instance d'ingestion | Résilience | Flux maintenu avec capacité réduite | Chronologie de panne | À exécuter |
| T-07 | Reconnexion WebSocket | Système | Instantané puis deltas, aucun doublon | Capture et logs | À exécuter |
| T-08 | Entrée et sortie d'un cercle et d'un polygone | Métier | Un événement unique par transition | Résultats de cas | À exécuter |
| T-09 | Oscillation GPS près d'une frontière | Métier | Pas d'avalanche d'alertes | Journal d'événements | À exécuter |
| T-10 | Dépassement de vitesse continu | Métier | Alerte initiale sans répétition abusive | Journal d'événements | À exécuter |
| T-11 | Accès d'un rôle non autorisé | Sécurité | Accès refusé et journalisé | Rapport de test | À exécuter |
| T-12 | Export d'un gestionnaire filtré | Sécurité | Seulement les véhicules autorisés | Fichier et journal | À exécuter |
| T-13 | Restauration d'une sauvegarde | Reprise | Intégrité vérifiée dans le RPO/RTO proposé | Procès-verbal | À exécuter |
| T-14 | Carte avec 10 000 véhicules enregistrés | Interface | Navigation et sélection utilisables | Mesures navigateur | À exécuter |
| T-15 | Vérification visuelle responsive | Interface | Aucun texte coupé ou chevauché | Captures de référence | À corriger |

## Mesures obligatoires

- débit accepté et traité ;
- taux d'erreur et de rejet ;
- latence aux percentiles 50, 95 et 99 ;
- retard et âge du plus ancien message ;
- CPU, mémoire et espace disque ;
- nombre de pertes et de doublons ;
- temps de détection et de reprise après panne.

## Règle de clôture

Un test n'est considéré comme réussi que si son environnement, ses données d'entrée, son résultat et sa preuve sont conservés. Les états « À exécuter » ne doivent pas être présentés comme des validations réalisées.
