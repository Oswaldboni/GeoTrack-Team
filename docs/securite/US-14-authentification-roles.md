# US-14.1 — Authentification forte et gestion des rôles

## Objectif

Définir le mécanisme d'authentification et de contrôle d'accès permettant de sécuriser l'utilisation de GeoTrack selon le rôle de chaque utilisateur.

## Authentification forte

L'accès à GeoTrack repose sur une authentification sécurisée comprenant :

- un identifiant utilisateur ;
- un mot de passe ;
- un second facteur d'authentification (MFA).

Le second facteur renforce la sécurité en réduisant le risque d'accès non autorisé lorsqu'un mot de passe est compromis.

## Gestion des rôles

GeoTrack utilise un modèle RBAC (Role-Based Access Control).

Trois rôles principaux sont définis :

### Admin

Responsabilités principales :

- gérer les utilisateurs ;
- attribuer et modifier les rôles ;
- configurer les paramètres du système ;
- accéder aux fonctions d'administration ;
- consulter les journaux de sécurité ;
- gérer les règles de sécurité.

### Gestionnaire

Responsabilités principales :

- consulter l'état de la flotte ;
- consulter les véhicules ;
- consulter les trajets ;
- consulter et traiter les alertes ;
- consulter les tableaux de bord ;
- accéder aux rapports autorisés.

### Opérateur

Responsabilités principales :

- consulter les véhicules autorisés ;
- suivre les positions et états des véhicules ;
- consulter les alertes nécessaires à son travail ;
- accéder uniquement aux fonctions opérationnelles autorisées.

## Principe du moindre privilège

Chaque utilisateur doit disposer uniquement des permissions nécessaires à son rôle.

Un utilisateur ne doit pas pouvoir accéder à une fonction qui ne correspond pas à ses responsabilités.

## Matrice simplifiée des permissions

| Fonction | Admin | Gestionnaire | Opérateur |
|---|---|---|---|
| Gérer les utilisateurs | Oui | Non | Non |
| Attribuer les rôles | Oui | Non | Non |
| Configurer le système | Oui | Non | Non |
| Consulter la flotte | Oui | Oui | Oui |
| Consulter les trajets | Oui | Oui | Limité |
| Consulter les alertes | Oui | Oui | Oui |
| Gérer les alertes | Oui | Oui | Limité |
| Consulter les rapports | Oui | Oui | Limité |
| Consulter les journaux de sécurité | Oui | Limité | Non |

## Contrôle d'accès

Après authentification :

1. le système identifie l'utilisateur ;
2. il détermine son rôle ;
3. il récupère les permissions associées ;
4. il vérifie les autorisations avant chaque opération protégée ;
5. l'accès est accordé ou refusé.

## Traçabilité

Les événements importants doivent être journalisés, notamment :

- connexions réussies ;
- échecs de connexion ;
- changements de rôles ;
- accès refusés ;
- modifications sensibles ;
- actions administratives.

## Résultat attendu

GeoTrack dispose d'un mécanisme d'authentification forte et d'un modèle RBAC permettant de contrôler l'accès aux fonctionnalités selon les rôles Admin, Gestionnaire et Opérateur.
