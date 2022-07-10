from tkinter import filedialog
from tkinter.filedialog import *
from tkinter import messagebox
from util import Util
from util import saisir_string
from personnage import Personnage
from sorcier import Sorcier
from guerrier import Guerrier



class GestionPersonnages():
    liste_personnages = ["Le Sorcier, Gwyr, a une énergie de 6, et 15 charmes", "Sorcier;Pied de chêne;19;7;4", "Guerrier;Lucius Fleurdelotus;14;14;52",
                         "Guerrier;SkyDragon;14;14;26", "Sorcier;Caius Marchéopus;19;19;19", "Guerrier;Heian;20;20;25",
                         "Sorcier;Nuage bleu;22;22;3",
                         "Sorcier;Caius Marchéopus;28;28;4",
                         "Guerrier;Histéric;32;32;65",
                         "Guerrier;Tintabulus;33;33;40",
                         "Sorcier;BlackThorn;34;34;4",
                         "Guerrier;Ciel hurlant;35;35;54",
                         "Guerrier;Bumbadil;36;36;3",
                         "Guerrier;Tintabulus;39;39;43",
                         "Guerrier;Pleindastus;47;47;5",
                         "Sorcier;Nuage bleu;50;50;14",
                         "Guerrier;L'Auroch;51;51;31",
                         "Guerrier;Cheval d'argent;52;52;13",
                         "Sorcier;Itak Italé;55;55;16",
                         "Sorcier;Tornade rouge;55;55;13",
                         "Sorcier;Amérix;56;56;16",
                         "Guerrier;Ptah;56;56;9",
                         "Sorcier;Caïus Obtus;60;60;13",
                         "Sorcier;Liric;66;66;10",
                         "Sorcier;Hibou-qui-silence;69;69;8",
                         "Sorcier;Nuage bleu;22;22;3",
                         "Sorcier;Caius Marchéopus;28;28;4",
                         "Guerrier;Histéric;32;32;65",
                         "Guerrier;Tintabulus;33;33;40",
                         "Sorcier;BlackThorn;34;34;4",
                         "Guerrier;Ciel hurlant;35;35;54",
                         "Guerrier;Bumbadil;36;36;3",
                         "Guerrier;Tintabulus;39;39;43",
                         "Guerrier;Pleindastus;47;47;5",
                         "Sorcier;Nuage bleu;50;50;14",
                         "Guerrier;L'Auroch;51;51;31",
                         "Guerrier;Cheval d'argent;52;52;13",
                         "Sorcier;Itak Italé;55;55;16",
                         "Sorcier;Tornade rouge;55;55;13",
                         "Sorcier;Amérix;56;56;16",
                         "Guerrier;Ptah;56;56;9",
                         "Sorcier;Caïus Obtus;60;60;13",
                         "Sorcier;Liric;66;66;10",
                         "Sorcier;Hibou-qui-silence;69;69;8"]
    fichier_courant = " "
    """
    Classe s'occupant de la gestion des personnages. 
    Attributes:
        liste_personnages (list): La liste des personnages
        fichier_courant (str): Le nom du fichier courant
    """

    def mettre_a_jour_liste(self):
        for i in self.liste_personnages:
            pass
        """
        Mets à jour et trie la liste des personnages par rapport à l'énergie courante. 
        Returns (list str): La liste triée des chaînes de caractères des personnages

        """

    def gestion_creer_sorcier(self):
        if saisir_et_creer_sorcier(self)==True:
            ajouter_personnage(self)
            return "Le nouveau sorcier a été ajouté à la liste"
        else:
            return "Le sorcier n'a pas été ajouté"


        pass

        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier) 
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.  
        Sinon, on affiche seulement que le sorcier n’a pas été ajouté.
        """

    def saisir_et_creer_sorcier(self):
        self.util.saisir_string("Donnez le nom du sorcier (entre 3 à 30)")
        if self.valider_nom(nom) == True:
            saisir_objet_entier("Entrez l'énergie du sorcier")
            if self.valider_energie_depart(energie_depart) == True:
                saisir_objet_entier("Entrez le nombre de charmes")
                if self.valider_nbr_charmes(nbr_charmes) == True:
                    return (self.nom)


        pass
        """
        Retourne un objet Sorcier valide. Chaque information du sorcier demandée doit être validée. 
        L’annulation d’une info entraine automatiquement l’annulation des informations suivantes.  
        Si toutes les informations sont valides, un sorcier est alors instancié.

        Return (Sorcier): Le sorcier instancié si la création a réussie, None sinon.
        """

    def gestion_creer_guerrier(self):
        if saisir_et_creer_guerrier(self) ==True:
            ajouter_personnage(self)
            print("Le nouveau guerrier a été ajouté à la liste")
        else:
            print("Le sorcier n'a pas été ajouté")
        pass
        """
        Crée un personnage sorcier si les informations du sorcier (méthode saisir_et_creer_sorcier) 
        sont valides, on ajoute le sorcier à la liste (méthode ajouter_personnage) et on affiche le message approprié.  
        Sinon, on affiche seulement que le sorcier n’a pas été ajouté.
        """

    def saisir_et_creer_guerrier(self):
        if self.valider_force(force) == True:
            saisir_string("Entrez le nom du sorcier")
                    return (self.nom)
        pass
        """
        Retourne un objet Guerrier valide.  Chaque information du guerrier demandée doit être validée. 
        L’annulation d’une information entraine automatiquement l’annulation des informations suivantes.  
        Si toutes les infos sont valides, un guerrier est alors instancié.

        Returns (Guerrier): Le guerrier instancié si la création a réussie, None sinon.
        """

    def ajouter_personnage(self, personnage):

        pass
        """
        Ajoute le Personnage à la liste.
        Args:
            personnage (Personnage): Le personnage à ajouter. 
        """

    def gestion_attaquer(self, index):
        pass
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.  
        Si le personnage sélectionné n’est pas mort, on saisit avec validation la force de l’attaque 
        (> 0 et <= energie_max).  Lorsque la force saisie est valide, on attaque le personnage sélectionné sinon on 
        affiche un message adéquat.  S’il n’y a aucun personnage sélectionné ou s’il est mort, 
        un message est affiché.

        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné. 
        """

    def gestion_augmenter_energie(self, index):
        pass
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.  
        Si le personnage sélectionné n’est pas mort, réinitialiser son énergie. S’il n’y a aucun personnage 
        sélectionné ou s’il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné. 
        """

    def gestion_crier(self, index):
        pass
        """
        Reçoit l’indice du personnage sélectionné ou -1 si aucun personnage n’est sélectionné.  
        Si le personnage sélectionné n’est pas mort, émettre son cri.  S’il n’y a aucun personnage sélectionné ou 
        s’il est mort, un message personnalisé est affiché.
        Args:
            index (int): L'indice du personnage sélectionné ou -1 si aucun n'est sélectionné. 
        """

    def gestion_ouvrir(self):
        if self.liste_personnages != []:
            sauvegarder_donnees = messagebox.askyesno("Gestion personnages",
                                                      "Voulez-vous sauvegarder les données courantes avant d'ouvrir un nouveau fichier?")
            if sauvegarder_donnees == True:
                self.gestion_enregistrer_sous()
                file = filedialog.askopenfile(mode="r", title="Sélectionner le fichier", filetypes=[("txt", "*.txt")])
                if file is None:
                    pass
                else:
                    content = file.read()
                    print(content)
            else:
                file = filedialog.askopenfile(mode="r", title="Sélectionner le fichier", filetypes=[("txt", "*.txt")])
                if file is None:
                    pass
                else:
                    content = file.read()
                    print(content)
        else:
            file = filedialog.askopenfile(mode="r", title="Sélectionner le fichier", filetypes=[("txt", "*.txt")])
            if file is None:
                pass
            else:
                content = file.read()
                print(content)

        """
        MANQUE À CHANGER LE FICHIER COURANT POUR LE FICHIER NOUVEAU, GERER LA RÉUSSITE DE SAUVEGARDE ET LE MESSAGE D'ERREUR
        Permet de gérer l'ouverture et la lecture d'un fichier de personnages 
        (un fichier .txt qui contient des informations sur des personnages, un personnage par ligne).  
        Si la liste n’est pas vide, on demande à l’utilisateur s’il veut sauvegarder les données courantes et 
        s’il répond oui, on fait appel à gestion_enregistrer_sous.  Ensuite, on demande à l’utilisateur le nom du 
        fichier à ouvrir.  Si le fichier choisi n’est pas null, le fichier à ouvrir devient le fichier courant 
        et si la lecture du fichier n’a pas bien fonctionné (voir méthode lireFichierPersonnages dans classe Util), 
        un message d’erreur est affiché.
        """

    def gestion_enregistrer(self):
        pass
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans le fichier courant.  
        Si on a un fichier courant, on écrit les personnages de la liste dedans 
        (voir méthode ecrire_fichier_personnages dans la classe Util) et on affiche un message approprié. 
        Si l’enregistrement n’a pas fonctionné, un message d’erreur est affiché. Si on n’a pas de fichier courant, 
        on enregistre dans un nouveau fichier en appelant la méthode (gestion_enregistrer_sous). 
        """

    def gestion_enregistrer_sous(self):

        pass
        """
        Permet de gérer l'enregistrement d'une liste de personnages dans un nouveau fichier.  
        On demande un nom de fichier à l’utilisateur, on l’assigne au fichier courant et on écrit 
        dedans les personnages (voir méthode ecrire_fichier_personnages dans la classe Util).  
        Afficher un message personnalisé s’il y a erreur lors de la sauvegarde ou si la sauvegarde est ok.
        """

    def gestion_vider_liste(self):
        if self.liste_personnages != []:
            sauvegarder_donnees = messagebox.askyesno("Gestion personnages",
                                                      "Voulez-vous sauvegarder les données courantes avant de vider la liste de personnages?")
            if sauvegarder_donnees == True:
                if self.fichier_courant is not None:
                    self.gestion_enregistrer()
                    self.liste_personnages = []
                    self.fichier_courant = None
                else:
                    self.gestion_enregistrer_sous()
                    self.liste_personnages = []
                    self.fichier_courant = None
            else:
                self.liste_personnages = []
                self.fichier_courant = None
        else:
            self.fichier_courant = None
        """
        Permet de fermer le fichier courant. Si la liste n'est pas vide et que l'utilisateur veut sauvegarder ses 
        données, enregistrer les données de la liste dans le fichier courant (gestion_enregistrer) ou dans un 
        nouveau fichier (gestion_enregistrer_sous) s’il n’y a pas de fichier courant.  
        La liste est vidée et le fichier courant devient none.
        """

    def gestion_quitter(self):
        quitter_application = messagebox.askyesno("Gestion personnages", "Voulez-vous vraiment quitter ce programme?")
        if quitter_application == True:
            exit()
        else:
            pass

        """
        Permet de quitter l'application après confirmation de l'utilisateur.
        """


n = Sorcier('2367', 40, 20, 10)
