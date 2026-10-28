import frappe


def validate_library_member(doc, method=None):
    if doc.email_address and "@" not in doc.email_address:
        frappe.throw("Please enter a valid email address.")


def validate_library_membership(doc, method=None):
    if doc.from_date and doc.to_date:
        if doc.to_date < doc.from_date:
            frappe.throw("To Date cannot be before From Date.")


def validate_library_transaction(doc, method=None):
    membership = frappe.db.exists(
        "Library Membership",
        {
            "library_member": doc.library_member,
            "docstatus": 1,
            "from_date": ("<=", doc.date),
            "to_date": (">=", doc.date),
        },
    )

    if not membership:
        frappe.throw("There is no active membership for this member.")

    if doc.type == "Issue" and doc.article:
        status = frappe.db.get_value("Article", doc.article, "status")
        if status != "Available":
            frappe.throw("This article is not available for issue.")
