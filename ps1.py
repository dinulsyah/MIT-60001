#Problem Set 1 Part A (MIT 6.0001)
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter cost of your dream home: "))
portion_down_payment=0.25
r=0.04
down_cost = total_cost*portion_down_payment
current_savings=0
monthly_salary=annual_salary/12
monthly_saving=monthly_salary*portion_saved
months=0
while down_cost>current_savings:
    current_savings=current_savings+monthly_saving+current_savings*r/12
    months=months+1
print (months)


#Problem Set 1 Part B (MIT 6.0001)
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter cost of your dream home: "))
semi_annual_raise= float(input("Enter the semi-annual raise, as a decimal: "))
portion_down_payment=0.25
r=0.04
down_cost = total_cost*portion_down_payment
current_savings=0
monthly_salary=annual_salary/12
monthly_saving=monthly_salary*portion_saved
months=0
while down_cost>current_savings:
    current_savings=current_savings+monthly_saving+current_savings*r/12
    months=months+1
    if months%6 == 0:
        monthly_saving = monthly_saving+monthly_saving*semi_annual_raise
print (months)

#Problem Set 1 Part C (MIT 6.0001)
months = 36
semi_annual = 0.07
r = 0.04
house_cost = 1000000
down_payment = 0.25*house_cost
current_savings = 0
difference = abs(current_savings-down_payment)
starting_salary = float(input("Enter the starting salary : "))
salary=starting_salary/12
high = 10000
low = 0
guess = (high+low)/2
bisection_step=0
while difference >= 100:
    for i in range(1,months+1):
        if i%6==0:
            salary=salary+salary*semi_annual
        current_savings = current_savings + guess*salary + (current_savings*r)/12
    current_savings=current_savings*0.0001
    difference= abs(current_savings-down_payment)
    bisection_step=bisection_step+1
    if current_savings > down_payment:
        high = guess
    elif bisection_step > 13:
        print ("it is not possible to pay the down payment in three years")
        break
    else:
        low = guess
    guess=(high+low)/2
    current_saving = 0
    salary = starting_salary/12
if bisection_step > 13:
    print ("")
else:
    print ("Best savings rate:",guess*0.0001)
    print ("Steps in bisection search:",bisection_step)"""
