while True:
    # Demande à l'utilisateur de saisir un mot
    mot = input("Veuillez saisir un mot sans accent ni majuscule: ")

    if mot.isalpha():
        break
    else:
        print("Le mot doit contenir uniquement des lettres de l'alphabet (sans accent ni majuscule).")

print("Vous avez saisi le mot :", mot)