import random
while True:
    tailleDuPlateau= input("Veillez saisir la taille du plateau : ")
    if tailleDuPlateau.isdigit() and int(tailleDuPlateau) > 0:
        tailleDuPlateau = int(tailleDuPlateau)
        break
    else:
        print("La taille doit être un entier positif.")




def creerPlateau():
    ############################################   
    ##  ON COMMENCE PAR CREER UN PLATEAU VIDE ##
    ############################################

    plateau = [[' ' for i in range(tailleDuPlateau)] for j in range(tailleDuPlateau)]
    
    
    ##########################################################   
    ## JE MET UN X PAR LIGNE ET PAR COLONNE SUR MON PLATEAU ##
    ##########################################################
    
    for i in range(tailleDuPlateau):
        while True:
            x = random.randint(0, tailleDuPlateau-1)
            if plateau[i][x] == ' ':
                plateau[i][x] = 'X'
                break
    
    ##########################################################   
    ##   JE PLACE DES O ES EVITANT DES CONFLIT AVEC LES X   ##
    ##########################################################
    for i in range(tailleDuPlateau):
        for j in range(tailleDuPlateau):
            if plateau[i][j] == ' ':
                # Vérifier si une 'X' est déjà présente dans la même ligne ou colonne
                has_x = False
                for k in range(tailleDuPlateau):
                    if plateau[i][k] == 'X' or plateau[k][j] == 'X':
                        has_x = True
                        break
                
                if not has_x:
                    plateau[i][j] = 'O'
    
    for i in range(tailleDuPlateau):
        for j in range(tailleDuPlateau):
            if(plateau[i][j] == 'X'):
             print('X', end=' ')
            else:
             print('O', end=' ')
        print()
    # return plateau


    

    

creerPlateau()
   



