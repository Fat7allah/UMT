app_name = "fne"
app_title = "FNE"
app_publisher = "Your Name"
app_description = "Gestion des membres FNE"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "your@email.com"
app_license = "MIT"

# Document Events
doc_events = {
    "Membre": {
        "validate": "fne.fne.doctype.membre.membre.validate"
    },
    "Carte Adhesion": {
        "validate": "fne.fne.doctype.carte_adhesion.carte_adhesion.validate"
    }
} 