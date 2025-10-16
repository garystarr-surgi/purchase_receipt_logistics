# --- Application Metadata ---
app_name = "purchase_receipt_logistics"
app_title = "Purchase Receipt Logistics"
app_publisher = "SurgiShop"
app_description = "Custom logic for Purchase Receipts including loose quantity calculation."
app_email = "gary.starr@surgishop.com"
app_license = "MIT"

# --- Server Hooks ---
doc_events = {
    "Purchase Receipt": {
        "before_validate": "purchase_receipt_logistics.doc_events.purchase_receipt.calculate_custom_totals"
    }
}

# --- Class Overrides ---
override_doctype_class = {
    "Purchase Receipt": "purchase_receipt_logistics.overrides.purchase_receipt.CustomPurchaseReceipt"
}
