class ClientRecord:
    def __init__(self, client_id, full_name, phone_number, home_address):
        self.id = client_id
        self.name = full_name
        self.phone = phone_number
        self.address = home_address

class OrderRecord:
    def __init__(self, order_id, client_id, creation_date, current_status, price_total):
        self.id = order_id
        self.customer_id = client_id
        self.date = creation_date
        self.status = current_status
        self.total = price_total
