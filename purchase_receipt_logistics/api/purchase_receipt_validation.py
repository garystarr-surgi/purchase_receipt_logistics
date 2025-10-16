# Inside validate_item_quantities(doc, method):
# ...
stock_qty = doc.qty or 0
loose_qty = doc.custom_loose_quantity or 0

# THIS LINE IS THE KEY TO BYPASSING THE CORE ERPNEXT ERROR:
doc.accepted_qty = stock_qty + loose_qty 
# ...
