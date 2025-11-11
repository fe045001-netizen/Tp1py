from datetime import datetime

class JournalTaches:
    def __enter__(self):
        self._fichier = open("journal.txt", "a", encoding="utf-8")
        return self

    def enregistrer(self, tache: str):
        horodatage = datetime.now().isoformat()
        self._fichier.write(f"[{horodatage}] {tache}\n")

    def __exit__(self, exc_type, exc_value, traceback):  self._fichier.close()
from journal import JournalTaches
from time import sleep

with JournalTaches() as journal:
    journal.enregistrer("Préparer la réunion du projet X")
    sleep(1)
    journal.enregistrer("Faire la revue de code")
    sleep(1)
    journal.enregistrer("Envoyer le rapport hebdomadaire")