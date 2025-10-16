import frappe
import erpnext.controllers.buying_controller as buying_controller

def patched_validate_accepted_rejected_qty(self):
    print("✅ Monkey-patch on BuyingController is active")

    for item in self.items:
        expected_received = item.qty + (item.custom_loose_quantity or 0) + item.rejected_qty
        if abs(item.received_qty - expected_received) > 0.001:
            frappe.throw(
                f"Row {item.idx}: Received Qty must equal Qty + Loose + Rejected Qty. Found {item.received_qty}, expected {expected_received}"
            )

buying_controller.BuyingController.validate_accepted_rejected_qty = patched_validate_accepted_rejected_qty
