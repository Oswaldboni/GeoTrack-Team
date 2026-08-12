# US-12 — Matrice des permissions par rôle

| Élément de traçabilité | Référence |
|---|---|
| User Story | US-12 / GTB-45 |
| Sous-tâche Jira | GTB-96 |
| Branche GitHub prévue | `feature/US-12` |
| Statut du livrable | En attente de validation de l'équipe |

## 1. Objectif

Définir les permissions associées aux trois rôles de GeoTrack afin de contrôler précisément ce que chaque utilisateur peut consulter et modifier dans l'application.

Cette matrice constitue la référence fonctionnelle pour l'implémentation du contrôle d'accès fondé sur les rôles (RBAC — Role-Based Access Control).

## 2. Rôles

| Rôle | Responsabilités |
|---|---|
| Administrateur | Administration complète de GeoTrack, y compris les utilisateurs, les rôles, la configuration et les journaux de sécurité. |
| Gestionnaire de flotte | Gestion opérationnelle des véhicules, des zones, des alertes et des rapports, sans gestion des comptes ni attribution des rôles. |
| Opérateur | Consultation et utilisation quotidienne des fonctions autorisées, sans droit de configuration, d'exportation ou d'administration. |

## 3. Légende

- **Autorisé** : le rôle peut exécuter l'action.
- **Limité** : le rôle peut exécuter seulement l'action précisée dans la colonne « Limitation ».
- **Interdit** : le rôle ne peut ni exécuter l'action ni appeler directement le service ou l'API associé.

## 4. Matrice détaillée des permissions

| Domaine | Permission | Administrateur | Gestionnaire de flotte | Opérateur | Limitation |
|---|---|---:|---:|---:|---|
| Carte | Voir la carte | Autorisé | Autorisé | Autorisé | L'opérateur voit uniquement les véhicules et les zones auxquels il est affecté. |
| Carte | Voir la position en temps réel des véhicules | Autorisé | Autorisé | Limité | L'opérateur voit uniquement les véhicules autorisés. |
| Carte | Utiliser les filtres de recherche | Autorisé | Autorisé | Limité | L'opérateur utilise les filtres courants sans enregistrer ni partager une configuration globale. |
| Véhicules | Consulter la fiche d'un véhicule | Autorisé | Autorisé | Limité | Consultation des véhicules affectés à l'opérateur. |
| Véhicules | Ajouter un véhicule | Autorisé | Autorisé | Interdit | — |
| Véhicules | Modifier un véhicule | Autorisé | Autorisé | Interdit | — |
| Véhicules | Supprimer ou désactiver un véhicule | Autorisé | Autorisé | Interdit | La suppression logique ou la désactivation est privilégiée pour conserver l'historique. |
| Geofencing | Voir les zones | Autorisé | Autorisé | Autorisé | L'opérateur voit seulement les zones utiles à ses activités. |
| Geofencing | Créer une zone | Autorisé | Autorisé | Interdit | — |
| Geofencing | Modifier une zone | Autorisé | Autorisé | Interdit | — |
| Geofencing | Supprimer ou désactiver une zone | Autorisé | Autorisé | Interdit | — |
| Alertes | Voir les alertes | Autorisé | Autorisé | Limité | Lecture des alertes associées aux véhicules ou zones autorisés. |
| Alertes | Acquitter une alerte | Autorisé | Autorisé | Interdit | — |
| Alertes | Fermer ou classer une alerte | Autorisé | Autorisé | Interdit | — |
| Alertes | Configurer les règles et les seuils | Autorisé | Autorisé | Interdit | Le gestionnaire agit uniquement sur les règles opérationnelles de la flotte. |
| Tableau de bord | Voir les indicateurs analytiques | Autorisé | Autorisé | Limité | L'opérateur accède uniquement aux indicateurs opérationnels liés à son périmètre. |
| Tableau de bord | Personnaliser les tableaux de bord | Autorisé | Autorisé | Interdit | — |
| Rapports | Consulter les rapports | Autorisé | Autorisé | Limité | L'opérateur consulte uniquement les rapports préautorisés de son périmètre. |
| Rapports | Générer un rapport | Autorisé | Autorisé | Interdit | — |
| Données | Exporter les données | Autorisé | Autorisé | Interdit | Toute exportation doit être journalisée. |
| Comptes | Voir la liste des utilisateurs | Autorisé | Interdit | Interdit | — |
| Comptes | Créer un compte utilisateur | Autorisé | Interdit | Interdit | — |
| Comptes | Modifier, suspendre ou supprimer un compte | Autorisé | Interdit | Interdit | — |
| Rôles | Attribuer ou modifier un rôle | Autorisé | Interdit | Interdit | L'administrateur ne doit pas contourner les règles de séparation des responsabilités définies par l'équipe. |
| Sécurité | Voir les journaux d'audit et de sécurité | Autorisé | Limité | Interdit | Le gestionnaire voit uniquement les événements opérationnels de son périmètre. |
| Sécurité | Modifier les paramètres de sécurité | Autorisé | Interdit | Interdit | — |
| Système | Modifier la configuration globale | Autorisé | Interdit | Interdit | — |

