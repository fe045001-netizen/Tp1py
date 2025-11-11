from Contact import Contact

class Carnet:
    def __init__(self):
        self._contacts = []

    def ajouter(self, contact: Contact):
        self._contacts.append(contact)

    def recherche(self, fragment: str):
         fragment_lower = fragment.lower()
         return [c for c in self._contacts if fragment_lower in c.nom.lower()]


    def afficher_tous(self):
        for contact in self._contacts:
            print(contact)
            
if __name__ == "__main__":

   c = Carnet()
   c.ajouter(Contact("Amina Saidi", "0612345678", "amina@example.com"))
   c.ajouter(Contact("Youssef Belkhou", "0699988877", "youssef@example.com"))
   c.ajouter(Contact("Said Toumi", "0677001122", "said@example.com"))

   resultat = c.recherche("sa")

   for contact in resultat:
      print(contact.nom, contact.telephone)
