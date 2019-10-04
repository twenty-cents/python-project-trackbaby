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

# Genre à saisir
genre = ""

# ------------------------------------------------------------------------------------------------
# Fonctions du script
# ------------------------------------------------------------------------------------------------
# Sasie du genre
def saisir_genre():
    saisie = ""
    while not (saisie == "f" or saisie == "g"):
        saisie = input("Entrez le genre de votre nourrisson ('g' pour garçon, 'f' pour fille) :")
        if not (saisie == "f" or saisie == "g"):
            print("Saisie incorrecte, essaie encore...")
            saisie = ""
        else:
            if saisie == "g":
                genre = "garcon"
            else:
                genre = "fille"
    return genre

# Extraire les constantes d'un fichier csv
def extraire_constantes(fichier, ):
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
    return

# ------------------------------------------------------------------------------------------------
# Point d'entrée du script
# ------------------------------------------------------------------------------------------------
# Saisie du genre
genre = saisir_genre()

# Extraction des constantes de poids
extraire_constantes(f'./nourrisson2/constantes-nourrissons/poids-age-{genre}-0-60.csv')
poids_05 = list(p05)
poids_25 = list(p25)
poids_50 = list(p50)
poids_75 = list(p75)
poids_95 = list(p95)

# Extraction des constantes de taille
extraire_constantes(f'./nourrisson2/constantes-nourrissons/taille-age-{genre}-0-60.csv')
taille_05 = list(p05)
taille_25 = list(p25)
taille_50 = list(p50)
taille_75 = list(p75)
taille_95 = list(p95)

# Extraction des constantes de périmètre crânien
extraire_constantes(f'./nourrisson2/constantes-nourrissons/perim-cra-age-{genre}-0-60.csv')
perimetre_cranien_05 = list(p05)
perimetre_cranien_25 = list(p25)
perimetre_cranien_50 = list(p50)
perimetre_cranien_75 = list(p75)
perimetre_cranien_95 = list(p95)

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

# Ajout des poids
ax1.plot(poids_05, label='5% poids')
ax1.plot(poids_25, label='25% poids')
ax1.plot(poids_50, label='50% poids')
ax1.plot(poids_75, label='75% poids')
ax1.plot(poids_95, label='95% poids')
ax1.scatter(mesures_age, mesures_poids)

# Ajout des tailles
ax2.plot(taille_05, label='5% taille')
ax2.plot(taille_25, label='25% taille')
ax2.plot(taille_50, label='50% taille')
ax2.plot(taille_75, label='75% taille')
ax2.plot(taille_95, label='95% taille')
ax2.scatter(mesures_age, mesures_taille)

# Ajout des périmètres crâniens
ax3.plot(perimetre_cranien_05, label='5% périmètre cranien')
ax3.plot(perimetre_cranien_25, label='25% périmètre cranien')
ax3.plot(perimetre_cranien_50, label='50% périmètre cranien')
ax3.plot(perimetre_cranien_75, label='75% périmètre cranien')
ax3.plot(perimetre_cranien_95, label='95% périmètre cranien')
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