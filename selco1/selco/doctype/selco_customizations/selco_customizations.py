# -*- coding: utf-8 -*-
# Copyright (c) 2015, Kishor and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class SelcoCustomizations(Document):
    pass
@frappe.whitelist()
def test_selco_cust(doc,method):
    frappe.msgprint("Hello success baby")

@frappe.whitelist()
def selco_customer_validations(doc,method):
    if not ( doc.customer_contact_number or doc.landline_mobile_2 ):
        frappe.throw("Enter either mobile number or landline number. \n Both cannot be left blank")
    var4 = frappe.db.get_value("Customer", {"customer_contact_number": (doc.customer_contact_number)})
    var5 = unicode(var4) or u''
    var6 = frappe.db.get_value("Customer", {"customer_contact_number": (doc.customer_contact_number)}, "customer_name")
    if var5 != "None" and doc.name != var5:
        frappe.throw("Customer with contact no " + doc.customer_contact_number + " already exists \n Customer ID : " + var5 + "\n Customer Name : " + var6)

@frappe.whitelist()
def selco_issue_updates(doc,method):
    from frappe.utils import now,now_datetime
    if doc.workflow_state =="Complaint Closed By Branch":
        doc.status = "Closed"
        doc.resolution_date = now()

@frappe.whitelist()
def selco_warranty_claim_updates(doc,method):
    if doc.workflow_state =="Dispatched From Godown":
        doc.status = "Closed"
