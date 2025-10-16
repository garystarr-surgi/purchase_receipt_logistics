import frappe
from frappe.utils import flt

def calculate_custom_totals(doc, method):
    """
    Totals loose, rejected, and received quantities across all items.
    Sets:
    - custom_total_loose_quantity
    - custom_total_rejected_quantity
    - custom_total_received
    """
    total_loose = 0
    total_rejected = 0
    total_received = 0

    for item in doc.items:
        qty = flt(item.qty)
        loose = flt(getattr(item, "custom_loose_quantity", 0))
        rejected = flt(item.rejected_qty)

        received = qty + loose + rejected

        item.received_qty = received
        item.accepted_qty = received - rejected

        total_loose += loose
        total_rejected += rejected
        total_received += received

    doc.custom_total_loose_quantity = total_loose
    doc.custom_total_rejected_quantity = total_rejected
    doc.custom_total_received = total_received
