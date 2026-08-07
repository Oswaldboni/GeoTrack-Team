# US-11 — Spécification du flux d'ajout d'un véhicule

## Objectif

Permettre à un administrateur d'enregistrer un nouveau véhicule dans le système GeoTrack afin qu'il puisse être identifié, configuré et intégré au suivi de la flotte.

## Acteur principal

Administrateur GeoTrack.

## Préconditions

- L'administrateur est authentifié.
- L'administrateur possède les droits nécessaires pour gérer les véhicules.
- Le véhicule n'existe pas déjà dans le système.

## Données à saisir

Lors de l'ajout d'un véhicule, l'administrateur doit pouvoir renseigner notamment :

- l'identifiant du véhicule ;
- la plaque d'immatriculation ;
- le numéro de série du véhicule ;
- le type de véhicule ;
- les capteurs associés ;
- l'état initial du véhicule.

## Parcours principal

1. L'administrateur accède à la section de gestion des véhicules.
2. Il sélectionne l'option permettant d'ajouter un nouveau véhicule.
3. Le système affiche le formulaire d'enregistrement.
4. L'administrateur saisit les informations du véhicule.
5. Le système vérifie la validité des données fournies.
6. Si les informations sont valides, le système enregistre le véhicule.
7. Le système confirme que le véhicule a été ajouté avec succès.
8. Le véhicule devient disponible dans la flotte GeoTrack.

## Cas d'erreur

Le système doit refuser l'enregistrement si :

- des champs obligatoires sont absents ;
- la plaque d'immatriculation existe déjà ;
- le numéro de série existe déjà ;
- les données fournies sont invalides.

Un message d'erreur clair doit être affiché à l'administrateur.

## Résultat attendu

Le nouveau véhicule est enregistré dans GeoTrack et peut ensuite être associé aux données de télémétrie et apparaître dans les fonctionnalités de suivi de la flotte.
