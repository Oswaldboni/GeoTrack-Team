# US-14.3 — Sécurité applicative de GeoTrack

## Objectif

Cette section présente les principaux mécanismes de sécurité retenus pour protéger la plateforme GeoTrack, ses utilisateurs, ses services et les données de télémétrie.

## 1. Authentification forte

L'accès à GeoTrack repose sur une authentification sécurisée.

Le mécanisme proposé combine :

- un identifiant utilisateur ;
- un mot de passe ;
- un second facteur d'authentification.

L'utilisation d'un second facteur permet de réduire le risque d'accès non autorisé lorsqu'un mot de passe est compromis.

## 2. Gestion des rôles et des permissions

GeoTrack utilise un modèle RBAC afin d'attribuer les autorisations selon les responsabilités de chaque utilisateur.

Les rôles principaux sont :

- Admin ;
- Gestionnaire ;
- Opérateur.

### Admin

Le rôle Admin dispose notamment des autorisations nécessaires pour :

- gérer les utilisateurs ;
- attribuer les rôles ;
- configurer le système ;
- consulter les journaux de sécurité ;
- effectuer certaines opérations administratives sensibles.

### Gestionnaire

Le Gestionnaire peut notamment :

- consulter la flotte ;
- consulter les trajets ;
- consulter et gérer les alertes ;
- accéder aux tableaux de bord ;
- consulter les rapports autorisés.

### Opérateur

L'Opérateur dispose d'un accès plus limité aux fonctions nécessaires aux opérations quotidiennes.

## 3. Principe du moindre privilège

Chaque utilisateur doit disposer uniquement des autorisations nécessaires à ses responsabilités.

Ce principe permet de limiter les conséquences d'une erreur, d'un compte compromis ou d'une utilisation non autorisée.

## 4. Sécurisation des communications

Les communications entre les différents composants de GeoTrack doivent être protégées par TLS.

Cela concerne notamment :

- les communications entre les véhicules et le service d'ingestion ;
- les échanges entre les API et les interfaces utilisateur ;
- les communications entre services internes ;
- les connexions vers les systèmes de stockage.

TLS permet de protéger la confidentialité et l'intégrité des données pendant leur transmission.

## 5. Protection des données au repos

Les données sensibles doivent être chiffrées lorsqu'elles sont stockées.

Cette protection concerne notamment :

- les bases de données ;
- les données historiques ;
- les sauvegardes ;
- les archives ;
- les fichiers contenant des informations sensibles.

## 6. Gestion des clés de chiffrement

Les clés de chiffrement doivent être séparées des données protégées.

La stratégie prévoit notamment :

- un accès limité aux clés ;
- la rotation périodique des clés ;
- la journalisation des opérations sensibles ;
- l'interdiction de stocker des clés directement dans le code source.

## 7. Journalisation et traçabilité

Les événements de sécurité importants doivent être enregistrés.

Exemples :

- connexions réussies ;
- échecs de connexion ;
- accès refusés ;
- changements de rôles ;
- modifications de paramètres sensibles ;
- opérations administratives ;
- erreurs liées aux certificats ou aux communications sécurisées.

Ces informations facilitent les audits et l'analyse des incidents.

## 8. Protection des sauvegardes

Les sauvegardes doivent bénéficier du même niveau de protection que les données principales.

Elles doivent notamment :

- être chiffrées ;
- être accessibles uniquement aux utilisateurs ou services autorisés ;
- être protégées contre les modifications non autorisées ;
- pouvoir être restaurées au moyen de procédures contrôlées.

## 9. Principaux risques couverts

La stratégie vise notamment à réduire les risques suivants :

- accès non autorisé ;
- vol de compte utilisateur ;
- interception des communications ;
- fuite de données ;
- modification non autorisée des informations ;
- abus de privilèges ;
- exploitation d'une sauvegarde compromise.

## 10. Synthèse

La sécurité de GeoTrack repose sur plusieurs mécanismes complémentaires :

- authentification forte ;
- gestion des rôles ;
- principe du moindre privilège ;
- chiffrement des communications ;
- chiffrement des données au repos ;
- gestion sécurisée des clés ;
- journalisation ;
- protection des sauvegardes.

## Conclusion

L'architecture de sécurité proposée vise à protéger les utilisateurs, les services et les données de GeoTrack tout au long de leur cycle de vie.

La combinaison du contrôle d'accès, du chiffrement et de la traçabilité permet de réduire les principaux risques liés à l'exploitation d'une plateforme de suivi de flotte.
