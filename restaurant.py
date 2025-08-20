from typing import Optional # https://docs.python.org/3/library/typing.html
# PS: zistil som ze PEP 8 odporuca snake_case


class MenuItem:
    def __init__(self, _id: int, name: str, description: str, price_cents: int):
        self._id = _id
        self.name: str = name
        self.description: str = description
        self.price_cents: int = price_cents


class Name:
    def __init__(self, first_name: str, last_name: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.full_name: str = f"{first_name} {last_name}"


class Table:
    def __init__(self, _id: int, name: str, reserved_for: Optional['Customer'] = None):
        self._id: int = _id
        self.name: str = name
        self.reserved_for: Optional['Customer'] = reserved_for

    
    def reserve(self, customer: Optional['Customer'] = None) -> None:
        if self.reserved_for is not None:
            raise ValueError("This table is already reserved!")
        
        self.reserved_for: Optional['Customer'] = customer


    def cancel_reservation(self):
        self.reserved_for: Optional['Customer'] = None


class Customer:
    def __init__(self, _id: int, name: Name, reserved_tables: list[Table]):
        self._id = _id
        self.name = name
        self.reserved_tables = reserved_tables


class CustomerOrder:
    def __init__(self, _id: int, name: str, items: list[MenuItem], ordered_by: Customer):
        self._id: int = _id
        self.name: str = name
        self.items: list[MenuItem] = items
        self.ordered_by: Customer = ordered_by

        self.total = 0
        for item in self.items:
            self.total += item.price_cents


class Restaurant:
    def __init__(self, menu_items: list[MenuItem], tables: list[Table], customer_orders: list[CustomerOrder]):
        self.menu_items = menu_items
        self.tables = tables
        self.customer_orders = customer_orders

    def reserve_tables(self, tables: list[Table], reserved_for: Customer) -> None:
        for table in tables:
            table.reserve(reserved_for)

    def add_order(self, order: CustomerOrder) -> None:
        self.customer_orders.append(order)

    def add_item_to_menu(self, menu_item: MenuItem) -> None:
        self.menu_items.append(menu_item)

    def print_menu(self) -> None:
        for menu_item in self.menu_items:
            print(f"{menu_item.name} for {menu_item.price_cents/100:.2f}. Description: {menu_item.description}")

    def print_reservations(self) -> None:
        for table in self.tables:
            if table.reserved_for is not None:
                print(f"{table.name} is reserved for {table.reserved_for.name.full_name}.")

    def print_orders(self) -> None:
        for order in self.customer_orders:
            print(f"{order.name} was ordered by {order.ordered_by.name.full_name}.")

"""
TODO:
- prejst na slovniky, nie len listy!!!

Optional:

Class Restaurant includes methods for adding, updating, and removing menu items, and also handles table cancellation and waitlisting.
Maintain a log of customer orders, calculates the total revenue, and prints a detailed sales report.
Menu that allows seasonal updates and includes a method to display a sorted menu by item price.
Enable customer feedback by storing ratings for each order and then calculates the average rating for each menu item.
"""
