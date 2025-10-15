# purchase_receipt.py
import frappe
from frappe.utils import flt

def calculate_custom_quantities(doc, method):
    # This runs on before_validate and ensures the final saved values are correct.
    total_received_qty = 0

    for item in doc.items:
        # Calculate received_qty and accepted_qty for the database lock-in
        qty = flt(item.qty)
        loose_qty = flt(getattr(item, "custom_loose_quantity", 0))
        rejected_qty = flt(item.rejected_qty)

        received_qty = qty + loose_qty + rejected_qty
        accepted_qty = received_qty - rejected_qty

        # Lock in values for the child table
        item.received_qty = received_qty
        item.accepted_qty = accepted_qty

        total_received_qty += received_qty

    # Lock in value for the parent (header field)
    doc.total_qty = total_received_qty
