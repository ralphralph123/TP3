class Personnage:
    energie_depart_defaut = 20
    energie_depart_min = 1
    energie_max = 100
    longueur_nom_min = 3
    longueur_nom_max = 30
    nom = " "
    energie_depart = 0
    energie_courante = 0

    def __init__(self, nom, energie_depart):
        self.nom = nom
        self.energie_depart = energie_depart
        self.energie_courante = energie_depart
        """
        Le constructeur du Personnage. Il doit initialiser le nom, l’énergie de départ et l’énergie courante. 
        À la création d’un objet personnage, l’énergie courante égale à l’énergie de départ.
        Args:
            nom (str): Le nom du personnage  
            energie_depart (int): L'énergie de départ 
        """

    def crier(self):
        return None
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def attaquer(self, force_attaque):
        return None
        """
        Méthode abstraite (sans code) utile pour l’héritage, cela forcera la classe dérivée à surcharger 
        la méthode (polymorphisme).
        """

    def est_mort(self):
        if self.energie_courante <= 0:
            return True
        else:
            return False

    def valider_nom(self, nom):
        self.nom = nom
        if (
            len(self.nom) >= Personnage.longueur_nom_min
            and len(self.nom) <= Personnage.longueur_nom_max
        ):
            return True
        else:
            return False
        """
        Valide le nom du personnage. Un nom de personnage est valide lorsqu’il a la bonne longueur 
        (entre min et max) bornes incluses.
        Args:
            nom (str): Le nom à valider

        Returns (bool): True si le nom est valide, False sinon.
        """

    def valider_energie_courante(self, energie_courante):
        self.energie_courante = energie_courante
        if (
            self.energie_courante >= 0
            and Personnage.energie_courante <= Personnage.energie_max
        ):
            return True
        else:
            return False

        """
        Valide l'énergie courante. Elle doit être positive (0 inclus) et ne doit pas dépasser energie_max.
        Args:
            energie_courante (int): L'énergie à valider.

        Returns (bool): True si l'énergie est valide, False sinon.

        """

    def valider_energie_depart(self, energie_courante):
        self.energie_courante = energie_courante
        if (
            Personnage.energie_depart >= Personnage.energie_depart_min
            and Personnage.energie_depart <= Personnage.energie_max
        ):
            return True
        else:
            return False
        """
        Valide l'énergie de départ. Elle est valide lorsqu’elle est entre energie_depart_min et 
        energie_max. (bornes incluses). 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'énergie de départ est valide, False sinon.
        """

    def reset_energie(self):
        self.energie_courante = self.energie_depart
        """
        Remet l’énergie courante du personnage à sa valeur de départ.
        """

    def get_energie_courante(self):
        return self.energie_courante
        """
        Retourne l'énergie courante
        Returns (int): L'énergie courante
        """

    def set_energie_courante(self, energie_courante):
        if self.valider_energie_courante(energie_courante) == True:
            self.energie_courante = energie_courante
            return True
        else:
            return False
        """
        Assigne l'énergie courante si elle est valide. 
        Args:
            energie_courante (int): L'énergie courante 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """

    def get_nom(self):
        return self.nom
        """
        Retourne le nom.
        Returns (str): Le nom.
        """

    def set_nom(self, nom):
        if self.valider_nom(nom) == True:
            self.nom = nom
            return True
        else:
            return False
        """
        Assigne le nom s'il est valide. 
        Args:
            nom (str): Le nom

        Returns (bool): True si l'assignation a réussi, False sinon.
        """

    def get_energie_depart(self):
        return self.energie_depart
        """
        Retourne l'énergie de départ.
        Returns (int): L'énergie de départ
        """

    def set_energie_depart(self, energie_depart):
        if self.valider_energie_depart(energie_depart) == True:
            self.energie_depart = energie_depart
            return True
        else:
            return False
        """
        Assigne l'énergie de départ si elle est valide. 
        Args:
            energie_depart (int): L'énergie de départ 

        Returns (bool): True si l'assignation a réussi, False sinon.
        """

    # compléter la méthode manquante


if __name__ == "__main__":
    t = Personnage("236", 50)
    print(t.valider_nom(""))
    print(t.est_mort())
    print(t.valider_energie_courante(""))
    print(t.valider_energie_depart(""))
    print(t.reset_energie())
    print(t.set_energie_courante(""))
    print(t.set_nom(""))
    print(t.get_energie_depart())
    print(t.set_energie_depart(""))
