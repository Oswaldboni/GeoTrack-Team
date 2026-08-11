# GeoTrack Team

Projet GEN1423 — conception et architecture du système de suivi de flotte GeoTrack.

## Objectif

GeoTrack est conçu pour suivre jusqu'à 10 000 véhicules transmettant une télémétrie toutes les 5 secondes. Le dépôt documente l'ingestion, l'affichage presque en temps réel, les alertes, l'historique sur deux ans, la sécurité, la résilience et l'observabilité.

## Repères de dimensionnement

| Indicateur | Valeur de référence |
|---|---:|
| Véhicules | 10 000 |
| Intervalle d'émission | 5 s |
| Débit nominal | 2 000 messages/s |
| Messages sur deux ans | 126 144 000 000 |
| Hypothèse par message | 300 octets |
| Volume brut sur deux ans | 37,84 To |

## Arborescence

| Dossier | Contenu |
|---|---|
| [`calculations/`](calculations/) | Débit et capacité de stockage |
| [`diagrams/`](diagrams/) | Diagrammes et exports visuels |
| [`docs/analyse/`](docs/analyse/) | Besoins, KPI et règles métier |
| [`docs/architecture/`](docs/architecture/) | Ingestion, temps réel, résilience et observabilité |
| [`docs/donnees/`](docs/donnees/) | Modèles, index et rétention |
| [`docs/maquettes/`](docs/maquettes/) | Interface principale |
| [`docs/risques/`](docs/risques/) | Registre des risques |
| [`docs/securite/`](docs/securite/) | Authentification et chiffrement |
| [`docs/tests/`](docs/tests/) | Stratégie de validation |
| [`figma/`](figma/) | Export du tableau de bord analytique |
| [`rapport/`](rapport/) | Éléments du rapport final |
| [`schemas/`](schemas/) | Contrat JSON de télémétrie |
| [`simulations/`](simulations/) | Simulateur de télémétrie |

## Exécution du simulateur

```bash
python3 simulations/telemetry/simulate_telemetry.py --cycles 1 --seed 42
```

Consultez [`simulations/README.md`](simulations/README.md) pour les paramètres.

## État de la documentation

Les documents existants des US-01, US-02, US-03, US-04, US-06, US-07, US-08, US-09, US-10, US-11, US-13, US-14 et US-15 sont présents. Les US-05 et US-12 ne figurent pas dans l'archive et doivent être comparées au Backlog Jira avant la remise.

Le rapport d'audit du 10 août 2026 se trouve dans [`AUDIT-2026-08-10.md`](AUDIT-2026-08-10.md).
