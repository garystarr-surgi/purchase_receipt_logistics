# --- Application Metadata ---

app_name = "purchase_receipt_logistics"
app_title = "Purchase Receipt Logistics"
app_publisher = "SurgiShop"
app_description = "Custom logic for Purchase Receipts including loose quantity calculation."
app_email = "gary.starr@surgishop.com"
app_license = "MIT"

fixtures = ["Client Script"]

# --- Desk Pages (optional, if you have a config.desktop module) ---
get_desk_pages = {
    "module_name": "purchase_receipt_logistics.config.desktop"
}

# --- Event Hooks ---
doc_events = {
    "Purchase Receipt": {
        # This hook ensures your custom quantity logic runs during validation
        "before_validate": "purchase_receipt_logistics.doc_events.purchase_receipt.calculate_custom_quantities"
    }
}
