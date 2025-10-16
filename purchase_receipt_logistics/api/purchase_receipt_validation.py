import frappe

@frappe.whitelist()
def validate_item_quantities(doc, method):
    """
    Ensure the standard ERPNext fields are set to pass the original validation,
    incorporating the loose quantity.
    """
    
    # 1. Calculate the final accepted quantity (Stock Qty + Loose Qty)
    stock_qty = doc.qty or 0
    loose_qty = doc.custom_loose_quantity or 0
    
    # 2. Update the document object IN PLACE to pass validation
    # This is the key override!
    doc.accepted_qty = stock_qty + loose_qty
    
    # Note: received_qty and rejected_qty are already set by the client script
    
    # After this function runs, the document continues to the original ERPNext validation.
    # The validation will now check:
    # doc.received_qty == (doc.accepted_qty) + doc.rejected_qty
    # And since your client script and this Python code ensure consistency, it should pass.
