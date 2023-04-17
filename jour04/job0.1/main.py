nombre = input("Veillez saisir un nombre entier : ")
nombre = int(nombre)

def puissance(x,n):
    if n == 0:
        return 1
    else:
        return x * puissance(x,n-1)
    
x = 2    
resultat = puissance(x,nombre)
print("Le resultat de ",x," puissance ",nombre," est :",resultat)