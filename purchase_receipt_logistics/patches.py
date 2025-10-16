def apply_patch():
    import erpnext.stock.doctype.purchase_receipt.purchase_receipt as pr_module

    def patched_validate(self):
        print("✅ Monkey-patch is active")
        for item in self.items:
            expected_received = item.qty + (item.custom_loose_quantity or 0) + item.rejected_qty
            if abs(item.received_qty - expected_received) > 0.001:
                frappe.throw(
                    f"Row {item.idx}: Received Qty must equal Qty + Loose + Rejected Qty. Found {item.received_qty}, expected {expected_received}"
                )

    pr_module.PurchaseReceipt.validate_accepted_rejected_qty = patched_validate
