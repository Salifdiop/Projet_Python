"""
Vous êtes admin d'une PME qui exerce dans la microfinance.
Vous êtes sollicités afin de composer un script qui permet de gerer les projets
Le script comporte les fonctions suivantes :
-Fonction de saisie des informations d'un projet
-Fonction de creation d'un dossier dans le disque local C
-Fonction d'affichage des informations d'un projet saisi
-fonction de creation d'un fichier contenant l'ensemble des projet de la PME
Ce fichier est contenu dans le dossier initialement creer dans C
-Une fonction qui affiche l'ensemble des projets du fichier
-Une fonction qui determine le cout total de tous les projets du fichier
-Une fonction qui determine et affiche le projet dont le cout est le plus eleve et le projet dont le cout est
le plus faible
-Une fonction qui ajoute de nouveau projet dans le fichier
-Fonction pour le menu
Projet(code,nom,porteur de projet,cout du projet,secteur d'activité,localisation projet)
"""
#Fonction de saisie des informations d'un projet
sep = ";"
def saisi_information_projet():
    print("~~~~~~~~~~~~~~"*10)
    print("Saisi des informations d'un projet :")
    code = input("Entrer le code du projet :")
    nom = input("Entrer le nom du projet :")
    porteur_de_projet = input("Entrer le porteur de projet :")
    while True :
        cout_projet = input("Entrer le cout du projet :")
        if cout_projet.strip().isdigit():
            break
        else:
            print("Erreur !! Le cout est numérique .")
    secteur_activite = input("Entrer le secteur d'activité :")
    localisation = input("Entrer la localisation du projet :")
    duree_projet = input("Entrer la duree du projet :")
    projet = code+sep+nom+sep+porteur_de_projet+sep+cout_projet+sep
    projet+=secteur_activite+sep+localisation+sep+duree_projet+sep+"\n"
    return projet
#projet = saisi_information_projet()
#print(projet)

#Fonction de creation d'un dossier dans le disque local C
import os

def creation_dossier():
    nom_dossier = input("Entrer le nom du dossier á creer : ")
    os.chdir("C:/")
    if os.path.exists(nom_dossier):
        print("Un dossier de même nom existe deja!")
    else:
        os.mkdir(nom_dossier)
        print(f"Le dossier {nom_dossier} est cree avec succes dans C")
#creation_dossier()
        
#Fonction d'affichage des informations d'un projet saisi
def affiche_information_projet(projet):
    if len(projet)==0:
        print("Aucun projet est passé en parametre !")
    else:
        print("les informations du projet sont :")
        proj = projet.split(sep)
        for p in proj:
            print(p,end="\t")
        print()
#affiche_information_projet(projet)

#fonction de creation d'un fichier contenant l'ensemble des projet de la PME
def creation_fichier_projet():
    nom_dossier = input("Entrer le nom du dossier qui va contenir le fichier á creer : ")

    #chemin du dossier Documents
    #chemin = "C:/Users/HP/OneDrive - ESMT/Bureau/Python"

    #Se deplacer dans Documents
    
    os.chdir("C:/")
    
    if not os.path.exists(nom_dossier):
        print("Le dossier n'existe pas")
    else:
        nom_fichier = "liste_projets.txt"
        os.chdir(nom_dossier)
        if not os.path.exists(nom_fichier):
            f = open(nom_fichier,"w")
            while True:
                reponse = input("voulez vous ajouté un nouveau projet ? O/N :")
                if reponse.upper()=="O":
                    projet = saisi_information_projet()
                    f.write(projet)
                    print("projet enregistrer avec succés dans le fichier ")
                elif reponse.upper()=="N":
                    f.close()
                    print("Fin de la creation de fichier")
                    break
                else:
                    print("Erreur de choix")
        else:
            print("Le fichier existe deja")
#creation_fichier_projet()

#Une fonction qui affiche l'ensemble des projets du fichier
def affiche_fichier_projet():
    nom_dossier = input("Entrer le nom du dossier qui contient les projets :")
        
    os.chdir("C:/")
    
    if not os.path.exists(nom_dossier):
        print("Le dossier n'existe pas")
    else:
        nom_fichier = "liste_projets.txt"
        os.chdir(nom_dossier)
        if os.path.exists(nom_fichier):
            f = open(nom_fichier,"r")
            projets=f.readlines()
            f.close()
            if len(projets)==0:
                print("Le fichier du projet est vide")
            else:
                print("La liste des projets du fichier est :")
                i=1
                for projet in projets:
                    print("~~~~~"*10)
                    print("\t PROJET NUMERO",i)
                    affiche_information_projet(projet)
                    i +=1
        else:
            print("Le fichier n'existe pas")
#affiche_fichier_projet()

#Une fonction qui determine le cout total de tous les projets du fichier
def affiche_cout_total_projet():
    nom_dossier = input("Entrer le nom du dossier qui contient les projets :")
        
    os.chdir("C:/")
    
    if not os.path.exists(nom_dossier):
        print("Le dossier n'existe pas")
    else:
        nom_fichier = "liste_projets.txt"
        os.chdir(nom_dossier)
        if os.path.exists(nom_fichier):
            f = open(nom_fichier,"r")
            projets=f.readlines()
            f.close()
            if len(projets)==0:
                print("Le fichier du projet est vide")
            else:
                total = 0
                for projet in projets:
                    cout = int(projet.split(sep)[3])
                    total+=cout
                print("Le cout total des projet est :",total,"FCFA")
        else:
            print("Le fichier n'existe pas")
affiche_cout_total_projet()
                




























        
