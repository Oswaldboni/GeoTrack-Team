# US-12 / GTB-98 — Spécifications fonctionnelles des parcours de gestion des comptes utilisateurs

## Traçabilité

| Élément | Référence |
|---|---|
| User Story | US-12 / GTB-45 — Gestion des comptes utilisateurs et des rôles |
| Sous-tâche Jira | GTB-98 — Rédiger les spécifications fonctionnelles des parcours d'invitation, de création et de modification des comptes utilisateurs |
| Matrice de référence | GTB-96 — Matrice des permissions par rôle |
| Diagramme de référence | GTB-97 — Diagramme UML de gestion des habilitations |
| Branche de travail | `feature/US-12.3-specifications-parcours-comptes-utilisateurs` |
| Statut | Prêt pour revue de l'équipe |

## 1. Objectif

Définir le comportement fonctionnel attendu des parcours d'invitation, de création et de modification des comptes GeoTrack. Cette spécification précise les acteurs autorisés, les champs, les validations, les changements d'état, les erreurs, les permissions et les interfaces de service proposées afin de permettre une implémentation sans ambiguïté.

## 2. Périmètre et acteurs

### 2.1 Acteurs

| Acteur | Actions permises dans ce périmètre |
|---|---|
| Administrateur | Inviter un utilisateur, créer directement un compte, consulter les comptes, modifier les informations, le rôle et le statut d'un compte. |
| Utilisateur invité | Finaliser son compte à partir d'un lien d'activation valide. |
| Utilisateur authentifié | Modifier ses informations personnelles de base et son mot de passe. |
| Gestionnaire de flotte | Aucune administration des comptes ou des rôles. Il peut uniquement modifier son propre profil. |
| Opérateur | Aucune administration des comptes ou des rôles. Il peut uniquement modifier son propre profil. |

Les opérations d'administration exigent les permissions de GTB-96 : `user.create`, `user.update` et, pour tout changement de rôle, `role.assign`.

### 2.2 Hors périmètre

- Authentification multifacteur.
- Réinitialisation d'un mot de passe oublié.
- Création ou modification de nouveaux types de rôles.
- Importation massive d'utilisateurs.
- Suppression physique définitive des comptes et des traces d'audit.

## 3. Règles fonctionnelles communes

### 3.1 États d'un compte

| État | Signification | Connexion permise |
|---|---|:---:|
| `INVITED` | Invitation envoyée, mais compte non finalisé. | Non |
| `ACTIVE` | Compte finalisé et utilisable. | Oui |
| `DISABLED` | Compte désactivé par un administrateur. | Non |

Un email ne peut correspondre qu'à un seul compte, quel que soit son état. Une invitation en attente n'autorise pas la création d'un second compte avec le même email.

### 3.2 Règles sur les données

| Champ | Obligatoire | Règles |
|---|:---:|---|
| Prénom | Oui à l'activation ou à la création directe | De 1 à 100 caractères après suppression des espaces inutiles. |
| Nom | Oui à l'activation ou à la création directe | De 1 à 100 caractères après suppression des espaces inutiles. |
| Email | Oui | Format valide, normalisé en minuscules pour la comparaison, unique dans le système. |
| Rôle | Oui | Valeur existante parmi `ADMINISTRATEUR`, `GESTIONNAIRE_FLOTTE` et `OPERATEUR`. |
| Mot de passe | Oui à l'activation et à la création directe | Au moins 12 caractères, avec au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial. Ne doit jamais être enregistré ni journalisé en clair. |
| Confirmation du mot de passe | Oui dans l'interface | Doit être identique au mot de passe. Elle n'est pas conservée. |
| Statut | Géré par le système ou l'administrateur | Valeur parmi `INVITED`, `ACTIVE` et `DISABLED`. |

### 3.3 Autorisation et moindre privilège

1. Toute opération non explicitement autorisée est refusée.
2. Le serveur contrôle les permissions à chaque requête; masquer un bouton dans l'interface ne constitue pas un contrôle suffisant.
3. Seul un administrateur peut inviter un utilisateur, créer directement un compte, modifier le rôle d'un tiers ou changer son statut.
4. Un utilisateur ne peut jamais modifier son propre rôle ni son propre statut.
5. Un changement de rôle prend effet dès l'enregistrement. Le cache d'autorisations est invalidé et toute session utilisant d'anciennes permissions doit être actualisée ou révoquée.
6. La désactivation d'un compte révoque ses sessions actives et bloque immédiatement toute nouvelle connexion.
7. Les actions sensibles sont inscrites dans le journal d'audit sans mot de passe ni jeton d'invitation en clair.

