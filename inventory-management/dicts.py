def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    dic = {

    }

    for item in items:
        dic[item] = items.count(item)
    return dic


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    for keys, values in inventory.items():

        if keys in items:
            inventory[keys] = values + items.count(keys)

    for item in items:
        if item not in inventory.keys():
            inventory[item] = items.count(item)

    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """

    for keys, values in inventory.items():

        if keys in items:
            inventory[keys] = values - items.count(keys)

    for key, value in inventory.items():

        if value < 0:
            inventory[key] = 0

    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory.keys():
        inventory.pop(item)

    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    lis = []

    for keys, values in inventory.items():
        if values != 0:
            inv_list = (keys, values)
            lis.append(inv_list)

    return lis


print(decrement_items({"wood": 2, "iron": 3, "diamond": 1},
                      ["wood", "wood", "wood", "iron", "diamond", "diamond"]))
