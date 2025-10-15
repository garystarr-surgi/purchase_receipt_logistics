let debounceTimer;

function calculate_quantities(frm, cdt, cdn) {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
        const row = locals[cdt][cdn]; // Safely resolve the row

        const qty = flt(row.qty || 0);
        const loose_qty = flt(row.custom_loose_quantity || 0);
        const rejected_qty = flt(row.rejected_qty || 0);

        const total_received_qty = qty + loose_qty + rejected_qty;
        const accepted_qty = total_received_qty - rejected_qty;

        frappe.model.set_value(cdt, cdn, 'received_qty', total_received_qty);
        frappe.model.set_value(cdt, cdn, 'accepted_qty', accepted_qty);

        frappe.show_alert({
            message: __('Quantities recalculated'),
            indicator: 'blue'
        }, 2);
    }, 200);
}

frappe.ui.form.on('Purchase Receipt Item', {
    qty: calculate_quantities,
    custom_loose_quantity: calculate_quantities,
    rejected_qty: calculate_quantities,

    form_render: function(frm, cdt, cdn) {
        calculate_quantities(frm, cdt, cdn);
    },

    purchase_receipt_items_add: function(frm, cdt, cdn) {
        calculate_quantities(frm, cdt, cdn);
    }
});

frappe.ui.form.on('Purchase Receipt', {
    refresh: function(frm) {
        frm.doc.items.forEach(item => {
            calculate_quantities(frm, item.doctype, item.name);
        });
    }
});
