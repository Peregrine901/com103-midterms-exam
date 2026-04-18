
# Ask for name
name = ""
while name == "":
    name = input("Please enter your name: ")
    if name == "":
        print("Error, name cannot be empty.")

# Ask for budget
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
