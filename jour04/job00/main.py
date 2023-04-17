nombre = input("Veillez saisir un nombre entier : ")
nombre = int(nombre)

def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)
resultat =factoriel(nombre) 
   
print("le factoriel de",nombre,"est : ",resultat)