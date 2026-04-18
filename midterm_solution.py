
# the code ask for the name of the user
name = ""
while name == "":
    name = input("Please enter your name: ")
    if name == "":
        print("Error, name cannot be empty.")

# ask budget
budget = ""
while True:
    budget = input("Enter your weekly budget: ")
    if budget == "":
        print("Error, budget cannot be empty.")
    else:
        valid = True
        for ch in budget:
            if ch not in "0123456789.":
                valid = False
        if valid and budget != ".":
            budget = float(budget)
            break
        else:
            print("Error, invalid budget. Please enter a number.")

# added the categories and looping for the choices
categories = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

print("\nExpense Categories:")
i = 0
while i < len(categories):
    print(str(i+1) + ". " + categories[i])
    i = i + 1

entries = []
total = 0
count = 0

# ask the user their choices
while count < 4:
    option = input("\nEnter category number (1-5) or 0 to skip: ")
    if option == "":
        print("Error, invalid option.")
    else:
        valid = True
        for ch in option:
            if ch not in "0123456789":
                valid = False
        if valid:
            option = int(option)
            if option == 0:
                count = count + 1
            elif option >= 1 and option <= 5:
                desc = ""
                while desc == "":
                    desc = input("Enter item description: ")
                    if desc == "":
                        print("Error, description cannot be empty.")
                amount = input("Enter amount spent: ")
                valid_amt = True
                for ch in amount:
                    if ch not in "0123456789.":
                        valid_amt = False
                if valid_amt and amount != ".":
                    amount = float(amount)
                    total = total + amount
                    msg = ""
                    if amount >= budget * 0.25:
                        msg = " ! High Expense Alert!"
                    entries.append(categories[option-1] + " - " + desc + ": " + str(amount) + msg)
                    count = count + 1
                else:
                    print("Error, invalid amount.")
            else:
                print("Error, invalid option. Please enter 0-5.")
        else:
            print("Error, invalid option.")

