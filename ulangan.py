import random
from traceback import print_tb
from IPython.display import HTML, display

def display_data_as_table(data, headers=[]):
    if len(headers) == 0:
        for i in range(len(data[0])):
            print("\ni =",i,"len(data[0]) =", len(data[0]))
            headers.append("Column " + str(i))
            print("\nheaders = ",headers)
    display(HTML(
        '<table><thead><tr><th>{}</th></tr></thead><tbody><tr>{}</tr></tbody></table>'.format(
            '</th><th>'.join(header for header in headers),
            '</tr><tr>'.join(
            '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in data)
        )
    ))
    
def calculate_points(transaction):
    point = transaction[1] /100000
    points = int(point)
    return points

def generate_transaction_data(n=100):
    transactions = []
    print("\ntransactions =",transactions)
    for i in range(1, 5):
        print("\ni =", i)
        amount = random.randint(75, 400) * 1000
        print("\namount =",amount)
        price = random.randint(75, 150) * 1000
        print("\nprice =",price)
        items = amount / price
        print("\nitems =",items)
        items = int(items)
        print("integer items =",items)
        if items == 0:
            items += 1
            print("\nif items0 =",items)
        transaction = (i, amount, items)
        transaction = (i, amount, items, calculate_points(transaction))
        print("\ntransaction =",transaction)
        transactions.append(transaction)
        print("\ntipe data transactions =",type(transaction))
        print("\ntransactions =",transactions)
    return transactions
transactions = generate_transaction_data()
print("\ntipe data transactions =",type(transactions))
print("\nThe first 5 transaction data:")
display_data_as_table(transactions[:5], headers=["Transaction ID", "Amount", "Items", "Point"])
#print("\ndisplay_data_as_table() =", display_data_as_table(transactions[:5], headers=["Transaction ID", "Amount", "Items", "Point"]))
