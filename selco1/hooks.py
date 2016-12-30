# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "selco1"
app_title = "selco"
app_publisher = "Kishor"
app_description = "selco customizations"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "poorvi@selco-india.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/selco1/css/selco1.css"
# app_include_js = "/assets/selco1/js/selco1.js"

# include js, css files in header of web template
# web_include_css = "/assets/selco1/css/selco1.css"
# web_include_js = "/assets/selco1/js/selco1.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#    "Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "selco1.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "selco1.install.before_install"
# after_install = "selco1.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "selco1.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#     "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#     "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
     "Customer": {
         "validate": "selco1.selco.doctype.selco_customizations.selco_customizations.selco_customer_validations"                        
    },
 }

# doc_events = {
#     "*": {
#         "on_update": "method",
#         "on_cancel": "method",
#         "on_trash": "method"
#    }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#     "all": [
#         "selco1.tasks.all"
#     ],
#     "daily": [
#         "selco1.tasks.daily"
#     ],
#     "hourly": [
#         "selco1.tasks.hourly"
#     ],
#     "weekly": [
#         "selco1.tasks.weekly"
#     ]
#     "monthly": [
#         "selco1.tasks.monthly"
#     ]
# }

# Testing
# -------

# before_tests = "selco1.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
#     "frappe.desk.doctype.event.event.get_events": "selco1.event.get_events"
# }
