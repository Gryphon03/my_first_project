######################################
#   CALCULATEUR DE BUDGET MENSUEL    #
######################################


def saisir_montant(message):
    while True:
        try:
            message_erreur = "La réponse que vous avez saisie est invalide. Veuillez réessayer."
            liste_depenses = float(input(message))
            return liste_depenses
        except ValueError:
            print(message_erreur)


def saisir_revenu():
    salaire_principal = saisir_montant("Entrez le salaire mensuel : ")
    return salaire_principal

def saisir_depenses_mensuelles():
    n_liste_depenses = ["Loyer", "Épicerie", "Transport", "Loisir"]
    total = 0
    for elem in n_liste_depenses:
        liste_depenses = saisir_montant(f"Entrez le montant associé au {elem} : ")
        total = total + liste_depenses
    return total

def montant_restant(salaire, depenses):
    revenu_restant = salaire - depenses
    return revenu_restant

def main():
    salaire = saisir_revenu()
    depenses = saisir_depenses_mensuelles()
    reste = montant_restant(salaire,depenses)
    print(f"À la fin du mois, selon vos données il vous restera ${reste:.2f}.")

    if reste > 0:
        print("Félicitations, vos finances sont bien gérées!")
    elif reste == 0:
        print("Faites attention, vous êtes à risque de faillite.")
    elif reste < 0:
        print("DANGER ! Vous dépensez plus d'argent que vous n'en gagnez. Penser à réviser vos dépenses.")

main()