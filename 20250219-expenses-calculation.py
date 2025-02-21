#To ask Nabiha 
Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
while True:
    month = input("For which month: ")
    if month == "stop": 
        break
    while month not in Months: 
        print("***Not Allowed***")
        month = input("For which month: ")   
        if month == "stop": 
            break
    if month == "stop": 
        break
         
    salary = input("What is your salary: ") 
    percentageSaving = input("What is your percentage for saving: ")
    percentageRent = input("What is your percentage for renting: ")
    percentageElectricity = input("What is your percentage for electricity: ")

    #The amount allocated to saving, rent, and electricity
    print("- Nabiha salary for the month of", month, "is", salary + "$. From this amount, Nabiha saved ", str(float(salary)*float(percentageSaving)) + "$ spend ", str(float(salary)*float(percentageRent)) + "$ on renting "
    "and", str(float(salary)*float(percentageElectricity)) + "$ on electricity")

    #Total amount Nabiha spends on saving, rent, and electricity combined
    sumexpenses = float(salary)*float(percentageSaving) +  float(salary)*float(percentageRent) + float(salary)*float(percentageElectricity)
    print("- The total expenses of Nabiha is " + str(sumexpenses) +"$")

    #Remainder of Nabiha's salary
    remainder = float(salary) - sumexpenses
    print("- The remainder of her salary is ", str(remainder) +"$")

    #Yearly rent and electricity cost 
    YearlyRent = (float(salary)*float(percentageRent))*12 
    print("- Nabila's yearly rent is " + str(YearlyRent) +"$")
    YearlyElectricity = (float(salary)*float(percentageElectricity))*12
    print("- Nabila's yearly relectricy cost is " + str(YearlyElectricity) + "$")

    #Nabiha"s total salary for the month raised to power of 2
    Power = float(salary)**2 
    print("- Nabiha's total salary for the month raised to the power 2 is " + str(Power) +"$")

    #Additional random amount of 50$

