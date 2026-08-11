# US-06.2 — Algorithme de détection de franchissement de zones

## Objectif

Définir l'algorithme permettant de déterminer en quasi temps réel si un véhicule se trouve à l'intérieur ou à l'extérieur d'une zone de geofencing, puis de détecter les événements d'entrée et de sortie.

Cette conception s'appuie sur le modèle de zones défini dans US-06.1.

## 1. Cas d'une zone circulaire

Une zone circulaire est définie par :

- un centre ;
- un rayon exprimé en mètres.

Pour déterminer si un véhicule se trouve dans la zone, la distance entre sa position GPS et le centre est calculée.

Pour des coordonnées géographiques, la formule de Haversine peut être utilisée.

La règle est :

```text
distance(position_vehicule, centre_zone) <= rayon
```

## 2. Cas d'une zone polygonale

Pour un polygone, un algorithme point-dans-polygone ou une fonction géospatiale de la base détermine si la position se situe à l'intérieur. Le polygone doit être valide, fermé et contenir au moins trois sommets distincts.

## 3. Détection d'un franchissement

Le système conserve le dernier état connu de chaque paire véhicule-zone.

```text
ancien = EXTERIEUR, nouveau = INTERIEUR  → ZONE_ENTERED
ancien = INTERIEUR, nouveau = EXTERIEUR  → ZONE_EXITED
ancien = nouveau                         → aucun événement
```

La première position initialise l'état sans générer automatiquement un franchissement, sauf règle métier explicite contraire.

## 4. Réduction des faux événements

La précision GPS peut faire osciller une position près de la frontière. Une tolérance spatiale ou la confirmation par deux positions consécutives peut être appliquée. Cette règle doit rester assez courte pour respecter le délai de notification inférieur à une minute.

## 5. Pseudo-algorithme

```text
pour chaque position valide :
  rechercher les zones candidates avec un index géospatial
  pour chaque zone candidate :
    calculer le nouvel état intérieur/extérieur
    comparer avec le dernier état stable
    si la transition est confirmée :
      enregistrer le nouvel état
      publier un événement unique
```

## 6. Cas d'erreur

- Une position invalide est rejetée et journalisée.
- Une zone géométriquement invalide ne peut pas être activée.
- Un événement déjà publié est détecté par son identifiant.
- Une position reçue en retard ne doit pas annuler un état calculé avec une position plus récente.

## Critères de validation

- Les cas intérieur, extérieur et frontière sont testés pour un cercle et un polygone.
- Une entrée et une sortie sont détectées une seule fois.
- Une position ancienne est ignorée.
- Le filtrage spatial évite de tester toutes les zones pour chaque message.
- Le délai complet de notification respecte la cible de US-06.3.

## Conclusion

La détection repose sur un calcul géométrique suivi d'une comparaison d'état. La validation des zones, l'ordre temporel et la stabilisation près des frontières sont nécessaires pour produire des événements fiables.
