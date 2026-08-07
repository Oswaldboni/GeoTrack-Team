# US-08.1 — Analyse des besoins de stockage sur 2 ans

## Objectif

Estimer le volume de données de télémétrie généré par la flotte GeoTrack afin de déterminer les besoins de stockage à long terme.

## Données de départ

Le système GeoTrack doit gérer :

- 10 000 véhicules ;
- un message de télémétrie toutes les 5 secondes par véhicule ;
- un fonctionnement 24 h/24 et 7 j/7 ;
- une conservation des données pendant 2 ans.

La taille exacte d'un message de télémétrie n'étant pas définie, une hypothèse de dimensionnement est utilisée pour réaliser l'estimation.

## Hypothèse sur la taille d'un message

La taille moyenne d'un message de télémétrie est estimée à :

**300 octets par message**

Cette estimation prend en compte les principales informations d'un message :

- identifiant du véhicule ;
- latitude ;
- longitude ;
- vitesse ;
- direction ;
- horodatage ;
- état du véhicule ;
- informations de diagnostic.

Cette valeur constitue une hypothèse de dimensionnement et pourra être ajustée après mesure de la taille réelle des messages.

## Calcul du nombre de messages

### Messages par seconde

10 000 / 5 = **2 000 messages par seconde**

### Messages par minute

2 000 × 60 = **120 000 messages par minute**

### Messages par heure

120 000 × 60 = **7 200 000 messages par heure**

### Messages par jour

7 200 000 × 24 = **172 800 000 messages par jour**

### Messages par année

172 800 000 × 365 = **63 072 000 000 messages par année**

### Messages sur deux ans

63 072 000 000 × 2 = **126 144 000 000 messages**

## Volume brut estimé

126 144 000 000 messages × 300 octets

= **37 843 200 000 000 octets**

Soit environ :

**37,84 To de données brutes sur deux ans**

## Capacité de stockage recommandée

Le volume brut calculé ne prend pas en compte :

- les index ;
- les métadonnées ;
- les structures internes de la base de données ;
- les sauvegardes ;
- la réplication ;
- la marge de croissance.

Pour le dimensionnement initial, une capacité d'environ **50 To de stockage primaire utile** peut donc être envisagée.

Si une stratégie de réplication est utilisée, la capacité physique nécessaire sera supérieure. Par exemple, trois copies complètes des données pourraient nécessiter jusqu'à environ **150 To de capacité physique**, avant optimisation.

## Limites de l'estimation

Cette estimation suppose :

- que les 10 000 véhicules transmettent continuellement ;
- qu'un message est envoyé toutes les 5 secondes sans interruption ;
- qu'une année contient 365 jours ;
- que la taille moyenne reste proche de 300 octets ;
- qu'aucune compression ni agrégation n'est appliquée au volume brut.

Le volume réel pourra donc varier selon le format définitif des messages, la base de données choisie et la stratégie de compression et d'archivage.

## Conclusion

GeoTrack pourrait produire environ **126,144 milliards de messages de télémétrie sur deux ans**, représentant environ **37,84 To de données brutes** selon l'hypothèse retenue.

Ce volume justifie une architecture de stockage adaptée aux données temporelles et géospatiales ainsi qu'une stratégie de hiérarchisation, de compression et d'archivage des données anciennes.
