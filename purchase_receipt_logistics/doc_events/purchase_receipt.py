import frappe
from frappe.utils import flt

def calculate_custom_quantities(doc, method):
    frappe.msgprint("Hook is running")
    """
    Hook: before_validate on Purchase Receipt.
    Sets received_qty = qty + custom_loose_quantity + rejected_qty.
    Sets accepted_qty = received_qty - rejected_qty.
    Updates total_qty on parent.
    """

    frappe.log_error("Hook triggered", f"Purchase Receipt: {doc.name}")

    total_received_qty = 0

    for item in doc.items:
        qty = flt(item.qty)
        loose_qty = flt(getattr(item, "custom_loose_quantity", 0))
        rejected_qty = flt(item.rejected_qty)

        received_qty = qty + loose_qty + rejected_qty
        accepted_qty = received_qty - rejected_qty

        item.received_qty = received_qty
        item.accepted_qty = accepted_qty

        total_received_qty += received_qty

    doc.total_qty = total_received_qty
