# This min project is an expense tracker that lets you input your expenses view the summary of your expenses, view by category.
import sys

expenses = []

def menu():
    print("\n--- Welcome to the Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. View by Category")
    print("4. Exit")
    selection = int(input("Enter your choice (1-4): "))
    if selection == 1:
        addExpense()
    
    elif selection == 2:
        viewSummary(expenses)

    elif selection == 3:
        viewCategory(expenses)
    
    elif selection == 4:
        quit_program()
    
    else:
        print(f"Please choose a valid selection")
        menu()
       
def addExpense():
    category = input("Please input the category of your expense: ").title()
    amount = float(input("Please input the amount you spent on the category: "))
    expense = {"Category": category, "Amount": amount}
    expenses.append(expense)
    print(f"Added ${amount:.2f} under category '{category}'.")

def viewSummary(expenses):
    if expenses:
         total = sum(exp["Amount"] for exp in expenses)
         avg = total / len(expenses)
         print(f"Total Spent: ${total:.2f}")
         print(f"Average Expense: ${avg:.2f}")
    else:
        print(f"There are no expenses to view.")

def viewCategory(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    print("Available categories")
    categories = {expense["Category"] for expense in expenses}
    
    for c in categories:
        print(f"- {c}")
        
    cat = input("Please select a category you would like to view: ")
        
    filtered = [e for e in expenses if e["Category"] == cat]
    
    if filtered:
        total = sum(e["Amount"] for e in filtered)
        print(f"Expenses in {cat}:")
        for e in filtered:
            print(f"- ${e['Amount']:.2f}")
        print(f"Total: ${total:.2f}")
    else:
        print(f"No expenses found for categroy '{cat}'.")
   

def quit_program():
    print("Exiting program goodbye.")
    sys.exit()


while True:
    menu()

            

        


