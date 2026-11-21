# Step 1 - Create and run a Python file
print("**** Python Foundation Lab Started ****") # print function

# Step 2 - Create variables and data types 
product = "Laptop" # string variable
quantity = 3 # integer variable
unit_price = 799.99 # float variable
in_stock = True # boolean variable

print("**** Variable Values ****") # print function
print("Product:", product)
print("Quantity:", quantity)
print("Unit Price:", unit_price)
print("In Stock:", in_stock)

print("**** Data Types ****") # print function
print(type(product))
print(type(quantity))
print(type(unit_price))
print(type(in_stock))

# Step 3 - Perform a sales calculation
total_sales = quantity * unit_price # calculate total sales
print("**** Sales Calculation ****") # print function
print("Product:", product)
print("Quantity:", quantity)
print("Unit Price:", unit_price)
print("Total Sales:", total_sales)

# Step 4 - Apply Conditional Statements
if total_sales >= 1000:
    print("Total sales exceed $1000.")
else:
    print("Total sales are below $1000.")

# Step 5 - Process Multiple Sales using a loop
sales = [1200, 850, 2400, 1750, 3200] # list of sales amounts
print("**** Multiple Sales Processing ****") # print function
for sale in sales:
    if sale >= 2000:
        print(f"Sale amount ${sale} is a high sale.")
    else:
        print(f"Sale amount ${sale} is a regular sale.")