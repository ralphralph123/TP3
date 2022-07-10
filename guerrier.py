from personnage import Personnage


class Guerrier(Personnage):
    force_defaut = 20
    force_max = 80
    perte_force_defaut = 2
    gain_force_defaut = 10
    force = 0
    """
    Classe représentant un Guerrier. Hérite de Personnage.
    Attributes:
        force_defaut (int): La valeur par défaut de la force
        force_max (int): La valeur maximum de la force
        perte_force_defaut (int): La perte de force lors d'une attaque
        gain_force_defaut (int): Le gain de force lors d'une resitution d'énergie
        force (int): La force courante du guerrier
    """
    def __init__(self, nom, energie_depart, energie, force):
        super().__init__(nom, energie_depart)
        self.force = force
        self.energie_courante = energie
        """
        Le constructeur du Guerrier. Il doit initialiser le nom, l’énergie de départ, l’énergie courante et la force. 
        NB : pensez à optimiser votre code et utiliser le constructeur de la classe parente.
        Args:
            nom (str): Le nom du guerrier 
            energie_depart (int): L'énergie de départ du guerrier 
            energie (int): L'énergie courante du guerrier 
            force (int): La force du guerrier 
        """


    def to_string(self):
        return "Le guerrier, {} a une énergie de {} et une force de {}".format(self.nom, self.energie_courante, self.force)
        """
        Retourne une chaîne du genre : "Le guerrier, nom de Personnage, a une énergie de valeur de 
        l’énergie et une force de valeur de la force."
 
        Returns (str): La chaîne représentant le guerrier. 
        """


    def valider_force(self, force):
        if self.force >= 0 and self.force <= self.force_max:
            return True
        else:
            return False
        """
        Valide si la force en paramètre est valide (entre 0 et force_max inclusivement).
        Args:
            force (int): La force à valider 

        Returns (bool): True si la force est valide, False sinon
        """
    
    
    def get_force(self):
        return self.force
    
    
    def set_force(self, force):
        if self.valider_force(force) == True:
            self.force = force
            return True
        else:
            return False
        

    def crier(self):
        return "Vous allez goûter à la puissance de mon épée!"
        """
        Retourne le cri du guerrier : "Vous allez goûter à la puissance de mon épée!"
        Returns (str): Le cri du guerrier
        """


    def attaquer(self, force_attaque):
        self.force_attaque = force_attaque
        self.energie_courante -= self.force_attaque
        self.force -= self.perte_force_defaut
        if self.energie_courante <= 0 or self.force <= 0:
            self.energie_courante = 0
            self.force = 0
        """
        Lorsqu’un guerrier se fait attaquer, son énergie est diminuée de la force de l’attaque.  
        Si la force de l’attaque est plus grande que son énergie, l’énergie du guerrier devient 0 (il meurt).
        Lors d’une attaque, la force du guerrier est aussi modifiée.  Elle est diminuée, à chaque attaque, 
        de la valeur de perte_force_defaut jusqu’à concurrence de 0.  Si le guerrier meurt pendant l’attaque, 
        sa force est aussi mise à 0.
        Args:
            force_attaque (int): La force de l'attaque 
        """

    def reset_energie(self):
        self.energie_courante = self.energie_depart
        while self.force <= 90:
            self.force += self.gain_force_defaut

        """
        Permet de remettre l’énergie courante du guerrier à sa valeur de départ (héritage) et 
        augmente sa force (la valeur de force) par la valeur de gain_force_defaut jusqu’à concurrence de 
        la force maximale sans jamais la dépasser.       
        """

    # setter et getter, a vous de compléter
m = Guerrier('23',40, 100, 48)
print(m.reset_energie())