let debounceTimer;

function calculate_quantities(frm, cdt, cdn) {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
        const row = locals[cdt][cdn];

        const qty = flt(row.qty || 0);
        const loose_qty = flt(row.custom_loose_quantity || 0);
        const rejected_qty = flt(row.rejected_qty || 0);

        const received_qty = qty + loose_qty + rejected_qty;
        const accepted_qty = received_qty - rejected_qty;

        frappe.model.set_value(cdt, cdn, 'received_qty', received_qty);
        frappe.model.set_value(cdt, cdn, 'accepted_qty', accepted_qty);

        update_total_qty(frm);
    }, 200);
}

function update_total_qty(frm) {
    const total = frm.doc.items.reduce((sum, item) => {
        return sum + flt(item.received_qty || 0);
    }, 0);
    frm.set_value('total_qty', total);
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
