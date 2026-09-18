# Expence Tracker

expenses = [] #list of all expenses in form of dicitionary
print("Welcome to Expense Tracker : ")

while True:
    print("====MENU===")
    print("1. Add Expenses")
    print("2. View all expenses")
    print("3. View Total khrcha")
    print("4. Exit")

    choice = input("Please Enter Your Choice")

# Add Expence
    if(choice ==1):
        date = input("Enter the Date:")
        category = input("Enter the Category : ex- (food,travel,makeup...)")
        description = input("Add some Details :")