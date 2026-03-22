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
        #self.location

    def change_description(self, new_description):
        self.description = new_description

    def increase_total_amount(self, amount):
        self.total_amount += amount

    def decrease_total_amount(self, amount):
        self.total_amount -= amount

    def change_reorder_amount(self, new_reorder_amount):
        self.reorder_amount = new_reorder_amount

    def change_price_per_unit(self, new_price_per_unit):
        self.price_per_unit = new_price_per_unit

    def change_reorder_lead_time(self, new_reorder_lead_time):
        self.reorder_lead_time = new_reorder_lead_time

    def get_total_cost(self):
        return self.price_per_unit * self.total_amount

