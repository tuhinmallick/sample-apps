import invoiceservice.app.api.db as db

def get_all_invoices():
    return db.fetch_all_invoices()