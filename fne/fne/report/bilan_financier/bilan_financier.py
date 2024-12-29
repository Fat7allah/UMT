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
            "fieldname": "total_revenus",
            "label": _("Total Revenus"),
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "fieldname": "total_depenses",
            "label": _("Total Dépenses"),
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "fieldname": "solde",
            "label": _("Solde"),
            "fieldtype": "Currency",
            "width": 120
        }
    ]

def get_data(filters):
    conditions = get_conditions(filters)
    
    revenus = frappe.db.sql("""
        SELECT 
            section,
            SUM(montant) as total_revenus
        FROM 
            `tabRevenu`
        WHERE
            {conditions}
        GROUP BY 
            section
    """.format(conditions=conditions), filters, as_dict=1)
    
    depenses = frappe.db.sql("""
        SELECT 
            section,
            SUM(montant) as total_depenses
        FROM 
            `tabDepense`
        WHERE
            {conditions}
        GROUP BY 
            section
    """.format(conditions=conditions), filters, as_dict=1)
    
    # Fusionner les résultats
    sections = list(set([r.section for r in revenus] + [d.section for d in depenses]))
    data = []
    
    for section in sections:
        revenu = next((r for r in revenus if r.section == section), {"total_revenus": 0})
        depense = next((d for d in depenses if d.section == section), {"total_depenses": 0})
        
        data.append({
            "section": section,
            "total_revenus": revenu.get("total_revenus", 0),
            "total_depenses": depense.get("total_depenses", 0),
            "solde": revenu.get("total_revenus", 0) - depense.get("total_depenses", 0)
        })
    
    return data

def get_conditions(filters):
    conditions = "1=1"
    if filters.get("section"):
        conditions += " AND section = %(section)s"
    if filters.get("annee_scolaire"):
        conditions += " AND annee_scolaire = %(annee_scolaire)s"
    if filters.get("from_date"):
        conditions += " AND date >= %(from_date)s"
    if filters.get("to_date"):
        conditions += " AND date <= %(to_date)s"
    return conditions 