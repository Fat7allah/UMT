import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {
            "fieldname": "section",
            "label": _("Section"),
            "fieldtype": "Link",
            "options": "Section",
            "width": 150
        },
        {
            "fieldname": "total_cartes",
            "label": _("Total Cartes"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "cartes_payees",
            "label": _("Cartes Payées"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "cartes_non_payees",
            "label": _("Cartes Non Payées"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "montant_total",
            "label": _("Montant Total"),
            "fieldtype": "Currency",
            "width": 120
        }
    ]

def get_data(filters):
    conditions = get_conditions(filters)
    
    data = frappe.db.sql("""
        SELECT 
            r.section,
            COUNT(ca.name) as total_cartes,
            SUM(CASE WHEN ca.statut = 'Payée' THEN 1 ELSE 0 END) as cartes_payees,
            SUM(CASE WHEN ca.statut = 'Non payée' THEN 1 ELSE 0 END) as cartes_non_payees,
            SUM(CASE WHEN ca.statut = 'Payée' THEN r.montant ELSE 0 END) as montant_total
        FROM 
            `tabCarte Adhesion` ca
            LEFT JOIN `tabRevenu` r ON r.carte_adhesion = ca.name
        WHERE
            {conditions}
        GROUP BY 
            r.section
    """.format(conditions=conditions), filters, as_dict=1)
    
    return data

def get_conditions(filters):
    conditions = "1=1"
    if filters.get("section"): 
        conditions += " AND r.section = %(section)s"
    if filters.get("annee_scolaire"):
        conditions += " AND r.annee_scolaire = %(annee_scolaire)s"
    if filters.get("from_date"):
        conditions += " AND ca.date_adhesion >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND ca.date_adhesion <= %(to_date)s"
    return conditions 