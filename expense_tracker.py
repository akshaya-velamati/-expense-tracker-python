import csv

def add_transaction():
    date = input("Date (YYYY-MM-DD): ")
    amount = float(input("Amount: "))
    type_ = input("Type (income/expense): ")
    desc = input("Description: ")
    with open("expenses.csv", 'a', newline='') as f:
        csv.writer(f).writerow([date, amount, type_, desc])

def view_transactions():
    try:
        with open("expenses.csv", 'r') as f:
            for row in csv.reader(f):
                print(row)
    except FileNotFoundError:
        print("No records yet.")

def view_balance():
    income = expense = 0
    try:
        with open("expenses.csv", 'r') as f:
            for row in csv.reader(f):
                amt = float(row[1])
                if row[2].lower() == "income": income += amt
                else: expense += amt
    except FileNotFoundError:
        pass
    print("Balance:", income - expense)

while True:
    print("\n1. Add  2. View All  3. Balance  4. Exit")
    ch = input("Choose: ")
    if ch == '1': add_transaction()
    elif ch == '2': view_transactions()
    elif ch == '3': view_balance()
    elif ch == '4': break
    else: print("Invalid")