## 4. Parcours d'invitation

### 4.1 Préconditions

- L'administrateur est authentifié.
- Il possède la permission `user.create`.
- Le rôle choisi existe et peut être attribué.

### 4.2 Formulaire d'invitation

| Champ | Type | Obligatoire | Validation |
|---|---|:---:|---|
| Email | Champ email | Oui | Format valide et email non utilisé. |
| Rôle prévu | Liste | Oui | Rôle existant et autorisé. |

### 4.3 Déroulement nominal

1. L'administrateur ouvre la fonction « Inviter un utilisateur ».
2. Il saisit l'email et sélectionne le rôle prévu.
3. Le système valide l'autorisation, le format de l'email, son unicité et le rôle.
4. Le système crée un compte à l'état `INVITED`.
5. Le système génère un jeton d'activation à usage unique, valable 48 heures.
6. Le système enregistre uniquement une représentation sécurisée du jeton et sa date d'expiration.
7. Un email contenant le lien d'activation est envoyé à l'adresse indiquée.
8. Le système confirme à l'administrateur que l'invitation a été envoyée.
9. L'utilisateur ouvre le lien et le système vérifie le jeton.
10. Si le jeton est valide, un formulaire demande le prénom, le nom, le mot de passe et sa confirmation. L'email et le rôle sont affichés en lecture seule.
11. Le système valide les champs et active le compte.
12. Le jeton devient inutilisable, le statut passe de `INVITED` à `ACTIVE` et les permissions du rôle sont appliquées.

### 4.4 Résultat attendu

- Le compte est actif et utilisable.
- Le lien d'activation ne peut plus être réutilisé.
- L'activation et l'identité de l'administrateur ayant envoyé l'invitation sont journalisées.

### 4.5 Cas d'erreur

| Situation | Comportement attendu | Code fonctionnel proposé |
|---|---|---|
| Email absent ou invalide | Le formulaire reste ouvert et indique le champ à corriger. | `INVALID_EMAIL` |
| Email déjà associé à un compte | Aucune invitation n'est créée. | `EMAIL_ALREADY_USED` |
| Rôle absent ou inconnu | Aucune invitation n'est créée. | `INVALID_ROLE` |
| Utilisateur non autorisé | L'action est refusée et journalisée. | `FORBIDDEN` |
| Échec d'envoi de l'email | Le système signale l'échec et permet une nouvelle tentative contrôlée. Le compte demeure `INVITED`. | `INVITATION_EMAIL_FAILED` |
| Jeton absent ou invalide | Le formulaire d'activation n'est pas affiché. | `INVALID_INVITATION_TOKEN` |
| Lien expiré | L'activation est refusée et l'utilisateur est invité à demander une nouvelle invitation. | `INVITATION_EXPIRED` |
| Lien déjà utilisé | L'activation est refusée sans modifier le compte. | `INVITATION_ALREADY_USED` |
| Mot de passe insuffisant | Le compte reste `INVITED` et les règles à respecter sont affichées. | `WEAK_PASSWORD` |

### 4.6 Renvoi d'une invitation

Un administrateur peut renvoyer une invitation uniquement si le compte est encore `INVITED`. L'ancien jeton est invalidé, un nouveau délai de 48 heures commence et un nouvel email est envoyé. Un compte `ACTIVE` ou `DISABLED` ne peut pas recevoir une invitation d'activation.

## 5. Parcours de création directe

### 5.1 Décision fonctionnelle

GeoTrack accepte deux modes de création :

- l'invitation, parcours recommandé lorsque l'utilisateur choisit lui-même son mot de passe;
- la création directe par un administrateur, prévue pour les besoins internes autorisés.

Dans le mode direct, le mot de passe initial doit être transmis à l'utilisateur par un canal sécurisé extérieur aux journaux de l'application. Une évolution peut imposer son changement à la première connexion.

### 5.2 Préconditions

- L'administrateur est authentifié et possède `user.create`.
- Si le rôle doit être choisi ou modifié, il possède également `role.assign`.

### 5.3 Formulaire de création

