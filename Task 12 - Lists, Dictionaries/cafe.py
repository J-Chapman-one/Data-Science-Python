#menu of four items sold in cafe stored in list
menu = ["pasta", "chips", "tea", "coffee"]

#stock level of each item sold in cafe stored in dictionary
stock = {"pasta" : 10,
        "chips" : 10,
        "tea" : 50,
        "coffee" : 50}

#price of each item sold in cafe stored in dictionary
price = {"pasta" : 5.05,
        "chips" : 3.50,
        "tea" : 1.50,
        "coffee" : 1.50}

total_stock = 0 #place  holder for overall stock value
for items in menu:
    total_stock += stock[items] * price[items] #calcualtion to determine overall stock value, iterates through each item in menu
    
print("The total stock value is £",total_stock)