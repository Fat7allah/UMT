import frappe
from frappe.model.document import Document

class Membre(Document):
    def before_save(self):
        # Vérifier si le membre existe déjà avec le même email
        if self.email:
            existing_member = frappe.db.exists("Membre", {
                "email": self.email,
                "name": ("!=", self.name)
            })
            if existing_member:
                frappe.throw("Un membre avec cet email existe déjà")

    def validate(self):
        # Validation du numéro de téléphone
        if self.telephone and not self.telephone.isdigit():
            frappe.throw("Le numéro de téléphone ne doit contenir que des chiffres") 