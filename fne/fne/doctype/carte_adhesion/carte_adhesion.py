import frappe
from frappe.model.document import Document
from datetime import datetime, date

class CarteAdhesion(Document):
    def before_save(self):
        # Générer automatiquement le numéro de carte
        if not self.numero_carte:
            annee = datetime.now().year
            count = frappe.db.count('Carte Adhesion', {
                'creation': ('between', (f'{annee}-01-01', f'{annee}-12-31'))
            })
            self.numero_carte = f"CA{annee}{str(count + 1).zfill(4)}"

    def validate(self):
        # Vérifier que la date d'expiration est postérieure à la date d'adhésion
        if self.date_adhesion and self.date_expiration:
            if self.date_expiration <= self.date_adhesion:
                frappe.throw("La date d'expiration doit être postérieure à la date d'adhésion") 