mealPrice = float(input("Enter the total amount of the meal:"))  #Used to gather the meal total
Gratuity = mealPrice * .18 #tip amount
Tax = mealPrice * .07 #tax amount
totalPrice = mealPrice + Gratuity + Tax
print("Receipt for Meal")
print('Meal:', mealPrice) #Used commas to seperate text from variables
print('Gratuity:', Gratuity)
print('Tax:', Tax)
print('Total:', totalPrice)