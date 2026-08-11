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
```

L'alerte doit aussi conserver un identifiant d'événement source et la position ayant déclenché le franchissement. Ces données permettent la déduplication et l'audit.

## 3. Chaîne de notification

1. Le service de geofencing publie l'événement d'entrée ou de sortie.
2. Le service d'alertes vérifie qu'il n'a pas déjà traité cet identifiant.
3. Il enregistre l'alerte avec le statut `NON_LUE`.
4. Il la diffuse au tableau de bord par le canal temps réel.
5. Le gestionnaire peut la marquer comme lue ou traitée.

## 4. Délai

Le délai est mesuré entre l'horodatage du franchissement détecté et la réception par le tableau de bord. La cible d'acceptation est inférieure à 60 secondes au percentile 95 sous charge nominale.

## 5. Déduplication et bruit

Un même événement ne doit créer qu'une alerte, même s'il est retransmis. Les oscillations GPS près de la frontière sont traitées par les règles de stabilité définies dans US-06.2 avant la création de l'événement.

## 6. Traçabilité

Le système conserve la zone, le véhicule, le type de franchissement, l'heure de détection, l'heure de notification, le destinataire et les changements de statut. Une alerte ne doit pas être supprimée par le simple fait d'être marquée comme lue.

## Critères de validation

- Une entrée et une sortie valides produisent chacune une alerte distincte.
- Une retransmission du même événement ne produit pas de doublon.
- L'alerte est visible en moins de 60 secondes au percentile 95.
- Seuls les gestionnaires autorisés reçoivent l'information.
- L'état lu ou traité est conservé dans l'historique.

## Conclusion

Le mécanisme sépare la détection géométrique de la notification. L'identifiant d'événement, la mesure du délai et la conservation du cycle de vie rendent les alertes fiables et vérifiables.
