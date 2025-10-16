# --- Application Metadata ---
app_name = "purchase_receipt_logistics"
app_title = "Purchase Receipt Logistics"
app_publisher = "SurgiShop"
app_description = "Custom logic for Purchase Receipts including loose quantity calculation."
app_email = "gary.starr@surgishop.com"
app_license = "MIT"

# --- Document Events (Server-Side Hooks) ---
doc_events = {
    "Purchase Receipt": {
        "before_validate": "purchase_receipt_logistics.doc_events.purchase_receipt.calculate_custom_totals"
    },
    "Purchase Receipt Item": {
        "before_save": "purchase_receipt_logistics.api.purchase_receipt_validation.validate_item_quantities"
    }
}

# --- Monkey Patch Loader ---
# Import the module that applies patches at import time
import purchase_receipt_logistics.monkey_patches
