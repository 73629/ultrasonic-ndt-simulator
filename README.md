# Simulation d'un contrôle non destructif par ultrasons

## Description

Ce projet est une simulation simplifié d'un contrôle non destructif par ultrason de type A-Scan
dans un bloc d'acier contenant un défaut interne.

## simplification du modèle physique et équations utilisées

## Formule de l'atténuation acoustique

L'atténuation de l'amplitude de l'onde acoustique est régie par l'équation suivante :

$$A = A_0 \times e^{-\alpha \times d}$$

**Avec :**
* $A_0$ : Amplitude de l'onde émise.
* $A$ : Amplitude de l'onde qui a parcouru la distance $d$.
* $d$ : Distance parcourue.
* $\alpha$ : Coefficient dépendant du matériau et de la fréquence au carré, défini par :

$$\alpha = k \times f^2$$ 

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

