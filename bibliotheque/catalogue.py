def rechercher_par_titre(self, mot):
    mot = mot.lower()
    return [l for l in self._livres if mot in l.titre.lower()]