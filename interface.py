from tkinter import Tk, Label, Entry, Button

#Création du titre et de la dimension du nouveau tableau
fenetre = Tk()
fenetre.title("Le calculateur")
fenetre.geometry("500x400")

label_mensuel = Label(fenetre, text="Salaire mensuel")
label_mensuel.pack()
entry_mensuel = Entry(fenetre)
entry_mensuel.pack()

label_loyer = Label(fenetre, text="Loyer")
label_loyer.pack()
entry_loyer = Entry(fenetre)
entry_loyer.pack()

label_epicerie = Label(fenetre, text="Épicerie")
label_epicerie.pack()
entry_epicerie = Entry(fenetre)
entry_epicerie.pack()

label_transport = Label(fenetre, text="Transport")
label_transport.pack()
entry_transport = Entry(fenetre)
entry_transport.pack()

label_loisir = Label(fenetre, text="Loisir")
label_loisir.pack()
entry_loisir = Entry(fenetre)
entry_loisir.pack()

def calculer():
    salaire = float(entry_mensuel.get())
    loyer = float(entry_loyer.get())
    epicerie = float(entry_epicerie.get())
    transport = float(entry_transport.get())
    loisir = float(entry_loisir.get())
    total_depenses = loyer + epicerie + transport + loisir
    reste = salaire - total_depenses
    label_resultat = Label(fenetre, text=f"Solde restant : {reste:.2f} $")
    label_resultat.pack()

bouton_1 = Button(fenetre, text="Cliquer ici pour calculer", command=calculer)
bouton_1.pack()

fenetre.mainloop()