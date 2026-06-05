# Simulation d'un contrôle non destructif par ultrasons

## Description

Ce projet est une simulation simplifié d'un contrôle non destructif par ultrason de type A-Scan
dans un bloc d'acier contenant un défaut interne.

## Modèle physique et équations utilisées

# Formule de l'atténuation acoustique

L'atténuation de l'amplitude de l'onde acoustique est décrite par l'équation suivante :

$$A = A_0 e^{-\alpha d}$$

**Avec :**
* $A_0$ : Amplitude initiale de l'onde .
* $A$ : Amplitude de l'onde après avoir parcouru une distance $d$.
* $d$ : Distance parcourue.
* $\alpha$ : Coefficient d'atténuation qui dépend du matériau et de la fréquence de l'onde. Pour une onde de 2 MHz, 
             le $\alpha$ de l'acier peut varier de 5 à 50 dB/m. J'ai choisi 40 dB/m.  


Temps de vol :

t = 2d / v

Atténuation :

A = A0 exp(-αd)

## Résultat

![Résultat](ascan.png)

## Technologies

- Python
- NumPy
- Matplotlib

## Lancer le projet

pip install -r requirements.txt

python simulation.py

