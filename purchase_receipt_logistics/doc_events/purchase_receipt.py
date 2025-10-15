import frappe
from frappe.utils import flt

def calculate_custom_quantities(doc, method):
    """
    Step 1: Set received_qty = qty + custom_loose_quantity + rejected_qty
    """
    for item in doc.items:
        qty = flt(item.qty)
        loose_qty = flt(getattr(item, "custom_loose_quantity", 0))
        rejected_qty = flt(item.rejected_qty)

        item.received_qty = qty + loose_qty + rejected_qty
