def saisir_revenu():
    salaire_principal = float(input("Entrez le salaire mensuel: "))
    return salaire_principal

def saisir_depenses_mensuelles():
    liste_depenses = float(input("Entrez le montant des dépenses mensuelles: "))
    return liste_depenses

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