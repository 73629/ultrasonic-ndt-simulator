# Simulation d'un contrôle non destructif par ultrasons

## Description

Ce projet est une simulation simplifié d'un contrôle non destructif par ultrason de type A-Scan
dans un bloc d'acier contenant un défaut interne.

## Modèle physique et équations utilisées

### Paramètres de l'onde, du bloc et du défaut

Le bloc et le défaut :
* on ne considère que la profondeur
* Le bloc d'acier est parfaitement homogène à part pour le défaut
* Le bloc a une épaisseur de 50 mm, et le défaut est situé à 30 mm sous le palpeur
* Le défaut a une coefficient de réflexion de 0.5 et un coeff. de transmission de 0.5
* Le fond du bloc à un coefficient de réflexion de 0.95

L'onde :
* Fréquence de 2 MHz
* longitudinale
* vitesse longitudianale dans l'acier de 5900 m/s
* L'écho de fond ne repasse pas sur le défaut
* L'amplitude initiale de l'onde est de 1

### Atténuation acoustique

L'atténuation de l'amplitude de l'onde acoustique est décrite par l'équation suivante :

$$A = A_0 e^{-\alpha d}$$

**Avec :**
* $A_0$ : Amplitude initiale de l'onde .
* $A$ : Amplitude de l'onde après avoir parcouru une distance $d$.
* $d$ : Distance parcourue.
* $\alpha$ : Coefficient d'atténuation qui dépend du matériau et de la fréquence de l'onde, en (Np/m). Pour une onde de 2 MHz, 
             le $\alpha$ de l'acier peut varier de 5 à 50 dB/m. J'ai choisi 40 dB/m, ce qui correspond environ à 4.6 Np/m  


### Temps de vol 
la formule décrivant le temps de vol est :

$$t = \frac{v_L p}{2}$$

**Avec :**
* $t$ = temps entre l'émission de l'onde sa réception par le palpeur
* $v_L$ = vitesse longitudinale de l'onde 
* $p$ = profondeur que l'onde a atteinte avant d'être réfléchie

### coefficients de réflexion et de transmission

$$R = \frac{A_r}{A_i}$$ et $$T = \frac{A_t}{A_i}$$

**Avec :**
* $R$ = coefficient de réflexion
* $T$ = coefficient de réflexion
* $A_i$ = amplitude de l'onde incidente
* $A_r$ = amplitude de l'onde réfléchie 
* $A_t$ = amplitude de l'onde transmise

## Résultat

![Résultat](ascan.png)

Essai

## Technologies

- Python
- NumPy
- Matplotlib

## Lancer le projet

pip install -r requirements.txt

python simulation.py

