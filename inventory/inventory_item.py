class InventoryItem:
    def __init__(self, id, description, total_amount, reorder_amount, price_per_unit,
                 reorder_lead_time, total_cost):
        self.id = id
        self.description = description
        self.total_amount = total_amount
        self.reorder_amount = reorder_amount
        self.price_per_unit = price_per_unit
        self.reorder_lead_time = reorder_lead_time
        self.total_cost = total_cost
        self.location

    