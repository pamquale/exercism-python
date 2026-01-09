"""Functions to keep track and alter inventory."""


def create_inventory(items):
    output = dict()
    for item in items:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1    
    return output
        


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[f'{item}'] += 1
        else:
            inventory[f'{item}'] = 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory and inventory[f'{item}'] != 0:
            inventory[f'{item}'] -= 1
    return inventory


def remove_item(inventory, item):
    inventory.pop(item, 'Unknown')
    return inventory


def list_inventory(inventory):
    fullInventory = []
    for item in inventory:
        if inventory[item] != 0:
            fullInventory.append((item, inventory[item]))
    return fullInventory

