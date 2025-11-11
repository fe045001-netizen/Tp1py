# inventaire.py

from article import Article

# Création de trois articles
a1 = Article("A001", "Clé USB 16Go", 5.50, 100)
a2 = Article("A002", "Souris sans fil", 15.90, 50)
a3 = Article("A003", "Clavier mécanique", 45.00, 30)

articles = [a1, a2, a3]

for article in articles:
    print(article)

total = sum(a.valeur_stock() for a in articles)
print(f"Valeur d’inventaire : {total:.2f} €")

