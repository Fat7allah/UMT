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
app_include_css = "/assets/css/fne.css"
app_include_js = "/assets/js/fne.js"

# include js, css files in header of web template
web_include_css = "/assets/css/fne.css"
web_include_js = "/assets/js/fne.js"

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

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "fne/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"} 