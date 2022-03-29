class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity

        self.item = {}
        self.total_quantity = 0

    def add_item(self, name, price, quantity):
        if name in self.item:
            return False
        if self.total_quantity + quantity > self.max_capacity:
            return False

        self.item[name] = [name, price, quantity]
        self.total_quantity += quantity
        return True

    def delete_item(self, name):
        if name not in self.item:
            return False
        self.total_quantity -= self.item[name][2]
        del self.item[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        list_of_names = []
        for key, value in self.item.items():
            if min_price <= value[1] <= max_price:
                list_of_names.append(value[0])
        return list_of_names

    def get_most_stocked_item(self):
        most_stocked = None
        current_list = ["", 0]
        for key, value in self.item.items():
            if value[2] > current_list[1]:
                current_list = [value[0], value[2]]
                most_stocked = value[0]
        return most_stocked







