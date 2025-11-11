
class Article:
    def __init__(self, reference: str, designation: str, prix_ht: float, stock: int):
        self.reference = reference
        self.designation = designation
        self.prix_ht = prix_ht
        self.stock = stock

    def valeur_stock(self) -> float:
        return self.prix_ht * self.stock

    def __str__(self):
        return f"Réf {self.reference} — {self.designation} : {self.stock} unités à {self.prix_ht:.2f} € HT"
