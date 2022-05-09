import random
from traceback import print_tb
from IPython.display import HTML, display

def amount ():
    amount = random.randint(75, 400) * 1000
    return amount

def price ():
    price = random.randint(75, 400) * 1000
    return price

def items ():
    for i in range(1,5):
        items = amount()/price()
        items = int(items)
        if items == 0:
            items += 1
    return items

def calculate_points(transaction):
    point = transaction[1] /100000
    points = int(point)#agar point menjadi integer
    return points

def generate_transaction_data(n=100):
    transactions = []
    for i in range(1, 5):#range(1,6) karena data yg diminta ada 5 baris
        transaction = (i, amount(), items(), price())
        transaction = (i, amount, items, calculate_points(transaction))#calculate_points(transaction) = points
        transactions.append(transaction)
    return transactions

