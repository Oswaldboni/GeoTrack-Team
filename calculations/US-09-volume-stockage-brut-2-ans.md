# US-09.1 — Calcul du volume de stockage brut sur 2 ans

## Objectif

Calculer le volume de stockage brut nécessaire pour conserver deux années de données de télémétrie générées par la flotte GeoTrack.

## Données de départ

- 10 000 véhicules ;
- un message toutes les 5 secondes par véhicule ;
- fonctionnement 24 h/24 et 7 j/7 ;
- conservation pendant 2 ans.

La taille moyenne d'un message n'étant pas fournie dans l'énoncé, une hypothèse de dimensionnement est nécessaire.

## Hypothèse

La taille moyenne d'un message de télémétrie est estimée à :

**300 octets par message**

Cette hypothèse représente notamment :

- identifiant du véhicule ;
- coordonnées GPS ;
- vitesse ;
- direction ;
- horodatage ;
- état du véhicule ;
- informations de diagnostic.

## Calcul du nombre de messages

### Par seconde

10 000 / 5 = **2 000 messages par seconde**

### Par minute

2 000 × 60 = **120 000 messages**

### Par heure

120 000 × 60 = **7 200 000 messages**

### Par jour

7 200 000 × 24 = **172 800 000 messages**

### Par année

172 800 000 × 365 = **63 072 000 000 messages**

### Sur deux ans

63 072 000 000 × 2 = **126 144 000 000 messages**

## Calcul du volume brut

126 144 000 000 × 300 octets

= **37 843 200 000 000 octets**

Soit environ :

**37,84 To de données brutes**

## Limites du calcul

Ce volume représente uniquement les données brutes de télémétrie.

Il ne comprend pas :

- les index ;
- les métadonnées ;
- les sauvegardes ;
- la réplication ;
- les structures internes de la base de données ;
- les marges de croissance.

## Conclusion

Avec l'hypothèse de 300 octets par message, GeoTrack doit prévoir environ **37,84 To de stockage brut** pour conserver deux années de télémétrie de 10 000 véhicules.

Cette estimation servira de base à la définition de la stratégie de rétention, de hiérarchisation et d'archivage des données.
