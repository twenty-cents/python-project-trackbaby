#######################################################################################
# Nom du script : nourrisson1-form.py
# Version       : 1.0
# Créé le       : 04/10/19 par Vincent 
# 
#######################################################################################
# Version améliorée du script nourrisson1.py avec affichage d'une fenêtre de saisie
# pour saisir les données suivantes du nourrisson :
# - genre
# - poids
# - taille
# - périmètre crânien
#
#######################################################################################
# TODO : La gestion de la fermeture par la croix de la fenêtre n'entraine pas 
#        l'arrêt du script
#
# Bug : la fenêtre ne ferme pas 
#       Lors de l'appui sur le bouton VALIDER, les contrôles sont déchargés de la 
#       fenêtre, mais celle-ci reste ouverte
#
#######################################################################################

# Données de références nourrisson
import nourrisson1_donnees
# Pour gérer la sortie du script
import sys
# Pour gérer le formulaire de saisie
import pyforms 
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton
from pyforms.controls import ControlCombo
from pyforms.controls import ControlSlider
from pyforms.controls import ControlNumber

# Classe Formulaire de saisie
class SaisieGenreForm(BaseWidget):

    top_ok = False

    def __init__(self, *args, **kwargs):
        super().__init__('Suivi nourrisson Step 3')

        #Definition of the forms fields
        self._genrecbx = ControlCombo('Genre')
        self._ageslider = ControlSlider('Age (en mois)')
        self._poidstext = ControlNumber('Poids (en kg)')
        self._tailletext = ControlNumber('Taille (en cm)')
        self._perimetrecranientext = ControlNumber('Périmètre crânien (en cm)')
        self._runbutton     = ControlButton('Vérifier les constantes')

        # Initialisation de la combo box Genre
        self._genrecbx.add_item('Garçon', 'g')
        self._genrecbx.add_item('Fille', 'f')

        # Initialisation du slider Age
        self._ageslider.min = 0
        self._ageslider.max = 60

        # Initialisation de la saisie du poids
        self._poidstext.min = 0
        self._poidstext.step = .1
        self._poidstext.decimals = 1

        # Initialisation de la saisie de la taille
        self._tailletext.min = 0
        self._tailletext.step = .1
        self._tailletext.decimals = 1

        # Initialisation de la saisie du périmètre crânien
        self._perimetrecranientext.min = 0
        self._perimetrecranientext.step = .1
        self._perimetrecranientext.decimals = 1

        # Ajout du callback quand le bouton de validation est pressé
        self._runbutton.value = self.__runEvent

        # Ajout des contrôles dans le formulaire
        self._formset = [
            '_genrecbx',
            '_ageslider',
            '_poidstext',
            '_tailletext',
            '_perimetrecranientext',
            '_runbutton'
        ]

    def __runEvent(self):
        # Bug : la fenêtre ne ferme pas
        # Les contrôles sont déchargés de la fenêtre, mais la fenêtre reste ouverte
        self.close()

# ------------------------------------------------------------------------------------------------
# Exécution de la fenêtre de saisie des données du nourrisson
# Etape 1 - 
# ------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    from pyforms import start_app
    frame = start_app(SaisieGenreForm, geometry=(200, 200, 400, 400) )

# ------------------------------------------------------------------------------------------------
# Fonctions du script
# ------------------------------------------------------------------------------------------------
genre_denomination = ""

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
# Exécution du script
# Etape 2 
# Processus d'analyse des résultats
# ------------------------------------------------------------------------------------------------
print("Bienvenue dans ce programme de vérification des constantes de votre nourrisson !")
# Saisie des entrées clavier
genre             = frame.controls.get('_genrecbx').value
age               = frame.controls.get('_ageslider').value
poids             = frame.controls.get('_poidstext').value
taille            = frame.controls.get('_tailletext').value
perimetre_cranien = frame.controls.get('_perimetrecranientext').value

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
