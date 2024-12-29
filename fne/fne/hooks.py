app_name = "fne"
app_title = "FNE"
app_publisher = "Your Name"
app_description = "Gestion des membres FNE"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "your@email.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_js = ["/assets/fne/js/fne.bundle.js"]
app_include_css = ["/assets/fne/css/fne.bundle.css"]

# include js, css files in header of web template
web_include_js = ["/assets/fne/js/fne.bundle.js"]
web_include_css = ["/assets/fne/css/fne.bundle.css"]

# Document Events
doc_events = {
    "Membre": {
        "validate": "fne.fne.doctype.membre.membre.validate"
    },
    "Carte Adhesion": {
        "validate": "fne.fne.doctype.carte_adhesion.carte_adhesion.validate"
    }
}

# Jinja
# ----------

website_route_rules = [
    {"from_route": "/fne", "to_route": "Membre"}
] 