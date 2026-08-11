# Simulations GeoTrack

Ce dossier contient les scripts et les résultats des expérimentations techniques réalisées dans le cadre du projet GeoTrack.

Il contient actuellement :
- le simulateur de télémétrie des véhicules ;
- les jeux de données utilisés pour les expérimentations ;
- les résultats des simulations de charge ;
- la documentation permettant de reproduire les expérimentations.

## Exécution rapide

Depuis la racine du dépôt :

```bash
python3 simulations/telemetry/simulate_telemetry.py --cycles 1 --seed 42
```

Test cible de génération avec 10 000 véhicules :

```bash
python3 simulations/telemetry/simulate_telemetry.py \
  --vehicles 10000 \
  --cycles 1 \
  --sample-size 5 \
  --seed 42
```

Simulation continue avec un cycle toutes les 5 secondes :

```bash
python3 simulations/telemetry/simulate_telemetry.py --cycles 0 --interval 5
```

Le script mesure la génération locale des messages. Il ne valide pas à lui seul le débit du réseau, du broker ou du stockage.
