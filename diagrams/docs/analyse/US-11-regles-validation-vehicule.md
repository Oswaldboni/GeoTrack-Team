# US-11.3 — Règles de validation des données d'enregistrement d'un véhicule

## Objectif

Définir les règles de validation appliquées lors de l'enregistrement d'un nouveau véhicule dans le système GeoTrack.

## Plaque d'immatriculation

- La plaque d'immatriculation est obligatoire.
- Elle doit respecter le format attendu par le système.
- Elle doit être unique dans GeoTrack.
- Si la plaque existe déjà, l'enregistrement du véhicule doit être refusé.

## Numéro de série

- Le numéro de série du véhicule est obligatoire.
- Il doit être unique dans le système.
- Avant l'enregistrement, GeoTrack doit vérifier qu'aucun autre véhicule n'utilise déjà ce numéro de série.
- En cas de doublon, l'enregistrement doit être refusé.

## Capteurs associés

- Les identifiants des capteurs doivent être valides.
- Les capteurs associés doivent exister dans le système.
- Un capteur déjà affecté à un autre véhicule ne doit pas pouvoir être associé sans modification préalable de son affectation.
- Les capteurs doivent être compatibles avec le type de véhicule lorsqu'une contrainte de compatibilité est définie.

## Validation générale des champs

- Tous les champs obligatoires doivent être renseignés.
- Les données doivent respecter les formats définis.
- Les valeurs incohérentes ou invalides doivent empêcher l'enregistrement.
- Les identifiants techniques doivent respecter les règles d'unicité définies par le système.

## Gestion des erreurs

Lorsqu'une validation échoue :

1. Le système refuse l'enregistrement.
2. Aucune donnée invalide ne doit être enregistrée dans la base de données.
3. Un message d'erreur clair doit indiquer à l'administrateur la donnée à corriger.
4. L'administrateur peut modifier les informations puis soumettre à nouveau le formulaire.

## Résultat attendu

Seuls les véhicules disposant de données valides, cohérentes et respectant les contraintes d'unicité peuvent être enregistrés dans GeoTrack.
