import frappe
from frappe.utils import flt

def calculate_custom_quantities(doc, method):
    """
    Hook: before_validate on Purchase Receipt.
    Adjusts received_qty and accepted_qty to include custom_loose_quantity.
    Ensures ERPNext validation: received_qty == accepted_qty + rejected_qty.
    """

    logger = frappe.logger("purchase_receipt_logistics")
    logger.debug(f"Running custom quantity logic for Purchase Receipt: {doc.name}")

    for item in doc.items:
        # Safely extract values
        qty = flt(item.qty)
        loose_qty = flt(getattr(item, "custom_loose_quantity", 0))
        rejected_qty = flt(item.rejected_qty)

        # Compute total received quantity
        total_received_qty = qty + loose_qty + rejected_qty
        item.received_qty = total_received_qty

        # Compute accepted quantity to satisfy ERPNext validation
        item.accepted_qty = total_received_qty - rejected_qty

        # Optional: log per item for debugging
        logger.debug(
            f"Item {item.item_code}: qty={qty}, loose={loose_qty}, rejected={rejected_qty}, "
            f"received={item.received_qty}, accepted={item.accepted_qty}"
        )

    logger.debug(f"Finished custom quantity logic for Purchase Receipt: {doc.name}")
