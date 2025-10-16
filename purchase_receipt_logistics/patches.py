import erpnext.controllers.buying_controller as buying_controller

def patched_validate_accepted_rejected_qty(self):
    print("✅ Monkey-patch active: default validation suppressed")
    # Optionally add your own validation logic here
    pass  # Suppresses ERPNext's default check entirely

# Apply the patch
buying_controller.BuyingController.validate_accepted_rejected_qty = patched_validate_accepted_rejected_qty