| Champ | Type | Obligatoire | Validation |
|---|---|:---:|---|
| Prénom | Texte | Oui | 1 à 100 caractères. |
| Nom | Texte | Oui | 1 à 100 caractères. |
| Email | Email | Oui | Format valide et valeur unique. |
| Rôle | Liste | Oui | Rôle existant. |
| Mot de passe | Mot de passe | Oui | Respecte les règles communes. |
| Confirmation | Mot de passe | Oui | Identique au mot de passe. |
| Statut initial | Valeur système | Oui | `ACTIVE`. |

### 5.4 Déroulement nominal

1. L'administrateur ouvre « Créer un compte ».
2. Il remplit tous les champs requis.
3. Le système vérifie les permissions, les formats, l'unicité de l'email, le rôle et le mot de passe.
4. Le compte est créé à l'état `ACTIVE`.
5. Les permissions de GTB-96 correspondant au rôle sont associées au compte.
6. Le système confirme la création et journalise l'opération.

### 5.5 Cas d'erreur

| Situation | Comportement attendu | Code fonctionnel proposé |
|---|---|---|
| Champ obligatoire absent | Aucun compte n'est créé et chaque champ concerné est signalé. | `REQUIRED_FIELD_MISSING` |
| Email invalide | Aucun compte n'est créé. | `INVALID_EMAIL` |
| Email déjà utilisé ou invité | Aucun compte n'est créé. | `EMAIL_ALREADY_USED` |
| Mot de passe insuffisant | Aucun compte n'est créé et les critères sont affichés. | `WEAK_PASSWORD` |
| Confirmation différente | Aucun compte n'est créé. | `PASSWORD_CONFIRMATION_MISMATCH` |
| Rôle invalide | Aucun compte n'est créé. | `INVALID_ROLE` |
| Administrateur non autorisé | L'action est refusée et journalisée. | `FORBIDDEN` |
| Erreur interne pendant la création | Aucune création partielle ne doit subsister. | `ACCOUNT_CREATION_FAILED` |

## 6. Parcours de modification

## 6.1 Modification d'un compte par un administrateur

### Préconditions

- L'administrateur est authentifié et possède `user.update`.
- La modification d'un rôle exige aussi `role.assign`.
- Le compte ciblé existe.

### Champs modifiables

| Champ | Administrateur | Règle |
|---|:---:|---|
| Prénom | Oui | 1 à 100 caractères. |
| Nom | Oui | 1 à 100 caractères. |
| Email | Oui | Format valide et valeur unique. Une vérification de la nouvelle adresse pourra être ajoutée ultérieurement. |
| Rôle | Oui | Rôle existant; effet immédiat sur les permissions. |
| Statut | Oui | Passage entre `ACTIVE` et `DISABLED`. |
| Mot de passe | Non dans ce formulaire | Utiliser un parcours distinct de réinitialisation ou de changement de mot de passe. |

### Déroulement nominal

1. L'administrateur consulte la liste des utilisateurs et ouvre un compte.
2. Le système affiche les informations actuelles.
3. L'administrateur modifie un ou plusieurs champs.
4. Le système vérifie ses permissions et valide les nouvelles valeurs.
5. Le système enregistre toutes les modifications dans une opération cohérente.
6. Si le rôle change, les anciennes permissions sont retirées et les nouvelles sont appliquées immédiatement.
7. Si le compte est désactivé, toutes ses sessions sont révoquées.
8. Le système affiche une confirmation et journalise les valeurs modifiées, sans données secrètes.

### Cas d'erreur

| Situation | Comportement attendu | Code fonctionnel proposé |
|---|---|---|
| Compte inexistant | Aucune modification. | `USER_NOT_FOUND` |
| Email déjà utilisé | Aucune modification. | `EMAIL_ALREADY_USED` |
| Valeur invalide | Aucune modification et affichage des champs en erreur. | `VALIDATION_ERROR` |
| Rôle inconnu | Aucune modification. | `INVALID_ROLE` |
| Permission `role.assign` absente | Le rôle reste inchangé. | `FORBIDDEN_ROLE_CHANGE` |
| Action d'administration non autorisée | L'action est refusée et journalisée. | `FORBIDDEN` |
| Modification concurrente | L'utilisateur doit actualiser les données avant de recommencer. | `ACCOUNT_ALREADY_MODIFIED` |
| Dernier administrateur actif désactivé ou privé du rôle Administrateur | L'opération est refusée pour éviter de rendre l'administration inaccessible. | `LAST_ACTIVE_ADMIN_REQUIRED` |

