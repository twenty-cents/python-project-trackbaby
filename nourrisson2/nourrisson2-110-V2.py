#######################################################################################
# Nom du script : nourrisson2-110-V2.py
# Version       : 1.0
# Créé le       : 03/10/19 par Vincent 
# 
#######################################################################################
# Version 110 lignes propre
#
#######################################################################################
# matplotlib pour réaliser les graphiques
import matplotlib.pyplot as plt
import numpy as np
# csv pour lire les fichiers de données
import csv
# Tables des mesures
mesures_age = []
mesures_poids = []
mesures_taille = []
mesures_perimetre_cranien = []
# Tables de travail
p05 = []
p25 = []
p50 = []
p75 = []
p95 = []

# Genre à renseigner
genre = "fille"

# ------------------------------------------------------------------------------------------------
# Fonctions du script
# ------------------------------------------------------------------------------------------------
# Ajouter un graphe
def ajouter_graphe(ax, fichier, legend):
    # Ràz des tables de travail
    p05.clear()
    p25.clear()
    p50.clear()
    p75.clear()
    p95.clear()

    # Extration des données
    with open(fichier, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            p05.append(float(row['P5']))
            p25.append(float(row['P25']))
            p50.append(float(row['P50']))
            p75.append(float(row['P75']))
            p95.append(float(row['P95']))
    
    ax.plot(p05, label=f'5% {legend}')
    ax.plot(p25, label=f'25% {legend}')
    ax.plot(p50, label=f'50% {legend}')
    ax.plot(p75, label=f'75% {legend}')
    ax.plot(p95, label=f'95% {legend}')

# ------------------------------------------------------------------------------------------------
# Point d'entrée du script
# ------------------------------------------------------------------------------------------------
# Récupération des mesures dans les fichiers à faire
with open('./nourrisson2/mesures.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        mesures_age.append(int(row['Mois']))
        mesures_poids.append(float(row['Poids']))
        mesures_taille.append(float(row['Taille']))
        mesures_perimetre_cranien.append(float(row['Périmètre crânien']))

# Affichage des graphiques à faire
fig = plt.figure()
ax1 = fig.add_subplot(131)
plt.xlabel('Age en mois')
plt.ylabel('Poids en kg')
plt.grid(True)
ax2 = fig.add_subplot(132)
plt.xlabel('Age en mois')
plt.ylabel('Taille en cm')
plt.grid(True)
ax3 = fig.add_subplot(133)
plt.xlabel('Age en mois')
plt.ylabel('Périmètre cranien en cm')
plt.grid(True)

# Extraction des constantes de poids
ajouter_graphe(ax1, f'./nourrisson2/constantes-nourrissons/poids-age-{genre}-0-60.csv', 'Poids')
# Extraction des constantes de taille
ajouter_graphe(ax2, f'./nourrisson2/constantes-nourrissons/taille-age-{genre}-0-60.csv', 'Taille')
# Extraction des constantes de périmètre crânien
ajouter_graphe(ax3, f'./nourrisson2/constantes-nourrissons/perim-cra-age-{genre}-0-60.csv', 'Périmètre cranien')

# Ajout des mesures
ax1.scatter(mesures_age, mesures_poids)
ax2.scatter(mesures_age, mesures_taille)
ax3.scatter(mesures_age, mesures_perimetre_cranien)

# Positionnement des légendes
ax1.legend()
leg = ax1.legend(loc=2, ncol=1, prop={'size':10})
leg.get_frame().set_alpha(0.4)

ax2.legend()
leg = ax2.legend(loc=2, ncol=1, prop={'size':10})
leg.get_frame().set_alpha(0.4)

ax3.legend()
leg = ax3.legend(loc=4, ncol=1, prop={'size':10})
leg.get_frame().set_alpha(0.4)
# Affichage des figures statistiques
plt.show()