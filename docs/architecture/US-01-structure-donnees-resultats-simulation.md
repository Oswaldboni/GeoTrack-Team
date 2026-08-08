# US-01.4 — Structure des données et résultats de simulation

## 1. Objectif

Documenter la structure retenue pour les messages de télémétrie GeoTrack et présenter les résultats du script de simulation développé dans le cadre de US-01.

## 2. Structure du message de télémétrie

Les messages de télémétrie utilisent un format JSON standardisé.

Les champs principaux sont :

- `vehicle_id`
- `latitude`
- `longitude`
- `speed_kmh`
- `direction_deg`
- `timestamp`
- `status`
- `diagnostic`

Cette structure permet de représenter les principales données envoyées par chaque véhicule.

## 3. Justification du format JSON

Le format JSON a été retenu pour plusieurs raisons :

- structure simple et lisible ;
- compatibilité avec de nombreux langages et services ;
- facilité de validation à l'aide d'un JSON Schema ;
- facilité de transmission entre composants ;
- adaptation aux échanges de télémétrie.

Le schéma de validation associé est disponible dans :

`schemas/telemetry-message.schema.json`

## 4. Simulation de télémétrie

Un script Python a été développé afin de générer automatiquement des messages de télémétrie.

Le fichier est disponible dans :

`simulations/telemetry/simulate_telemetry.py`

Le simulateur permet de configurer :

- le nombre de véhicules ;
- l'intervalle entre les cycles de génération ;
- les valeurs de position GPS ;
- la vitesse ;
- la direction ;
- l'état du véhicule ;
- certaines informations de diagnostic.

## 5. Configuration initiale du test

La première configuration proposée utilise :

- 100 véhicules simulés ;
- un intervalle de 5 secondes ;
- un message généré pour chaque véhicule à chaque cycle.

Cette configuration permet de vérifier le fonctionnement du simulateur avant d'augmenter progressivement la charge.

## 6. Charge théorique du projet

Le scénario cible de GeoTrack comprend :

- 10 000 véhicules ;
- un message toutes les 5 secondes par véhicule.

La charge théorique est donc :

10 000 / 5 = **2 000 messages par seconde**

Cela représente également :

- 120 000 messages par minute ;
- 7 200 000 messages par heure ;
- 172 800 000 messages par jour.

## 7. Résultats de simulation

Le script affiche pour chaque cycle :

- le nombre de messages générés ;
- quelques exemples de messages JSON ;
- le temps nécessaire pour générer le cycle.

Exemple de résultat attendu avec 100 véhicules :

```text
Cycle 1 : 100 messages générés en X seconde(s)
