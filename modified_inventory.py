class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class MostStocked:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def set_max_stock(self, item):
        self.name = item.name
        self.quantity = item.quantity


class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.item_dict = {}
        self.total_quantity = 0
        self.most_stocked = MostStocked(None, 0)

    def add_item(self, name, price, quantity):
        if name in self.item_dict:
            return False
        if self.total_quantity + quantity > self.max_capacity:
            return False
        item = Item(name, price, quantity)
        self.item_dict[name] = item
        self.total_quantity += quantity
        if quantity > self.most_stocked.quantity:
            self.most_stocked.set_max_stock(item)
        return True

    def delete_item(self, name):
        if name not in self.item_dict:
            return False
        self.total_quantity -= self.item_dict[name].quantity
        del self.item_dict[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        list_of_names = []
        for name, item in self.item_dict.items():
            if item.price >= min_price and item.price <= max_price:
                list_of_names.append(name)
        return list_of_names

    def get_most_stocked_item(self):
        return self.most_stocked.name

