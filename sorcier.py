from personnage import Personnage


class Sorcier(Personnage):
    nbr_charmes_defaut = 20
    nbr_charmes_max = 20
    nbr_charmes = 0
    """ 
    Classe représentant un Sorcier. Hérite de Personnage.
    Attributes:
        nb_charmes_defaut (int): Le nombre de charmes par défaut
        nb_charmes_max (int): Le nombre de charmes maximum
        nb_charmes (int): Le nombre de charmes courant
    """

    def __init__(self, nom, energie_depart, energie, nbr_charmes):
        super().__init__(nom, energie_depart)
        self.nbr_charmes = nbr_charmes
        self.energie_courante = energie
        """
        Le constructeur du Sorcier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et
        le nombre de charmes. NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom: Le nom du sorcier
            energie_depart:  L'énergie de départ du sorcier
            energie: L'énergie courante du sorcier
            nbr_charmes:  Le nombre de charmes du sorcier
        """

    def to_string(self):
        return "Le sorcier, {} a une énergie de {} et {} charmes".format(
            self.nom, self.energie_courante, self.nbr_charmes
        )
        """
        Retourne une chaîne du genre "Le sorcier, nom de Personnage, a une énergie de, valeur de l’énergie et,
        valeur du nombre de charmes, charmes."
        Returns (str): La chaîne représentant le Sorcier.
        """

    def valider_nbr_charmes(self, nbr_charmes):
        self.nbr_charmes = nbr_charmes
        if self.nbr_charmes >= 0 and self.nbr_charmes <= Sorcier.nbr_charmes_max:
            return True
        else:
            return False
        """
        Valide que le nombre de charmes est positif (0 inclus) et ne doit pas dépasser nbr_charmes_max. 
        Args:
            nb_charmes (int): Le nombre de charmes à valider 

        Returns (bool): True si le nombre de charmes est valide, false sinon.
        """

    def crier(self):
        return "Je vais tous vous anéantir!"
        """
        Retourne le cri du sorcier: "Je vais tous vous anéantir!"
        Returns: Le cri du sorcier
        """

    def attaquer(self, force_attaque):
        self.force_attaque = force_attaque
        self.energie_courante -= self.force_attaque
        if self.energie_courante <= 0:
            self.energie_courante = 0
        """
        Lorsqu’un sorcier se fait attaquer son énergie est diminuée de la force de l’attaque. Si la force de l’attaque est
        plus grande que son énergie, l’énergie du sorcier devient 0 (il meurt). 
        Args:
            force_attaque (int): La force de l'attaque 
        """

    def get_nbr_charmes(self):
        return self.nbr_charmes
        """
        Retourne le nombre de charmes du sorcier.
        Returns (int): Le nombre de charmes du sorcier.

        """

    def set_nbr_charmes(self, nbr_charmes):
        self.nbr_charmes = nbr_charmes
        if self.valider_nbr_charmes(nbr_charmes) == True:
            self.nbr_charmes = nbr_charmes
            return True
        else:
            return False
        """
        Assigne le nombre de charmes du sorcier. Le nombre de charmes doit être valide.
        Args:
            nb_charmes (int): Le nombre de charmes  

        Returns (bool): True si le nombre de charmes est valide et a été modifié, False sinon.
        """
