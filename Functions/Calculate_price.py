def Calculate(cart):
    total_price = 0
    for item in cart:
        total_price += item['price'] * item['quantity']

    return total_price

##Example cart data

cart =[
    {'name': "Apple", 'price':0.5, 'quantity': 4},
    {'name': "Orange", 'price':1.5, 'quantity': 7},
    {'name': "Banana", 'price':2.5, 'quantity': 3},
    {'name': "Grapes", 'price':4.5, 'quantity': 4}   
]

##Calling the function
total_cost = Calculate(cart)
print(total_cost)