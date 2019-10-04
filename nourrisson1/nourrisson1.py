# Données de références nourrisson
import nourrisson1_donnees

genre_denomination = ""

# ------------------------------------------------------------------------------------------------
# Fonctions du script
# ------------------------------------------------------------------------------------------------
# Tester si une entrée est un float
def is_float_positif(f):
    try:
        n = float(f)
        if n >= 0:
            return True
        else:
            return False
    except:
        return False

# Tester si une entrée est un int
def is_integer_positif(f):
    try:
        n = int(f)
        if n >= 0:
            return True
        else:
            return False
    except:
        return False

# Sasie du genre
def saisir_genre():
    genre = ""
    while not (genre == "f" or genre == "g"):
        genre = input("Entrez le genre de votre nourrisson ('g' pour garçon, 'f' pour fille) :")
        if not (genre == "f" or genre == "g"):
            print("Saisie incorrecte, essaie encore...")
            genre = ""
    return genre

# Sasie de l'âge
def saisir_age():
    age = -1
    while not(is_integer_positif(age) == True):
        age = input("Veuillez entrer l'âge de votre nourrisson en mois (entre 0 et 60 mois) : ")
        if is_integer_positif(age) == False or (is_integer_positif(age) == True and int(age) > 60):
            print("Saisie incorrecte, essaie encore...")
            age = -1
        else:
            age = int(age)
    return age

# Saisir le poids
def saisir_poids():
    poids = -1
    while is_float_positif(poids) == False:
        poids = input("Veuillez entrer le poids de votre nourrisson en kg : ")
        if is_float_positif(poids) == False:
            print("Saisie incorrecte, essaie encore...")
            poids = -1
        else:
            poids = float(poids)
    return poids

# Saisir la taille
def saisir_taille():
    taille = -1
    while is_float_positif(taille) == False:
        taille = input("Veuillez entrer la taille de votre nourrisson en cm : ")
        if is_float_positif(taille) == False:
            print("Saisie incorrecte, essaie encore...")
            taille = -1
        else:
            taille = float(taille)
    return taille

# Saisir le périmètre cranien
def saisir_perimetre_cranien():
    perimetre_cranien = -1
    while is_float_positif(perimetre_cranien) == False:
        perimetre_cranien = input("Veuillez entrer le périmètre cranien de votre nourrisson en cm : ")
        if is_float_positif(perimetre_cranien) == False:
            print("Saisie incorrecte, essaie encore...")
            perimetre_cranien = -1
        else:
            perimetre_cranien = float(perimetre_cranien)
    return perimetre_cranien

# Récupérer le poids minimum selon le genre
def recupere_poids_min(genre, age):
    global nourrisson1_donnees

    if genre == 'g':
        return nourrisson1_donnees.low_weights_boys[age]
    else:
        return nourrisson1_donnees.low_weights_girls[age]

# Récupérer le poids maximum selon le genre
def recupere_poids_max(genre, age):
    global nourrisson1_donnees

    if genre == 'g':
        return nourrisson1_donnees.high_weights_boys[age]
    else:
        return nourrisson1_donnees.high_weights_girls[age]

# Récupérer la taille minimume selon le genre
def recupere_taille_min(genre, age):
    global nourrisson1_donnees

    if genre == 'g':
        return nourrisson1_donnees.low_heights_boys[age]
    else:
        return nourrisson1_donnees.low_heights_girls[age]

# Récupérer la taille minimume selon le genre
def recupere_taille_max(genre, age):
    global nourrisson1_donnees

    if genre == 'g':
        return nourrisson1_donnees.high_heights_boys[age]
    else:
        return nourrisson1_donnees.high_heights_girls[age]

# Récupérer le périmètre cranien minimum selon le genre et l'âge
def recupere_perimetre_cranien_minimum(genre, age):
    global nourrisson1_donnees

    if genre == 'g':
        return nourrisson1_donnees.low_skulls_boys[age]
    else:
        return nourrisson1_donnees.low_skulls_girls[age]

# Récupérer le périmètre cranien minimum selon le genre et l'âge
def recupere_perimetre_cranien_maximum(genre, age):
    global nourrisson1_donnees

    if genre == 'g':
        return nourrisson1_donnees.high_skulls_boys[age]
    else:
        return nourrisson1_donnees.high_skulls_girls[age]

# Récupérer la dénomination du genre
def recuperer_genre_denomination(genre):            
    if genre == "g":
        genre_denomination = "un garçon"
    else:
        genre_denomination = "une fille"
    return genre_denomination

# Afficher le résultat de l'analyse du poids
def affiche_rapport_poids(genre, age, poids, poids_min, poids_max):
    print(f"\nLa norme de poids pour {recuperer_genre_denomination(genre)} de {age} mois est située entre {poids_min} kg et {poids_max} kg")
    if poids >= poids_min and poids <= poids_max:
        print(f"Le poids de votre nourrisson ({poids} kg) est dans la norme !")
    else:
        print(f"Le poids de votre nourrisson ({poids} kg) n'est pas dans la norme !")
    return

# Afficher le résultat de l'analyse de la taille
def affiche_rapport_taille(genre, age, taille, taille_min, taille_max):
    print(f"\nLa norme de taille pour {recuperer_genre_denomination(genre)} de {age} mois est située entre {taille_min} cm et {taille_max} cm")
    if taille >= taille_min and taille <= taille_max:
        print(f"La taille de votre nourrisson ({taille} cm) est dans la norme !")
    else:
        print(f"La taille de votre nourrisson ({taille} cm) n'est pas dans la norme !")
    return

# Afficher le résultat de l'analyse du périmètre cranien
def affiche_rapport_perimetre_cranien(genre, age, perimetre_cranien, perimetre_cranien_min, perimetre_cranien_max):
    print(f"\nLa norme de périmètre cranien pour {recuperer_genre_denomination(genre)} de {age} mois est située entre {perimetre_cranien_min} cm et {perimetre_cranien_max} cm")
    if perimetre_cranien >= perimetre_cranien_min and perimetre_cranien <= perimetre_cranien_max:
        print(f"Le périmètre cranien de votre nourrisson ({perimetre_cranien} cm) est dans la norme !")
    else:
        print(f"Le périmètre cranien de votre nourrisson ({perimetre_cranien} cm) n'est pas dans la norme !")
    return


# ------------------------------------------------------------------------------------------------
# Point d'entrée du script
# ------------------------------------------------------------------------------------------------
print("Bienvenue dans ce programme de vérification des constantes de votre nourrisson !")
# Saisie des entrées clavier
genre             = saisir_genre()
age               = saisir_age()
poids             = saisir_poids()
taille            = saisir_taille()
perimetre_cranien = saisir_perimetre_cranien()

# récupération des bornes selon le genre et l'âge
poids_min             = recupere_poids_min(genre, age)
poids_max             = recupere_poids_max(genre, age)
taille_min            = recupere_taille_min(genre, age)
taille_max            = recupere_taille_max(genre, age)
perimetre_cranien_min = recupere_perimetre_cranien_minimum(genre, age)
perimetre_cranien_max = recupere_perimetre_cranien_maximum(genre, age)

# Affichage des résultats des analyses
affiche_rapport_poids(genre, age, poids, poids_min, poids_max)
affiche_rapport_taille(genre, age, taille, taille_min, taille_max)
affiche_rapport_perimetre_cranien(genre, age, perimetre_cranien, perimetre_cranien_min, perimetre_cranien_max)
