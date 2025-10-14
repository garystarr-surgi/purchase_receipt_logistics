import frappe
from frappe.utils import flt

def calculate_custom_quantities(doc, method):
    """
    Hook: validate on Purchase Receipt.
    Adjusts received_qty and accepted_qty to include custom_loose_quantity.
    Ensures ERPNext validation: received_qty == accepted_qty + rejected_qty.
    Also sets total_qty on parent to sum of received_qty.
    """

    logger = frappe.logger("purchase_receipt_logistics")
    logger.debug(f"Running custom quantity logic for Purchase Receipt: {doc.name}")

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

        logger.debug(
            f"Item {item.item_code}: qty={qty}, loose={loose_qty}, rejected={rejected_qty}, "
            f"received={received_qty}, accepted={accepted_qty}"
        )

    doc.total_qty = total_received_qty
    logger.debug(f"Set total_qty on Purchase Receipt {doc.name} to {doc.total_qty}")
