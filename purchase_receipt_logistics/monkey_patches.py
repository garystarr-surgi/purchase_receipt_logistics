import frappe
import erpnext.controllers.buying_controller as buying_controller

# Save reference to the original function
_original_validate = buying_controller.BuyingController.validate_accepted_rejected_qty

def patched_validate_accepted_rejected_qty(self):
    """
    Extend ERPNext's validate_accepted_rejected_qty to include custom loose quantity logic.
    """
    # Call the original validation first
    _original_validate(self)

    # Now apply custom logic for 'custom_loose_quantity'
    if hasattr(self, "items"):
        for row in self.items:
            qty = row.qty or 0
            loose_qty = getattr(row, "custom_loose_quantity", 0) or 0
            rejected_qty = row.rejected_qty or 0

            total_received_qty = qty + loose_qty + rejected_qty
            accepted_qty = total_received_qty - rejected_qty

            # Update the row values
            row.received_qty = total_received_qty
            row.accepted_qty = accepted_qty

    frappe.msgprint("✅ Custom loose quantity logic applied")

# Apply the patch
buying_controller.BuyingController.validate_accepted_rejected_qty = patched_validate_accepted_rejected_qty
