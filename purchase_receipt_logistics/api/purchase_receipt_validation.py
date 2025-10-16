import frappe

# This function will run for every Purchase Receipt Item row during the server's validation stage.
@frappe.whitelist()
def validate_item_quantities(doc, method):
    """
    Overrides ERPNext's standard quantity check to include custom_loose_quantity.
    This logic should match your client-side calculation to ensure consistency.
    """
    
    # 1. Skip if the DocType is not Purchase Receipt Item (safety check)
    if doc.doctype != "Purchase Receipt Item":
        return

    # 2. Get quantities, ensuring your custom field is present
    qty = doc.qty or 0
    loose_qty = doc.custom_loose_quantity or 0
    rejected_qty = doc.rejected_qty or 0
    
    # Calculate what the total received quantity SHOULD be
    expected_received_qty = qty + loose_qty + rejected_qty
    
    # 3. Perform the check
    if doc.received_qty != expected_received_qty:
        # If there is a mismatch, use frappe.throw to display a clean error message
        # This is the original ERPNext check, but modified to reflect your logic
        frappe.throw(
            f"Row #{doc.idx}: Received Qty ({doc.received_qty}) must equal Stock Qty ({qty}) + Loose Qty ({loose_qty}) + Rejected Qty ({rejected_qty}). Total expected: {expected_received_qty}"
        )
