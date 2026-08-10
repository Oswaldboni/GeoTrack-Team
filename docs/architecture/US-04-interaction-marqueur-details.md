# US-04.4 — Interaction avec les marqueurs et affichage des détails

## Objectif

Documenter le comportement de l'interface GeoTrack lorsqu'un utilisateur clique sur un marqueur de véhicule sur la carte.

Cette conception correspond à la sous-tâche Jira GTB-56.

## Comportement attendu

Lorsqu'un utilisateur clique sur un marqueur :

1. le marqueur sélectionné ouvre un popup Leaflet ;
2. le popup affiche les principales informations du véhicule ;
3. la ligne correspondante dans la liste latérale est mise en surbrillance ;
4. la carte et la liste restent ainsi visuellement synchronisées.

## Informations affichées

Le popup présente notamment :

- l'identifiant du véhicule ;
- le statut ;
- la vitesse ;
- l'heure de la dernière position connue.

## Création du contenu du popup

Le contenu peut être généré dynamiquement à partir des données du véhicule.

```javascript
function createPopupContent(vehicule) {
  return `
    <div style="font-size:13px; min-width:180px;">
      <div style="font-weight:600; margin-bottom:6px;">
        Véhicule #${vehicule.id}
      </div>

      <div style="color:#5F5E5A; margin-bottom:2px;">
        Statut : ${vehicule.statut}
      </div>

      <div style="color:#5F5E5A; margin-bottom:2px;">
        Vitesse : ${vehicule.vitesse} km/h
      </div>

      <div style="color:#5F5E5A;">
        Dernière position :
        ${vehicule.derniereMaj || 'inconnue'}
      </div>
    </div>
  `;
}
