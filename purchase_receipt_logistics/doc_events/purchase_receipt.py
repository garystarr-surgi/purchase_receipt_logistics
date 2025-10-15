import frappe
from frappe.utils import flt

def calculate_custom_quantities(doc, method):
    """
    Server-side logic:
    - received_qty = qty + custom_loose_quantity + rejected_qty
    - accepted_qty = received_qty - rejected_qty
    - total_qty = sum of received_qty across all items
    """
    total_qty = 0

    for item in doc.items:
        qty = flt(item.qty)
        loose_qty = flt(getattr(item, "custom_loose_quantity", 0))
        rejected_qty = flt(item.rejected_qty)

        received_qty = qty + loose_qty + rejected_qty
        accepted_qty = received_qty - rejected_qty

        item.received_qty = received_qty
        item.accepted_qty = accepted_qty

        total_qty += received_qty

    doc.total_qty = total_qty
