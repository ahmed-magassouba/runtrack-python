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


# class livre
class Livre(Auteur) :
    _titre = ""

    def __init__(self,nom,prenom,oeuvre,titre):
        Auteur.__init__(self, nom, prenom, oeuvre)
        self._titre = titre

    def print(self):
        print("Le titre du livre est", self._titre)
    
    def get_titre(self):
        return self._titre
    
    def set_titre(self, titre):
        self._titre = titre


nouveauLivre = Livre("Doe", "John", [], "Livre3")
