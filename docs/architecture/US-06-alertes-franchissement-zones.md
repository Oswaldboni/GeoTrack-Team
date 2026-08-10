# US-06.3 — Génération d'alertes lors d'un franchissement de zone

## Objectif

Définir le mécanisme permettant de générer une alerte destinée aux gestionnaires lorsqu'un véhicule entre dans une zone de geofencing ou en sort.

La contrainte principale est que la notification soit reçue en moins d'une minute après le franchissement détecté.

## 1. Déclenchement

Le mécanisme s'appuie sur les événements générés par le service de détection de franchissement défini dans US-06.2.

Les événements possibles sont notamment :

- `ZONE_ENTERED`
- `ZONE_EXITED`

Lorsqu'un événement est reçu, le service d'alerte crée automatiquement une nouvelle alerte.

## 2. Structure d'une alerte

```text
Alerte {
  id: UUID
  vehiculeId: UUID
  zoneId: UUID
  type: enum("ENTREE", "SORTIE")
  timestamp: datetime
  statut: enum("NON_LUE", "LUE")
  destinataires: [userId]
}
