# Remvoe duplicates entry
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

# Convert the list to a set to remove duplicates
customer_ids = set(customer_ids)

# Convert the set back to a list if needed
customer_ids_list = list(customer_ids)

# Output the unique customer IDs
print("Customer ID List:", customer_ids_list)
