# Expence Tracker

expensesList  = [] #list of all expenses in form of dicitionary
print("Welcome to Expense Tracker : ")

while True:
    print("====MENU===")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))

# 1. Add Expence
    if(choice ==1):
        date = input("Enter the Date :")
        category = input("Enter the Category : ex- (food,travel,makeup...)")
        description = input("Add some Details :")
        amount = float(input("Enter the amount :"))

        expense ={
          "Date":date,
          "Category":category,
          "Description":description,
          "Amount":amount
        }

        expensesList.append(expense)
        print("\n Expence is added Succesfully")

# 2. View Allll Expeneses
    elif(choice ==2):
        if(len(expensesList)==0):
            print("---Go and Spend Some Money---")
        else:
              print("====== This is Your All Expense ======")  
              count = 1
              for eachExpense in expensesList:
                  print(f"Expense number {count} -> {eachExpense["Date"],{eachExpense["Category"]},{eachExpense["Amount"]}}")
                  count = count+1;

#View Total Spending
    elif(choice ==3):
        total=0
        for eachExpense in expensesList:
            total = total + eachExpense["Amount"]

            print("\n Total Expence =" , total)

# 4. EXIT
    elif(choice == 4):
        print("===ThankYou===")
        break
    else:
        print("Invalid Choice : Enter Again ")

 