## 6.2 Modification du profil par l'utilisateur

### Champs modifiables

| Champ | Utilisateur | Règle |
|---|:---:|---|
| Prénom | Oui | 1 à 100 caractères. |
| Nom | Oui | 1 à 100 caractères. |
| Mot de passe | Oui | Mot de passe actuel requis, puis nouveau mot de passe conforme et confirmation. |
| Email | Non dans ce parcours | Modification réservée à l'administrateur dans la portée de GTB-98. |
| Rôle | Non | Toute tentative est refusée. |
| Statut | Non | Toute tentative est refusée. |

### Déroulement nominal

1. L'utilisateur authentifié ouvre « Mon profil ».
2. Il modifie son nom ou son prénom, ou choisit le formulaire de changement du mot de passe.
3. Pour un changement de mot de passe, il saisit son mot de passe actuel, le nouveau et sa confirmation.
4. Le système valide les champs et l'identité de l'utilisateur.
5. Les nouvelles données sont enregistrées.
6. Après un changement de mot de passe, les autres sessions actives sont révoquées.
7. Le système confirme la modification et la journalise.

### Cas d'erreur

| Situation | Comportement attendu | Code fonctionnel proposé |
|---|---|---|
| Mot de passe actuel incorrect | Aucun changement. | `CURRENT_PASSWORD_INVALID` |
| Nouveau mot de passe insuffisant | Aucun changement et affichage des critères. | `WEAK_PASSWORD` |
| Confirmation différente | Aucun changement. | `PASSWORD_CONFIRMATION_MISMATCH` |
| Tentative de modifier le rôle ou le statut | L'action est refusée et journalisée. | `FORBIDDEN_FIELD` |
| Session expirée ou compte désactivé | L'utilisateur doit se reconnecter ou contacter un administrateur. | `UNAUTHORIZED` |

## 7. Endpoints fonctionnels proposés

Les chemins suivants décrivent les services attendus. Leur forme exacte peut être adaptée à l'architecture du projet, mais les contrôles fonctionnels doivent être conservés.

| Méthode et endpoint | Fonction | Permission requise | Résultat principal |
|---|---|---|---|
| `POST /api/admin/invitations` | Envoyer une invitation | `user.create` et `role.assign` | Invitation créée, réponse `201`. |
| `POST /api/admin/invitations/{userId}/resend` | Renvoyer une invitation | `user.create` | Nouveau jeton créé, réponse `200`. |
| `GET /api/invitations/{token}` | Vérifier un lien d'activation | Jeton valide | Informations non sensibles de l'invitation, réponse `200`. |
| `POST /api/invitations/{token}/activate` | Finaliser un compte invité | Jeton valide | Compte activé, réponse `200`. |
| `POST /api/admin/users` | Créer directement un compte | `user.create` et `role.assign` | Compte créé, réponse `201`. |
| `PATCH /api/admin/users/{userId}` | Modifier un compte, son rôle ou son statut | `user.update`; `role.assign` si rôle modifié | Compte mis à jour, réponse `200`. |
| `PATCH /api/me/profile` | Modifier son nom ou son prénom | Utilisateur authentifié | Profil mis à jour, réponse `200`. |
| `PUT /api/me/password` | Changer son mot de passe | Utilisateur authentifié | Mot de passe modifié, réponse `204`. |

### 7.1 Structure minimale des requêtes

#### Invitation

```json
{
  "email": "utilisateur@exemple.ca",
  "role": "OPERATEUR"
}
```

#### Activation

```json
{
  "firstName": "Amina",
  "lastName": "Diallo",
  "password": "MotDePasseSecurise!2026",
  "passwordConfirmation": "MotDePasseSecurise!2026"
}
```

#### Création directe

```json
{
  "firstName": "Amina",
  "lastName": "Diallo",
  "email": "utilisateur@exemple.ca",
  "role": "GESTIONNAIRE_FLOTTE",
  "password": "MotDePasseSecurise!2026",
  "passwordConfirmation": "MotDePasseSecurise!2026"
}
```

#### Modification par un administrateur

```json
{
  "firstName": "Amina",
  "lastName": "Diallo",
  "role": "OPERATEUR",
  "status": "ACTIVE"
}
```

Seuls les champs présents sont modifiés. Les champs non autorisés ou inconnus sont rejetés plutôt qu'ignorés silencieusement.

