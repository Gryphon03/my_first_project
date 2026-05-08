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
    categorie = {}
    n_liste_depenses = ["Loyer", "Épicerie", "Transport", "Loisir"]
    total = 0
    for elem in n_liste_depenses:
        liste_depenses = saisir_montant(f"Entrez le montant associé au {elem} : ")
        total = total + liste_depenses
        categorie[elem] = liste_depenses
    return total, categorie

def montant_restant(salaire, depenses):
    revenu_restant = salaire - depenses
    return revenu_restant

def main():
    salaire = saisir_revenu()
    depenses, categorie = saisir_depenses_mensuelles()
    reste = montant_restant(salaire,depenses)
    print("=" * 30)
    print("  RÉSUMÉ DU BUDGET MENSUEL  ")
    print("=" * 30)
    for nom, montant in categorie.items():
        print(f"{nom:<15}: ${montant:.2f}     {(montant/salaire) * 100}%")
    print("-" * 30)
    print(f"À la fin du mois, selon vos données il vous restera ${reste:.2f}.")
    print("=" * 30)

    if reste > 0:
        print("Félicitations, vos finances sont bien gérées!")
    elif reste == 0:
        print("Faites attention, vous êtes à risque de faillite.")
    elif reste < 0:
        print("DANGER ! Vous dépensez plus d'argent que vous n'en gagnez. Penser à réviser vos dépenses.")

main()