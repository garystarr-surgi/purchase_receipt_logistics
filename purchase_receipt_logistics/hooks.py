# --- Application Metadata ---
app_name = "purchase_receipt_logistics"
app_title = "Purchase Receipt Logistics"
app_publisher = "SurgiShop"
app_description = "Custom logic for Purchase Receipts including loose quantity calculation."
app_email = "gary.starr@surgishop.com"
app_license = "MIT"

# --- Document Events (Server-Side Hooks) ---
doc_events = {
    # Hook the Purchase Receipt to calculate totals and enforce custom logic
    "Purchase Receipt": {
        "before_validate": "purchase_receipt_logistics.doc_events.purchase_receipt.calculate_custom_totals"
    },
    # Optional: Hook Purchase Receipt Item if you want per-row validation
    "Purchase Receipt Item": {
        "before_save": "purchase_receipt_logistics.api.purchase_receipt_validation.validate_item_quantities"
    }
}

# --- Monkey Patch Loader ---
from purchase_receipt_logistics.patches import patched_validate_accepted_rejected_qty