## 5. Codes de permissions proposés

Les contrôles dans l'interface et dans l'API doivent utiliser des codes stables plutôt que le nom affiché des rôles.

| Code | Action protégée |
|---|---|
| `map.read` | Consulter la carte et les positions autorisées. |
| `map.filter` | Utiliser les filtres de la carte. |
| `vehicle.read` | Consulter les véhicules autorisés. |
| `vehicle.create` | Ajouter un véhicule. |
| `vehicle.update` | Modifier un véhicule. |
| `vehicle.delete` | Supprimer ou désactiver un véhicule. |
| `geofence.read` | Consulter les zones. |
| `geofence.create` | Créer une zone. |
| `geofence.update` | Modifier une zone. |
| `geofence.delete` | Supprimer ou désactiver une zone. |
| `alert.read` | Consulter les alertes autorisées. |
| `alert.acknowledge` | Acquitter une alerte. |
| `alert.close` | Fermer ou classer une alerte. |
| `alert.configure` | Configurer les règles et les seuils. |
| `dashboard.read` | Consulter le tableau de bord autorisé. |
| `dashboard.configure` | Personnaliser un tableau de bord. |
| `report.read` | Consulter les rapports autorisés. |
| `report.generate` | Générer un rapport. |
| `data.export` | Exporter des données. |
| `user.read` | Consulter les comptes utilisateurs. |
| `user.create` | Créer un compte. |
| `user.update` | Modifier ou suspendre un compte. |
| `user.delete` | Supprimer un compte. |
| `role.assign` | Attribuer ou modifier un rôle. |
| `audit.read` | Consulter les journaux autorisés. |
| `security.configure` | Modifier les paramètres de sécurité. |
| `system.configure` | Modifier la configuration globale. |

## 6. Modèle de données recommandé

Le modèle doit séparer les rôles, les permissions et leurs associations.

```sql
CREATE TABLE roles (
    id BIGINT PRIMARY KEY,
    code VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE permissions (
    id BIGINT PRIMARY KEY,
    code VARCHAR(100) UNIQUE NOT NULL,
    description VARCHAR(255) NOT NULL
);

CREATE TABLE role_permissions (
    role_id BIGINT NOT NULL,
    permission_id BIGINT NOT NULL,
    access_level VARCHAR(20) NOT NULL
        CHECK (access_level IN ('allowed', 'limited', 'denied')),
    scope_rule VARCHAR(255),
    PRIMARY KEY (role_id, permission_id),
    FOREIGN KEY (role_id) REFERENCES roles(id),
    FOREIGN KEY (permission_id) REFERENCES permissions(id)
);
```

La colonne `scope_rule` décrit les restrictions applicables aux accès limités, par exemple `assigned_vehicles_only` ou `operational_dashboard_only`.

## 7. Règles d'implémentation

1. Toute action absente de la matrice est refusée par défaut.
2. Le serveur vérifie la permission à chaque requête protégée; masquer un bouton dans l'interface ne suffit pas.
3. Les accès limités sont contrôlés selon le périmètre de l'utilisateur, par exemple les véhicules, les zones ou les rapports qui lui sont affectés.
4. Les changements de rôle, les refus d'accès, les exportations et les actions sensibles sont journalisés.
5. Une modification de la matrice doit être validée par l'équipe et versionnée dans GitHub avant son implémentation.
6. Les droits d'un utilisateur sont recalculés dès qu'un rôle ou une affectation est modifié.

## 8. Vérification des critères d'acceptation

| Critère | Réponse du livrable |
|---|---|
| Chaque fonctionnalité majeure est associée à une permission par rôle. | La matrice détaille la carte, les véhicules, le geofencing, les alertes, le tableau de bord, les rapports, les données, les comptes, les rôles, la sécurité et la configuration. |
| Les permissions sont autorisées, interdites ou limitées. | Les trois niveaux sont définis et chaque accès limité possède une restriction explicite. |
| La matrice est réutilisable pour le développement. | Des codes de permissions stables et un modèle `role_permissions` sont proposés. |
| Le principe du moindre privilège est appliqué. | Toute permission absente est refusée par défaut et le périmètre des accès limités est vérifié côté serveur. |
| La matrice est validée par l'équipe. | Statut à compléter après revue : **En attente de validation de l'équipe**. |

## 9. Décision de l'équipe

- Date de validation : à compléter.
- Participants : à compléter.
- Décision : à compléter (`approuvée`, `approuvée avec modifications` ou `refusée`).
- Commentaires : à compléter.
