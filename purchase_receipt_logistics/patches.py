import frappe
import erpnext.controllers.buying_controller as buying_controller

def patched_validate_accepted_rejected_qty(self):
    frappe.msgprint("✅ Monkey-patch active: default validation suppressed")
    # Add custom validation logic here if needed
    return

# Apply the patch
buying_controller.BuyingController.validate_accepted_rejected_qty = patched_validate_accepted_rejected_qty
