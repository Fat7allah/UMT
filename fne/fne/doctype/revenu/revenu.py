import frappe
from frappe.model.document import Document

class Revenu(Document):
    def validate(self):
        # Vérifier que le montant est positif
        if self.montant <= 0:
            frappe.throw("Le montant doit être positif")

        # Si type de revenu est carte d'adhésion, vérifier que la carte existe
        if self.type_revenu == "Carte d'Adhésion" and not self.carte_adhesion:
            frappe.throw("Veuillez sélectionner une carte d'adhésion")

        # Vérifier que l'année scolaire est active
        annee_scolaire = frappe.get_doc("Annee Scolaire", self.annee_scolaire)
        if not annee_scolaire.active:
            frappe.throw("L'année scolaire sélectionnée n'est pas active") 