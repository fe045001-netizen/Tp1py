class CompteurPage:
    total_visites = 0

    def __init__(self, url: str):
        self.url = url
        CompteurPage.total_visites += 1

    def afficher_stats(self) -> str:
        """Retourne une phrase avec le nombre de visites globales."""
        return f"Page {self.url} — visites globales : {CompteurPage.total_visites}"
from compteur_page import CompteurPage

p1 = CompteurPage("https://example.com/")
p2 = CompteurPage("https://example.com/blog")
p3 = CompteurPage("https://example.com/contact")

for p in (p1, p2, p3):
    print(p.afficher_stats())