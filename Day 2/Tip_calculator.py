print("Welcome to the Tip Calculator")
try:
    bill = float(input("What is the amount of the total bill? "))
    tip_percent = float(input("What percent of tip you want to add 10,12 or 15?"))
    persons = int(input("How many persons are going to split up the bill?"))
    each_pay = (bill * (1 + tip_percent/100)) / persons
    print(f"Each person should pay {round(each_pay,2)}")
except ValueError:
    print("Please enter numerical values only.")


