# contact.py
class Contact:
    def __init__(self, nom: str, telephone: str, email: str):
        self.nom = nom
        self.telephone = telephone
        self.email = email

    @property
    def initiale(self) -> str:
        return self.nom[0].upper()
