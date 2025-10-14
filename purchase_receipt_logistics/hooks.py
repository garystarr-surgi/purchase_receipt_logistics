# File: hooks.py
# Location: purchase_receipt_logistics/purchase_receipt_logistics/hooks.py

# Set up event handlers that trigger custom code execution
doc_events = {
    "Purchase Receipt": {
        # This tells Frappe to run the specified Python function
        # before the document passes its standard system validation.
        "before_validate": "purchase_receipt_logistics.doc_events.purchase_receipt.calculate_custom_quantities"
    }
}
