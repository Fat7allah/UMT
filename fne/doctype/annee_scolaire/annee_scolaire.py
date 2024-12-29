import frappe
from frappe.model.document import Document

class AnneeScolaire(Document):
    def validate(self):
        # Vérifier que la date de fin est postérieure à la date de début
        if self.date_debut and self.date_fin:
            if self.date_fin <= self.date_debut:
                frappe.throw("La date de fin doit être postérieure à la date de début")

        # Si cette année est active, désactiver les autres années
        if self.active:
            frappe.db.sql("""
                UPDATE `tabAnnee Scolaire`
                SET active = 0
                WHERE name != %s
            """, self.name) 