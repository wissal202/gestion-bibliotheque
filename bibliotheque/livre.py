
class Livre:
    """Un livre du catalogue."""

    def __init__(self, isbn, titre, auteur):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def __str__(self):
        marque = "+" if self.disponible else "-"
        return f"[{marque}] {self.titre} par {self.auteur} (ISBN {self.isbn})"
