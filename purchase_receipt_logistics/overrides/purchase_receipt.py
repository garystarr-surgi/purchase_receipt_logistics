import frappe
from erpnext.stock.doctype.purchase_receipt.purchase_receipt import PurchaseReceipt

class PurchaseReceipt(PurchaseReceipt):
    def validate_accepted_rejected_qty(self):
        # Run ERPNext's original validation first
        super().validate_accepted_rejected_qty()

        # Then apply your custom logic to include loose quantity
        for item in self.items:
            expected_received = item.qty + (item.custom_loose_quantity or 0) + item.rejected_qty
            if abs(item.received_qty - expected_received) > 0.001:
                frappe.throw(
                    f"Row {item.idx}: Received Qty must equal Qty + Loose + Rejected Qty. Found {item.received_qty}, expected {expected_received}"
                )
