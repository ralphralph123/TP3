from tkinter.filedialog import *
from tkinter import *
from gestion_personnages import GestionPersonnages
from personnage import Personnage


class Interface(Frame):
    gp = GestionPersonnages
    ps = Personnage
    pIndex = -1
    liste_personnages = []
    sauvegarder_donnees = " "

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Personnages : Un exemple d'héritage et de polymorphisme")
        self.pack(fill=BOTH, expand=True)

        self.menubar = Menu(self)

        menu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Fichier", menu=menu)
        menu.add_command(label="Ouvrir...", command=self.menuOuvrir_Click)
        menu.add_command(label="Enregistrer...", command=self.menuEnregistrer_Click)
        menu.add_command(
            label="Enregistrer sous...", command=self.menuEnregistrerSous_Click
        )
        menu.add_command(label="Vider liste...", command=self.menuViderListe_Click)
        menu.add_command(label="Quitter...", command=self.menuQuitter_Click)
        # ajouter les autres options

        self.master.config(menu=self.menubar)
        fen = self

        # frame 1 (droite)
        self.f1 = Frame(fen, bg="grey100")
        self.f1.pack(side=RIGHT, expand=TRUE)

        # frame 2 (gauche)

        # Ajout de labels dans les frames

        # Ajout du listbox

        scrollbar = Scrollbar(self, orient="vertical")
        scrollbar.pack(side=RIGHT, fill=BOTH)

        self.listbox = Listbox(self, width=350)
        self.listbox.pack(side=LEFT, fill=BOTH)

        def selectionner(evt):
            valeur = str((self.listbox.get(ACTIVE)))
            print(valeur)

        self.listbox.bind("<<ListboxSelect>>", selectionner)

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Ajout de bouttons

        b1 = Button(
            self.f1,
            padx=30,
            pady=27,
            text="Créer un sorcier",
            command=self.btnSorcier_Click,
        )
        b1.pack()

        b2 = Button(
            self.f1,
            padx=28,
            pady=27,
            text="Créer un guerrier",
            command=self.btnGuerrier_Click,
        )
        b2.pack()

        b3 = Button(
            self.f1, padx=53, pady=27, text="Attaquer", command=self.gp.gestion_attaquer
        )
        b3.pack()

        b4 = Button(
            self.f1,
            padx=17,
            pady=27,
            text="Réinitialiser l'énergie",
            command=self.gp.gestion_augmenter_energie,
        )
        b4.pack()

        b5 = Button(
            self.f1, padx=64, pady=27, text="Crier", command=self.gp.gestion_crier
        )
        b5.pack()

    def listIsEmpty(self):
        try:
            self.index = int(self.listbox.curselection()[0])
        except IndexError:
            return True

        return False

    # Ajoute un personnage dans la listbox
    def appendList(self, personnage):
        self.listbox.insert(END, personnage)

    # Remplace tous les personnages de la listbox par une nouvelle liste
    def updateList(self, personnages):
        self.listbox.delete(0, END)

        for personnage in personnages:
            self.listbox.insert(END, personnage)

        self.pIndex = -1

    # Permet d'identifier le personnage selectionné (set pIndex)
    def listbox_Click(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        index = widget.curselection()[0]

        # print ("selection:", selection, ": '%s'" % value)

        self.pIndex = index
        # print(gp.getPersonnage(index))

    def menuOuvrir_Click(self):
        self.gp.gestion_ouvrir(self)
        personnages = self.gp.mettre_a_jour_liste(self)

        # Update listview
        if personnages:
            self.updateList(personnages)

    def menuEnregistrer_Click(self):
        self.gp.gestion_enregistrer(self)

    def menuEnregistrerSous_Click(self):
        self.gp.gestion_enregistrer_sous(self)
        asksaveasfile(filetypes=[("all files", ".*")])

    def menuViderListe_Click(self):
        self.gp.gestion_vider_liste(self)
        # quit()

    def menuQuitter_Click(self):
        if self.gp.gestion_quitter(self):
            quit()

    def btnSorcier_Click(self):

        self.sorcier = GestionPersonnages.saisir_et_creer_sorcier(self)
        self.new_liste = GestionPersonnages.ajouter_personnage(self)
        if self.new_liste != None:
            self.listbox.delete(0, END)
            for values in self.new_liste:
                self.listbox.insert(END, values)
            self.gp.mettre_a_jour_liste(self)

    def btnGuerrier_Click(self):
        self.energie_courante = n.saisir_et_creer_guerrier()
        self.new_liste = n.ajouter_personnage(self.energie_courante)
        if self.new_liste != None:
            self.listbox.delete(0, END)
            for values in self.new_liste:
                self.listbox.insert(END, values)
            self.gp.mettre_a_jour_liste(self)

    def btnAttaquer_Click(self):
        self.gp.gestion_attaquer(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        if personnages:
            self.updateList(personnages)

        # Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")

    def btnRedonnerEnergie_Click(self):
        self.gp.gestion_augmenter_energie(self.pIndex)
        row = self.pIndex
        personnages = self.gp.mettre_a_jour_liste()

        # Update listview
        self.updateList(personnages)

        # Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")

    def btnCrier_Click(self):
        self.gp.gestionCrier(self.pIndex)
        row = self.pIndex

        # Garder le focus sur la meme ligne
        self.listbox.select_set(row)
        self.listbox.event_generate("<<ListboxSelect>>")


def main():
    root = Tk()
    root.geometry("700x400+300+100")
    app = Interface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
