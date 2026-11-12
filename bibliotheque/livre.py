class Livre:
"""Un livre du catalogue."""
def __init__(self, isbn, titre, auteur):
self.isbn = isbn
self.titre = titre
self.auteur = auteur
def __str__(self):
   status = "disponible" if self.disponible else "emprunté"
   return f "{self.titre} par {self.auteur} (ISBN {self.isbn}) - {status}"
   