## 8. Journalisation et traçabilité

Les événements suivants doivent être enregistrés avec la date, l'auteur, le compte visé, l'action et le résultat :

- invitation envoyée ou renvoyée;
- activation réussie ou refusée;
- création directe d'un compte;
- modification des informations d'un compte;
- changement de rôle avec ancien et nouveau rôle;
- activation ou désactivation d'un compte;
- changement de mot de passe, sans enregistrer les mots de passe;
- tentative d'action interdite.

Les jetons d'invitation, mots de passe et secrets ne doivent jamais apparaître dans les journaux.

## 9. Règles d'interface

1. Les champs obligatoires sont identifiés avant la soumission.
2. Les erreurs sont affichées près des champs concernés et un résumé indique pourquoi l'opération a échoué.
3. Un bouton de soumission est désactivé pendant le traitement afin d'éviter les doubles créations.
4. Une confirmation explicite est demandée avant la désactivation d'un compte ou la réduction de ses privilèges.
5. Les écrans et boutons d'administration ne sont visibles que pour les administrateurs, sans remplacer les contrôles côté serveur.
6. Après une réussite, l'interface affiche une confirmation claire et l'état actualisé du compte.

## 10. Scénarios de validation fonctionnelle

| ID | Scénario | Résultat attendu |
|---|---|---|
| INV-01 | Un administrateur invite une adresse inutilisée avec un rôle valide. | Compte `INVITED`, email envoyé et jeton valable 48 heures. |
| INV-02 | Une invitation est demandée pour un email déjà utilisé. | Refus `EMAIL_ALREADY_USED`; aucun doublon. |
| INV-03 | Un invité active son compte avec un lien valide. | Compte `ACTIVE`; lien invalidé; permissions du rôle appliquées. |
| INV-04 | Un invité ouvre un lien expiré ou déjà utilisé. | Activation refusée avec le message approprié. |
| CRE-01 | Un administrateur crée directement un compte valide. | Compte `ACTIVE`; permissions affectées; opération auditée. |
| CRE-02 | Le mot de passe ne respecte pas les règles. | Création refusée; aucune donnée partielle. |
| MOD-01 | Un administrateur change le rôle d'un utilisateur. | Nouvelles permissions applicables immédiatement. |
| MOD-02 | Un administrateur désactive un compte actif. | Connexion bloquée et sessions révoquées. |
| MOD-03 | Un opérateur tente de changer son rôle. | Refus `FORBIDDEN_FIELD`; tentative auditée. |
| MOD-04 | Un utilisateur change correctement son mot de passe. | Mot de passe remplacé et autres sessions révoquées. |
| MOD-05 | Une opération tente de désactiver le dernier administrateur actif. | Refus `LAST_ACTIVE_ADMIN_REQUIRED`. |

## 11. Vérification des critères d'acceptation

| Critère de GTB-98 | Réponse apportée |
|---|---|
| Les trois parcours sont documentés. | Les sections 4, 5 et 6 décrivent l'invitation, la création directe et les deux formes de modification. |
| Les étapes, champs et validations sont précisés. | Chaque parcours contient ses préconditions, son formulaire, son déroulement et ses règles. |
| Les erreurs principales sont identifiées. | Chaque parcours possède un tableau d'erreurs et des codes fonctionnels proposés. |
| Les règles suivent GTB-96. | Les opérations d'administration exigent `user.create`, `user.update` et `role.assign`; les autres rôles ne peuvent pas administrer les comptes. |
| Le document est utilisable en développement. | Les états, règles, endpoints, exemples de requêtes, événements d'audit et scénarios de validation sont définis. |
| Le moindre privilège est appliqué. | Les champs et actions non autorisés sont refusés et contrôlés côté serveur. |

## 12. Points à valider par l'équipe

- Confirmer que la création directe reste autorisée en plus du parcours d'invitation.
- Confirmer le délai de validité de 48 heures pour une invitation.
- Confirmer les règles minimales du mot de passe.
- Confirmer que seul l'administrateur peut modifier l'adresse email d'un compte.
- Confirmer la protection empêchant la désactivation du dernier administrateur actif.

## 13. Décision de l'équipe

- Date de validation : à compléter.
- Participants : à compléter.
- Décision : à compléter (`approuvée`, `approuvée avec modifications` ou `refusée`).
- Commentaires : à compléter.
