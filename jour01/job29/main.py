def moyenne(liste_note):
    for i in range(len(liste_note)):
        if liste_note[i] > 40 and liste_note[i] % 5 > 2 and liste_note[i] <=100:
                liste_note[i] = liste_note[i] + (5 - liste_note[i] % 5)
    return liste_note

liste_note = [73, 67, 48, 53]   

resultat = moyenne(liste_note)
print(resultat)
               

    