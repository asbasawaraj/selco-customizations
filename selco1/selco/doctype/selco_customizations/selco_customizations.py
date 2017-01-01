# -*- coding: utf-8 -*-
# Copyright (c) 2015, Kishor and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import operator

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

@frappe.whitelist()
def selco_purchase_receipt_updates(doc,method):
    selco_cost_center = frappe.db.get_value("Warehouse",doc.godown,"cost_center")
    for d in doc.get('items'):
        d.cost_center = selco_cost_center
    for d in doc.get('taxes'):
        d.cost_center = selco_cost_center

    po_list = []
    po_list_date = []
    for item_selco in doc.items:
        if item_selco.prevdoc_docname not in po_list:
            po_list.append(item_selco.prevdoc_docname)
            po_list_date.append(frappe.utils.formatdate(frappe.db.get_value('Purchase Order', item_selco.prevdoc_docname, 'transaction_date'),"dd-MM-yyyy"))
    doc.selco_list_of_po= ','.join([str(i) for i in po_list])
    doc.selco_list_of_po_date= ','.join([str(i) for i in po_list_date])
        #End of Insert By basawaraj On 7th september for printing the list of PO when PR is done by importing items from multiple PO

@frappe.whitelist()
def selco_stock_entry_updates(doc,method):
	#Inserted By basawaraj On 21st Dec
	selco_cost_center = frappe.db.get_value("Warehouse",doc.to_warehouse,"cost_center")
	#frappe.msgprint(_("{0} subscribers added").format(selco_cost_center))
	for d in doc.get('items'):
		d.cost_center = selco_cost_center
	      #End of Insert By basawaraj On 21st Dec

@frappe.whitelist()
def selco_material_request_updates(doc,method):
	#Start of Insert By Poorvi on 10-09-2016 for IBM value calculation
	selco_ibm_value = 0
	#if doc.workflow_state =="Approval Pending by SM - IBM":
	for idx,selco_item in enumerate(doc.items):
		selco_rate = frappe.db.sql("""select price_list_rate
			from `tabItem Price`
			where item_code = %s and price_list = "Branch Sales" """,(selco_item.item_code))
		if selco_rate:
			var1=selco_rate[0][0]
		else:
			var1=0
		doc.items[idx].selco_rate =var1
		selco_ibm_value = selco_ibm_value + (var1 * selco_item.qty)
	doc.selco_ibm_value = selco_ibm_value
	#doc.items.sort(key = lambda x: x.item_code)
	doc.items.sort(key=operator.attrgetter("item_code"), reverse=False)
