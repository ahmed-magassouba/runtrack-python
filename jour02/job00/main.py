class Personne :
  _nom=""
  _prenom=""

  def __init__(self, nom, prenom):
    self._nom = nom
    self._prenom = prenom


  def SePresenter(self):
    print("Bonjour, je m'appelle", self._prenom, self._nom)

  # getter nom
  def get_nom(self):
    return self._nom
    
  # setter nom
  def set_nom(self, nom):
    self._nom = nom

  # getter prenom
  def get_prenom(self):
    return self._prenom
    
  # setter prenom
  def set_prenom(self, prenom):
    self._prenom = prenom

user = Personne("Doe", "John")
user.set_prenom("Ahmed")

user.SePresenter()