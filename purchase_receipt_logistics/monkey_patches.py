import frappe
import erpnext.controllers.buying_controller as buying_controller

# Save reference to the original function
_original_validate = buying_controller.BuyingController.validate_accepted_rejected_qty

def patched_validate_accepted_rejected_qty(self):
    """
    PRE-PATCH: Ensure quantities are consistent before the original validation check runs.
    """
    
    # Apply custom logic FIRST to ensure values pass the check
    if hasattr(self, "items"):
        for row in self.items:
            # We only need to modify the row if a custom field exists
            if hasattr(row, "custom_loose_quantity"):
                qty = row.qty or 0
                loose_qty = row.custom_loose_quantity or 0
                rejected_qty = row.rejected_qty or 0
                
                total_received_qty = qty + loose_qty + rejected_qty
                accepted_qty = total_received_qty - rejected_qty

                # Update the row values to satisfy the original validation check
                # Note: received_qty is usually set by client side, but we force it here
                row.received_qty = total_received_qty
                row.accepted_qty = accepted_qty

    # Now call the original validation. It should now pass without throwing the error.
    _original_validate(self) 
    
    # Only show msgprint if validation passed
    frappe.msgprint("✅ Custom loose quantity patch successful")

# Apply the patch
buying_controller.BuyingController.validate_accepted_rejected_qty = patched_validate_accepted_rejected_qty
