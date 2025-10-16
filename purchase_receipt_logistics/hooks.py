# --- Application Metadata ---
app_name = "purchase_receipt_logistics"
app_title = "Purchase Receipt Logistics"
app_publisher = "SurgiShop"
app_description = "Custom logic for Purchase Receipts including loose quantity calculation."
app_email = "gary.starr@surgishop.com"
app_license = "MIT"

# --- Document Events (Server-Side Hooks) ---
doc_events = {
    # Hook the 'Purchase Receipt Item' DocType to run custom validation
    "Purchase Receipt Item": {
        # The 'validate' event runs when the document is saved/submitted.
        # This hook runs the Python function to include 'custom_loose_quantity' 
        # in the check, preventing the ERPNext error.
        "before_validate": "purchase_receipt_logistics.api.purchase_receipt_validation.validate_item_quantities"
    }
}

# --- Server Hooks ---
# doc_events = {
#    "Purchase Receipt": {
#        "before_validate": "purchase_receipt_logistics.doc_events.purchase_receipt.calculate_custom_totals"
#    }
# }

# --- Class Overrides ---
# override_doctype_class = {
#    "Purchase Receipt": "purchase_receipt_logistics.overrides.purchase_receipt.PurchaseReceipt"
# }

# --- Monkey Patch Loader ---
# from purchase_receipt_logistics.patches import patched_validate_accepted_rejected_qty
