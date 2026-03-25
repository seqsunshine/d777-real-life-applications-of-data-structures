Student Name: Sequoia Hancock
Student ID:010184738
Python Version: 3.11.2

Function Overview:

1: lookup_inventory(sku)
    - Purpose: Retrieves the inventory quantitiy for a specific SKU
    - How to run: Call lookup_inventory("SKU001") to get the current stock
    - Error Handling: Returns an error if the SKU is not found or is invalid (e.g. blank or None)
    - Edge Cases: Handles SKU with 0 stock cleanly

2: update_inventory(sku, quantity change)
    - Purpose: Updates inventory levels by adding or removing stock for a given SKU
    - How to run: Call update_inventory("SKU002", 25) to restock, use a negative number to reduce
    - Error Handling: Prevents reducing stock below zero. Rejects updates for SKUs that do not exist
    - Edge Cases: Handles attempts to remove more than what's available with a notification

3: add_order(order) + process_order()
    - Purpose: Adds an order to a queue and processes it in first-in-first-out order
    - How to run: Use add_order({"sku": "SKU001", "quantity": 5}) to add. Then call process order() to fulfill it
    - Error Handling: process_order() checks if the SKU exists and if enough stock is available before fulfilling
    - Edge Cases: Handles empty order queues, orders with missing fields, and SKUs not in inventory

4: get_low_stock(threshold)
    - Purpose: Returns a list of SKUs with inventory levels below a given threshold
    - How to run: Call get_low_stock(30) to see low stock items
    - Error Handling: Rejects negative or non-integer thresholds
    - Edge Case: Returns a clean message if no items are below threshold

5: suggest_storage_relocation(sku)
    - Suggests an optimal warehouse zone for storing a given SKU, based on available space
    - How to run: Call suggest_storage_relocation("SKU001")
    - Error Handling: Validates that the SKU is a non-empty string and exists in inventory
    - Edge Case: If all warehouse zones are full, it returns "No available storage zones found."

