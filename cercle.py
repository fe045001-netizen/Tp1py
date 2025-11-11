from math import pi

class Cercle:
    def __init__(self, rayon: float):
        self.rayon = rayon  
    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self, valeur):
        if valeur <= 0:
            raise ValueError("Le rayon est négatif ou nul.")
        self._rayon = valeur

    @property
    def perimetre(self):
        return 2 * pi * self._rayon

    @property
    def surface(self):
        return pi * (self._rayon ** 2)
