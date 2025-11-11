from cercle import Cercle

c = Cercle(3)
print(c.perimetre)  # 2πr
print(c.surface)    # πr²

try:
    c.rayon = -5
except ValueError as e:
    print("Erreur capturée :", e)