sales_ammount = float(input("How much did you sell oranges for: "))
actual_cost = float(input("What was the real price: "))
profit = sales_ammount - actual_cost
if (sales_ammount > actual_cost): 
    print("You earned a profit of ",profit)
else:
    print('You did not earn anything')
