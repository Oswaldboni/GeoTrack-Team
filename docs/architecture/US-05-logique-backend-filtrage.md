# US-05 — Logique backend de filtrage des véhicules

## Sous-tâche associée

**GTB-95 — Spécifier la logique de requête côté backend pour filtrer dynamiquement les données transmises à l’affichage**

## Objectif

Spécifier la logique backend permettant de filtrer dynamiquement les véhicules retournés à l’interface GeoTrack selon les critères définis dans GTB-93.

Les filtres principaux sont :

- zone géographique ;
- statut actif ou inactif ;
- recherche par identifiant du véhicule.

Cette logique doit permettre à l’interface de la carte interactive de recevoir uniquement les véhicules correspondant aux critères sélectionnés par le gestionnaire.

## Contexte

Cette sous-tâche complète :

- **GTB-93**, qui définit les critères de filtrage ;
- **GTB-94**, qui définit l’ergonomie et les composants UI associés aux filtres.

GTB-95 décrit la manière dont le backend reçoit les paramètres de filtrage, applique les règles correspondantes et retourne les résultats à l’interface.

## Endpoint proposé

L’API peut exposer l’endpoint suivant :

```http
GET /api/vehicules?zoneId={id}&statut={actif|inactif}&recherche={texte}
