# US-14.2 — Chiffrement des communications et des données

## Objectif

Définir les mécanismes de sécurité permettant de protéger les données GeoTrack pendant leur transmission et lorsqu'elles sont stockées.

## 1. Protection des données en transit

Toutes les communications contenant des données GeoTrack doivent utiliser des canaux chiffrés.

Cela concerne notamment :

- les communications entre les véhicules et le service d'ingestion ;
- les communications entre les API et les applications clientes ;
- les échanges entre les services internes ;
- les communications avec les interfaces d'administration ;
- les transferts de données vers les systèmes de stockage.

## 2. Utilisation de TLS

Les communications réseau doivent utiliser TLS afin de protéger :

- la confidentialité des données ;
- l'intégrité des échanges ;
- l'authenticité des services.

Les versions obsolètes des protocoles de sécurité ne doivent pas être utilisées.

La configuration cible doit privilégier TLS 1.3 et permettre TLS 1.2 lorsqu'une compatibilité est nécessaire.

## 3. Protection des données au repos

Les données stockées doivent également être protégées par chiffrement.

Cela concerne notamment :

- les bases de données ;
- les données historiques ;
- les fichiers contenant des informations sensibles ;
- les sauvegardes ;
- les archives.

Le chiffrement au repos permet de limiter l'exploitation des données lorsqu'un support de stockage ou une sauvegarde est obtenu sans autorisation.

## 4. Gestion des clés

Les clés de chiffrement doivent être gérées séparément des données.

Les principes suivants doivent être appliqués :

- limiter l'accès aux clés ;
- journaliser les opérations sensibles ;
- prévoir la rotation des clés ;
- empêcher le stockage des clés directement dans le code source ;
- séparer les responsabilités entre gestion des données et gestion des clés.

## 5. Authentification des services

Un canal chiffré ne suffit pas à lui seul.

Les composants GeoTrack doivent également vérifier l'identité des services avec lesquels ils communiquent.

Les certificats numériques permettent notamment de vérifier l'identité d'un service lors de l'établissement d'une connexion TLS.

## 6. Protection des sauvegardes

Les sauvegardes doivent bénéficier d'un niveau de protection comparable aux données principales.

Elles doivent notamment :

- être chiffrées ;
- être accessibles uniquement aux utilisateurs ou services autorisés ;
- être protégées contre les modifications non autorisées ;
- faire l'objet de procédures de restauration contrôlées.

## 7. Flux sécurisé proposé

Véhicule
→ connexion TLS
→ service d'ingestion
→ communications internes sécurisées
→ services GeoTrack
→ stockage chiffré

Les applications utilisateur accèdent également aux API GeoTrack au moyen de connexions sécurisées.

## 8. Journalisation

Les événements liés à la sécurité doivent être journalisés, notamment :

- échecs d'établissement de connexions sécurisées ;
- erreurs de certificat ;
- opérations de gestion des clés ;
- tentatives d'accès non autorisées ;
- opérations sensibles sur les données.

## 9. Principes de sécurité

La stratégie repose sur plusieurs principes :

- chiffrement en transit ;
- chiffrement au repos ;
- séparation des clés et des données ;
- contrôle strict des accès ;
- rotation des clés ;
- traçabilité des opérations sensibles.

## Résultat attendu

Les données GeoTrack restent protégées pendant leur transmission, leur stockage et leur sauvegarde.

La combinaison du chiffrement, de la gestion sécurisée des clés et du contrôle d'accès réduit les risques de divulgation ou de modification non autorisée des informations.
