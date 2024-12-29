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
            "fieldname": "profession",
            "label": _("Profession"),
            "fieldtype": "Data",
            "width": 200
        },
        {
            "fieldname": "total_membres",
            "label": _("Nombre de Membres"),
            "fieldtype": "Int",
            "width": 120
        },
        {
            "fieldname": "pourcentage",
            "label": _("Pourcentage"),
            "fieldtype": "Percent",
            "width": 100
        },
        {
            "fieldname": "cartes_valides",
            "label": _("Cartes Valides"),
            "fieldtype": "Int",
            "width": 120
        }
    ]

def get_data(filters):
    conditions = get_conditions(filters)
    
    data = frappe.db.sql("""
        SELECT 
            m.section,
            m.profession,
            COUNT(DISTINCT m.name) as total_membres,
            COUNT(DISTINCT CASE 
                WHEN ca.date_expiration >= CURDATE() AND ca.statut = 'Payée'
                THEN ca.name 
                ELSE NULL 
            END) as cartes_valides
        FROM 
            `tabMembre` m
            LEFT JOIN `tabCarte Adhesion` ca ON ca.membre = m.name
        WHERE
            {conditions}
        GROUP BY 
            m.section, m.profession
    """.format(conditions=conditions), filters, as_dict=1)
    
    # Calculer les totaux et pourcentages
    total_membres = sum(d.total_membres for d in data)
    for d in data:
        d.pourcentage = (d.total_membres / total_membres * 100) if total_membres else 0
    
    return data

def get_conditions(filters):
    conditions = "1=1"
    if filters.get("section"):
        conditions += " AND m.section = %(section)s"
    if filters.get("profession"):
        conditions += " AND m.profession = %(profession)s"
    if filters.get("niveau_etudes"):
        conditions += " AND m.niveau_etudes = %(niveau_etudes)s"
    return conditions 