# File: purchase_receipt.py
# Location: purchase_receipt_logistics/purchase_receipt_logistics/doc_events/purchase_receipt.py

import frappe
from frappe.utils import flt

def calculate_custom_quantities(doc, method):
    """
    Function executed via the 'before_validate' hook on Purchase Receipt.
    It recalculates received_qty and accepted_qty in Purchase Receipt Items
    to include 'custom_loose_quantity' and satisfy standard ERPNext validation.
    """
    
    frappe.logger("purchase_receipt_logistics").debug(f"Running custom validation for PR: {doc.name}")

    # Iterate through all items in the Purchase Receipt
    for item in doc.items:
        # 1. Get values safely using flt()
        qty = flt(item.qty)
        
        # NOTE: Ensure 'custom_loose_quantity' is the exact Fieldname you created
        loose_qty = flt(item.custom_loose_quantity)
        
        rejected_qty = flt(item.rejected_qty)

        # 2. Calculate the actual TOTAL physical quantity received based on your rule
        # Total Received Qty = Qty + Custom Loose Qty + Rejected Qty
        total_received_qty = qty + loose_qty + rejected_qty
        
        # Set the 'received_qty' field in the document item
        item.received_qty = total_received_qty

        # 3. Calculate Accepted Qty to satisfy standard ERPNext validation:
        # Standard Validation: Received Qty = Accepted Qty + Rejected Qty
        # Therefore: Accepted Qty = Received Qty - Rejected Qty
        item.accepted_qty = total_received_qty - rejected_qty
        
        # The system will now find that item.received_qty == item.accepted_qty + item.rejected_qty, 
        # allowing the document to be saved/submitted without the validation error.

    frappe.logger("purchase_receipt_logistics").debug(f"Finished custom quantity calculation for PR: {doc.name}")
