# inventory_system.py
# Standard imports
from typing import NoReturn
from copy import deepcopy


def create_inventory() -> dict:
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    # Main categories in the inventory
    categories = ['Electronics', 'Groceries', 'Clothing']
    
    inventory = {
        category: {
            'Laptop': dict(name='Laptop', price=1100, quantity=5),
            'Tablet': dict(name='Tablet', price=500, quantity=15)
        } if category == 'Electronics' else {
            'Jeans': dict(name='Jeans', price=40, quantity=50)
        } if category == 'Clothing' else {
            'Milk': dict(name="Milk", price=50, quantity=1)
        }
        for category in categories
    }
    return inventory


def update_inventory(inventory: dict, category: str, item_name: str, update_info: dict) -> NoReturn:
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    @param inventory: The inventory dictionary to update
    @param category: The category of the item to update
    @param item_name: The name of the item to update
    @param update_info: The information to update (e.g., {'quantity': 10})
    """
    # Check if the category exists in the inventory
    if category in inventory:
        # Check if the item exists in the category
        if item_name in inventory[category]:
            # Update the item information
            inventory[category][item_name].update(update_info)
        else:
            inventory[category][item_name] = update_info
    else:
        # Add the new category to the inventory with the new item
        inventory[category] = {item_name: update_info}


def merge_inventories(inv1: dict, inv2: dict) -> dict:
    """
    Merge two inventory systems without losing any data.
    @param inv1: The first inventory to merge
    @param inv2: The second inventory to merge
    """
    # Create a deep copy of the first inventory
    merged_inventory = deepcopy(inv1)
    
    # Iterate through the second inventory and update the merged inventory
    for category, items in inv2.items():
        if category not in merged_inventory:
            merged_inventory[category] = items
        else:
            for item_name, item_info in items.items():
                if item_name in merged_inventory[category]:
                    # Merge the quantity of existing items
                    merged_inventory[category][item_name]['quantity'] += item_info['quantity']
                    # Update other information if needed
                    for key, value in item_info.items():
                        if key != 'quantity':
                            merged_inventory[category][item_name][key] = value
                else:
                    # Add new items
                    merged_inventory[category][item_name] = item_info
    return merged_inventory


def get_items_in_category(inventory: dict, category: str) -> dict:
    """
    Retrieve all items in a specified category.
    @param inventory: The inventory dictionary to retrieve items from
    @param category: The category to retrieve items from
    """
    return inventory.get(category, {})


def find_most_expensive_item(inventory: dict) -> dict:
    """
    Find and return the most expensive item in the inventory.
    @param inventory: The inventory dictionary to find the most expensive item in
    """
    # Initialize variables to track the most expensive item and its price
    most_expensive_item = {}
    max_price = float('-inf')
    
    # Iterate through the inventory to find the most expensive item
    for category, items in inventory.items():
        for item_name, item_info in items.items():
            if item_info.get('price', 0) > max_price:
                max_price = item_info.get('price', 0)
                most_expensive_item = item_info
    return most_expensive_item


def check_item_in_stock(inventory: dict, item_name: str) -> dict:
    """
    Check if an item is in stock and return its details if available.
    @param inventory: The inventory dictionary to check for the item
    @param item_name: The name of the item to check for in stock
    """
    # Iterate through the inventory to find the item
    for category, items in inventory.items():
        if item_name in items:
            return items[item_name]
    return None


def view_categories(inventory: dict) -> list:
    """
    View available categories (keys of the outer dictionary).
    @param inventory: The inventory dictionary to view categories from
    """
    return list(inventory.keys())


def view_all_items(inventory: dict) -> list:
    """
    View all items (values of the inventory).
    @param inventory: The inventory dictionary to view all items
    @return: A list of all items in the inventory
    """
    all_items = []
    for category in inventory:
        all_items.extend(inventory[category].values())
    return all_items


def view_category_item_pairs(inventory: dict) -> list:
    """
    View category-item pairs (items view of the inventory).
    @param inventory: The inventory dictionary to view category-item pairs
    @return: A list of tuples containing category-item pairs
    """
    category_item_pairs = []
    for category, items in inventory.items():
        for item in items:
            category_item_pairs.append((category, item))
    return category_item_pairs


def copy_inventory(inventory: dict, deep: bool = True) -> dict:
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    @param inventory: The inventory dictionary to copy
    @param deep: Boolean flag to determine if a deep copy should be made (default is True)
    @return: A copy of the inventory
    """
    if deep:
        return deepcopy(inventory)
    return inventory.copy()
