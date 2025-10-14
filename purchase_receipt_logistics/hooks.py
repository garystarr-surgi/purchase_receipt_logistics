# --- Application Metadata Required by Frappe ---
# Defines the official title of the app for display in the module/app list.
app_name = "purchase_receipt_logistics"
app_title = "Purchase Receipt Logistics"

# --- ERPNext Site Installation Hooks ---
# This hook is critical for the app to appear in the site's app list for installation.
get_desk_pages = {
    "module_name": "purchase_receipt_logistics.config.desktop"
}

# --- Event Handlers (Your Custom Logic) ---
# Set up event handlers that trigger custom code execution
doc_events = {
    "Purchase Receipt": {
        # This tells Frappe to run the specified Python function
        # before the document passes its standard system validation.
        "before_validate": "purchase_receipt_logistics.doc_events.purchase_receipt.calculate_custom_quantities"
    }
}
