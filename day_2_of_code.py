#writing a greeting to the user
print("Welcome to tip calculator!")

#asking user for the bill amount
bill = float(input("What was the total bill? $"))

#asking user for tip amount
tip = int(input("What percent tip would you like to give? 10, 12, or 15? "))

#asking user for number of individuals splitting the total bill
persons = int(input("How many people to split the bill? "))

#calculating tip amount 
tip_amount = (tip / 100) * bill

#splitting the bill among the individuals
bill_per_person = bill / persons

# bill of each individual plus tip each individaul is to pay
amount = bill_per_person + tip_amount / persons

#total amount to be payed by each individual rounded up to 2 decimal places
individual_amount = round(amount, 2)

#finally printing out the result
print(f"Each person should pay: ${individual_amount}")