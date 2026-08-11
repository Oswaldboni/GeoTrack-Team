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
```

Les valeurs dynamiques doivent être échappées avant leur insertion dans le HTML afin d'éviter qu'une donnée reçue soit interprétée comme du code.

## Synchronisation avec la liste

L'application conserve un identifiant de sélection unique. Un clic sur un marqueur ou sur une ligne de la liste met à jour ce même état, centre la carte si nécessaire et applique le style de sélection aux deux représentations.

Lorsqu'une nouvelle télémétrie arrive pour le véhicule sélectionné, le popup est mis à jour sans être fermé ni recréé inutilement.

## Cas particuliers

- Si le véhicule n'a jamais envoyé de position, la carte affiche un état « position inconnue ».
- Si la dernière position est ancienne, son âge est affiché visiblement.
- Si le véhicule disparaît du filtre courant, la sélection est réinitialisée.
- Si le chargement des détails échoue, un message court permet de réessayer sans bloquer la carte.

## Accessibilité

La couleur ne doit pas être le seul moyen de distinguer les statuts. Les marqueurs et lignes doivent inclure un libellé lisible, être utilisables au clavier et conserver un contraste suffisant.

## Critères de validation

- Le clic sur un marqueur affiche le bon véhicule.
- La ligne correspondante est mise en évidence et la sélection est réciproque.
- Les données dynamiques ne peuvent pas injecter de HTML ou de script.
- L'âge d'une position périmée est visible.
- La fonctionnalité reste utilisable au clavier.

## Conclusion

Le popup, la liste et la carte reposent sur un état de sélection commun. Cette approche évite les incohérences et maintient les détails à jour lors de la réception de nouvelles positions.
