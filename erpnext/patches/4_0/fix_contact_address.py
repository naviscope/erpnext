import frappe

def execute():
	frappe.reload_doc("website", "doctype", "contact_us_settings")
	address = frappe.db.get_value("Contact Us Settings", None, "address")
	if address:
		address = frappe.doc("Address", address)
		contact = frappe.bean("Contact Us Settings", "Contact Us Settings")
		for f in ("address_title", "address_line1", "address_line2", "city", "state", "country", "pincode"):
			contact.doc.fields[f] = address.get(f)
		
		contact.save()