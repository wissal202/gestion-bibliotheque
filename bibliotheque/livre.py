class Livre:
"""Un livre du catalogue."""
def __init__(self, isbn, titre, auteur):
self.isbn = isbn
self.titre = titre
self.auteur = auteur
def __str__(self):
   marque = "+" if self.disponible else "-"
   return f "[{marque}] {self.titre} - {self.auteur}"