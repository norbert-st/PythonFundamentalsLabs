# Step 1 - Create a function
def calculate_sales(quantity, unit_price):
    return quantity * unit_price

result = calculate_sales(3, 799.99) # call the function with quantity and unit price
print("**** Sales Calculation using Function ****") # print function
print("Total Sales:", result)

# Step 2 - Reuse the function with different values
print("**** Reusing Function with Different Values ****") # print function
print("Total Sales for 5 units at $499.99 each:", calculate_sales(5, 499.99))
print("Total Sales for 10 units at $299.99 each:", calculate_sales(10, 299.99))
print("Total Sales for 2 units at $999.99 each:", calculate_sales(2, 999.99))

# Step 3 - Check and Convert Data Types
print("")
print("**** Data Type Check and Conversion ****") # print function
quantity = "5" # string variable
print("Original quantity:", quantity, type(quantity))
quantity = int(quantity) # convert string to integer
print("Converted quantity:", quantity, type(quantity))
print("Total Sales after conversion:", calculate_sales(quantity, 500)) #call function

# Step 4 - Store multiple vaules in a list
sales = [1200, 850, 2400, 1750, 3200] # list of sales amounts
print("")
print("**** Store multiple vaules in a list ****") # print function
print("Sales:", sales)
print("First sale:", sales[0]) #indexing
print("Number of sales:", len(sales))

# Step 5 - Create and process a Dictionary
order = {
    "OrderID": "ORD001", # key and value pair
    "Product": "Laptop",
    "Quantity": 2,
    "UnitPrice": 850
}
 
total = calculate_sales(order["Quantity"], order["UnitPrice"])
print("")
print("****** Create and Process a Dictionary ******")
print("Product:", order["Product"])
print("Total Sales:", total)