"""
Simulation simplifiée d'un contrôle non destructif (CND)
par une onde ultrasonore longitudinale dans un bloc d'acier.

Fonctionnalités :
- propagation d'une onde ultrasonore de 2 MHz ;
- modulation sinusoïdale par enveloppe gaussienne ;
- atténuation de l'amplitude de l'onde dans l'acier ;
- réflexion sur un défaut interne ;
- réflexion sur le fond de la pièce ;
- génération d'un A-Scan simulé.

Auteur : Nicolas Desnoyers
"""


import numpy as np
import matplotlib.pyplot as plt

# Paramètres du bloc d'acier

vitesse_son = 5900         # m/s (vitesse d'une onde ultrasonique longitudinale dans l'acier)
epaisseur = 50e-3          # 50 mm (épaisseur du bloc d'acier)
profondeur_defaut = 30e-3  # 30 mm (profondeur du défaut dans le bloc d'acier)



# Paramètres du palpeur

frequence = 2e6            # 2 MHz (fréquence de l'onde)
largeur_impulsion = 0.5e-6 # largeur de l'enveloppe gaussienne
A_0 = 1                    # amplitude initiale de l'enveloppe gaussienne



# Coefficient d'atténuation (alpha) :
# Pour une fréquence de 2 MHz, l'acier a un coeff. d'aténuation de 5 à 50 dB/m. On choisit 40 dB/m, puis on convertit en Np/m pour les calculs

alpha_db = 40   # dB/m
alpha = alpha_db/8.686 # Np/m



# Coefficients de réflexion et de transmission

R_defaut = 0.50  # coeff. de réflexion du défaut
T_defaut = 0.50  # coeff. de transmission du défaut
R_fond = 0.95    # coeff. de réflexion du fond



# Temps de vol

t_defaut = 2 * profondeur_defaut / vitesse_son  # Temps de vol de l'onde réfléchie par le défaut
t_fond = 2 * epaisseur / vitesse_son            # Temps de vol de l'onde réfléchie par le fond

print(f"temps de l'écho du défaut : {t_defaut*1e6:.2f} µs")
print(f"temps de l'écho de fond   : {t_fond*1e6:.2f} µs")



# Création du domaine temporel

t = np.linspace(0, 25e-6, 5000)



# Modulation de l'impulsion de l'onde ultrasonore par une gaussienne

def impulsion_us(t, t0, amplitude,
                 frequence=2e6,
                 largeur=0.5e-6):

    enveloppe = np.exp(
        -((t - t0)**2) / (2 * largeur**2)
    )

    porteuse = np.sin(
        2 * np.pi * frequence * (t - t0)
    )

    return amplitude * enveloppe * porteuse



# Atténuation des amplitudes de l'onde réfléchie et de l'onde transmise du défaut

# L'onde perd de l'amplitude en se dirigeant vers le défaut. Son amplitude juste avant de frapper le défaut est A_i :

A_i = A_0 * np.exp(
    -alpha * (profondeur_defaut)
)

# En frappant le défaut, l'amplitude de l'onde réfléchie sur le défaut est diminuée à A_rdefaut :

A_defaut_r = R_defaut*A_i

# En retournant au palpeur, l'onde réfléchie du défaut perd encore de l'amplitude. Son amplitude finale, que le palpeur détecte, est A_defaut :

A_defaut = A_defaut_r * np.exp(
    -alpha * (profondeur_defaut)
)

# L'amplitude de l'onde transmise, juste après le défaut, est A_défaut_t :

A_defaut_t = T_defaut*A_i

# Puis son amplitude continue de diminuer en allant vers le fond.
# Juste avant de toucher le fond, l'amplitude de l'onde transmise est A_fond_i :

A_fond_i = A_defaut_t * np.exp(
    -alpha * (epaisseur-profondeur_defaut)
)

# En touchant le fond, elle est réfléchie, et son amplitude devient A_fond_r :

A_fond_r = R_fond*A_fond_i

# En retournant au palpeur, l'amplitude de l'onde réfléchie du fond diminue encore. Son amplitude finale lue par le palpeur est A_fond :

A_fond = A_fond_r * np.exp(
    -alpha * (epaisseur)
)

print(f"lorsqu'elle revient au palpeur, l'amplitude de l'onde réfléchie par le défaut est : {A_defaut:.2f}")
print(f"lorsqu'elle revient au palpeur, l'amplitude de l'onde réfléchie par le fond est : {A_fond:.2f}")



# Définition du signal reçu par le palpeur

signal = (

    # impulsion émise
    impulsion_us(
        t,
        1e-6,
        amplitude=1.0,
        frequence=frequence,
        largeur=largeur_impulsion
    )

    +

    # écho du défaut
    impulsion_us(
        t,
        t_defaut,
        amplitude=A_defaut,
        frequence=frequence,
        largeur=largeur_impulsion
    )

    +

    # écho du fond
    impulsion_us(
        t,
        t_fond,
        amplitude=A_fond,
        frequence=frequence,
        largeur=largeur_impulsion
    )
)



# Affichage des échos

plt.figure(figsize=(12,6))

plt.plot(
    t*1e6,
    signal,
    linewidth=1.2
)

plt.axvline(
    t_defaut*1e6,
    color='red',
    linestyle='--',
    label=f"Défaut ({profondeur_defaut*1000:.0f} mm)"
)

plt.axvline(
    t_fond*1e6,
    color='green',
    linestyle='--',
    label=f"Fond ({epaisseur*1000:.0f} mm)"
)

plt.xlabel("Temps (µs)")
plt.ylabel("Amplitude")
plt.title("Simulation A-Scan Ultrasonore")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("ascan.png", dpi=300)
plt.show()