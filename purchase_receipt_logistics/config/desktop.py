# This file defines the custom app's module icon and links on the Frappe Desk.
from frappe import _

def get_desk_pages():
    """Defines the structure of the module page on the Frappe Desk."""
    return {
        # Unique name of the module/app
        "module_name": "Purchase Receipt Logistics",

        # Module's color (hex code)
        "color": "#3498db",

        # Icon for the module (using a standard Frappe icon class)
        "icon": "octicon octicon-package",

        # The display label for the module on the desktop
        "label": _("Purchase Receipt Logistics"),

        # Settings/Configuration links within the module page
        "settings": [
            {
                "label": _("Core Documents"),
                "items": [
                    {
                        "type": "doctype",
                        "name": "Purchase Receipt",
                        "label": _("View Purchase Receipts")
                    }
                ]
            }
        ],

        # Quick access links within the module page
        "links": [
            {
                "label": _("Logistics Reports"),
                "items": [
                    {
                        "type": "report",
                        "name": "Incoming Items",
                        "doctype": "Purchase Receipt"
                    }
                ]
            }
        ]
    }

