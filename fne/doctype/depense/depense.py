import frappe
from frappe.model.document import Document

class Depense(Document):
    def validate(self):
        # Vérifier que le montant est positif
        if self.montant <= 0:
            frappe.throw("Le montant doit être positif")

        # Vérifier que l'année scolaire est active
        annee_scolaire = frappe.get_doc("Annee Scolaire", self.annee_scolaire)
        if not annee_scolaire.active:
            frappe.throw("L'année scolaire sélectionnée n'est pas active")

        # Vérifier que la pièce jointe est présente
        if not self.piece_jointe:
            frappe.throw("Une pièce justificative est requise") 