# class personne
class Personne :

    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    def get_nom(self):
        return self._nom
        
    def set_nom(self, nom):
        self._nom = nom

    def get_prenom(self):
        return self._prenom
    
    def set_prenom(self, prenom):
        self._prenom = prenom

# class auteur
class Auteur(Personne):
    _oeuvre = []

    def __init__(self, nom, prenom, oeuvre):
        Personne.__init__(self, nom, prenom)
        self._oeuvre = oeuvre

    def listerOeuvre(self):
        print("L'auteur est", self._prenom, self._nom + " et son oeuvre est", self._oeuvre)
        for i in self._oeuvre:
            print(self._oeuvre[i])

    def ecrireUnLivre(self, titre):
        self._oeuvre.append(titre)
        print("L'auteur a écrit un nouveau livre", titre)

    def get_oeuvre(self):
        return self._oeuvre
    
    def set_oeuvre(self, oeuvre):
        self._oeuvre = oeuvre

# class client
class Client(Personne):
    collection = {
        "livre":"",
    }
    def __init__(self, nom, prenom, collection):
        Personne.__init__(self, nom, prenom)
        self.collection = collection

   


# class Bibliotheque
class Bibliotheque:

    _nom = ""
    _catalogue = {
        "livre":"",
        "quantite":0
    }

    def __init__(self, nom, catalogue):
        self._nom = nom
        self._catalogue = catalogue

    def acheterLivre(self, livre, quantite):
        self._catalogue["livre"] = livre
        self._catalogue["quantite"] = quantite

    def inventaire(self):
        print("Le catalogue de la bibliotheque est", self._catalogue)

    def louer(self):
       client = Client("Doe", "John", "livre1")
       livre="livre5"
       for i in self._catalogue:
           if self._catalogue["livre"] == livre and self._catalogue["quantite"] > 0:
               print("Le livre", livre, "est disponible")
               self._catalogue["quantite"] -= 1
           else:
               print("Le livre", livre, "n'est pas disponible")
    
    def rendreLivres(self):
        client = Client("Doe", "John", "livre1")
        livre="livre5"
        for i in self._catalogue:
            if self._catalogue["livre"] == livre:
                print("Le livre", livre, "est disponible")
                self._catalogue["quantite"] += 1
            else:
                print("Le livre", livre, "n'est pas disponible")