#shared data structures

inventory = {
    "SKU001": 100,
    "SKU002": 50,
    "SKU003": 0
}

from collections import deque
order_queue = deque()


warehouse_zones = {
    "Zone A": {"capacity": 1000, "used": 800},
    "Zone B": {"capacity": 1500, "used": 1200},
    "Zone C": {"capacity": 1200, "used": 600}
}


#function 1
#purpose - retrieve current inventory based on SKU
#data structure used - hash table

def lookup_inventory(sku):
    if sku in inventory:
        return f"{sku}: {inventory[sku]} units in stock"
    else:
        return f"{sku}: not found in inventory"


#funciton 2
#purpose - update inventory by adding or subtracting by an SKU
#data structure used - hash table

def update_inventory(sku, quantity_change):
    if sku not in inventory:
        return f"Error: SKU {sku} does not exist in inventory."
    
    new_quantity = inventory[sku] + quantity_change

    if new_quantity < 0:
        return f"Error: Cannot reduce {sku} below zero. Current stock: {inventory[sku]}"
    
    if sku not in inventory:
        return f"Error: SKU {sku} does not exist in inventory."
    
    inventory[sku] = new_quantity
    return f"{sku} updated to {inventory[sku]} units."


#function 3
#purpose - process the next order in the queue and update inventory accordingly
#data structure used - queue and hash table

def add_order(order):
    order_queue.append(order)

def process_order():
    if not order_queue:
        return "No orders to process"
    
    order = order_queue.popleft()
    sku = order.get("sku")
    qty = order.get("quantity")

    if not isinstance(qty, int) or qty <= 0:
        return f"Invalid quantity for order: {order}"

    if sku not in inventory:
        return f"Order failed: {sku} not found in inventory"
    
    if inventory[sku] < qty:
        return f"Order failed: not enough stock for {sku}"
    
    inventory[sku] -= qty
    return f"Order for {sku} x{qty} processed successfully"


#function 4
#purpose - give a list of items that are below a certain quantity threshold
#data structure used - sorted list

def get_low_stock(threshold):
    if not isinstance(threshold, int) or threshold < 0:
        return "Error: Threshold must be a non-negative number."

    low_stock_items = []
    for sku, qty in inventory.items():
        if qty < threshold:
            low_stock_items.append((sku, qty))
    
    if not low_stock_items:
        return f"No items are below the threshold of {threshold} units."
    
    low_stock_items.sort(key=lambda x: x[1])
    result = "Low stock items:\n"
    for sku, qty in low_stock_items:
        result += f" - {sku}: {qty} units\n"
    return result.strip()

#function 5
#purpose - reccomend the best warehouse zone for storing a product based on available space
#data structure used - hash table

def suggest_storage_relocation(sku):
    if not isinstance(sku, str) or not sku.strip():
        return "Error: Invalid SKU input. SKU must be a non-empty string."
    if sku not in inventory:
        return f"Error: SKU {sku} does not exist in inventory."

    least_used_zone = None
    min_usage = float("inf")

    for zone, data in warehouse_zones.items():
        if data["used"] >= data["capacity"]:
            continue

        usage_percent = data["used"] / data["capacity"]
        if usage_percent < min_usage:
            min_usage = usage_percent
            least_used_zone = zone

    if least_used_zone:
        return f"Suggested zone for storing {sku}: {least_used_zone}"
    else:
        return "No available storage zones found."

#tests

if __name__ == "__main__":

    #test lookup_inventory
    print("LOOKUP INVENTORY")
    print(lookup_inventory("SKU001")) #normal
    print(lookup_inventory("SKU003")) #edge (zero in stock)
    print(lookup_inventory("SKU999")) #error (sku does not exist)


    #test update_inventory
    print("\nUPDATE INVENTORY")
    print(update_inventory("SKU002", 25)) #normal
    print(update_inventory("SKU001", -150)) #edge (stock can't be negative)
    print(update_inventory("SKU999", 10)) #error (sku does not exist)

    #test add_order and process order
    print("\nORDER PROCESSING")
    add_order({"sku": "SKU001", "quantity": 5}) #normal
    add_order({"sku": "SKU003", "quantity": 10}) #edge (zero stock)
    add_order({"sku": "SKU999", "quantity": 1}) #error (sku does not exist)
    print(process_order()) #normal
    print(process_order()) #not enough stock
    print(process_order()) #SKU does not exist
    print(process_order()) #queue is empty

    #test get_low_stock
    print("\nLOW STOCK CHECK")
    print(get_low_stock(30)) #normal
    print(get_low_stock(0)) #edge (nothing should be returned)
    print(get_low_stock(-5)) #error (negative input)

    #test suggest_storage_relocation
    print("\nSTORAGE SUGGESTION")
    print(suggest_storage_relocation("SKU001")) #normal
    print(suggest_storage_relocation("")) #error (blank sku)
    print(suggest_storage_relocation("SKU999")) #error (invalid sku)

    #edge case with all zones full
    warehouse_zones = {
        "Zone A": {"capacity": 1000, "used": 1000},
        "Zone B": {"capacity": 1500, "used": 1500},
        "Zone C": {"capacity": 1200, "used": 1200}
    }
    print("\nSTORAGE SUGGESTION EDGE CASE")
    print(warehouse_zones)
    print(suggest_storage_relocation("SKU002")) #edge case (no space left)
