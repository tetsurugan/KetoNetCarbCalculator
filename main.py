#This is for the random functionality
import random

#This is a dictionary with Low carb Recipes that can be expanded upon by you if you want.
LowCarbRecipes = {
  'Keto Chicken Sandwhich':
  '2 slices Keto Culture Bread, 1/2 cup Cooked Chicken, Lettuce, Tomato, Mustard, Mayo, 1 sandwhich serving 2 Net Carbs',
  'Creamed Spinach':
  '10 ounces frozen spinach, 3 tablespoons parmesan cheese, 3 ounces cream cheese, 2 tablesppons sour cream, 1/4 teaspon garlic poder, 1/4 teaspon onion powder 3 servings of 4 net carbs', 'Pickles':'Pickles, 0 carbs', 'Boiled Eggs':'Boiled Eggs 0 carbs', 'Pork Rinds':'Pork Rinds 0 carbs'
}
item = list(LowCarbRecipes.items())


#This is the start of the program that you see It’s asking for your name and then from there it will break down into two pathways.
name = input("Hey, What is your name? ")

print(
  "Hello " + name,
  "Did you want the Net Carb Calculator'NCC' \nDid you want the Low carb Ideas?'LCI'"
)
mode = input("Type NCC or LCI ")
#NCC Net Carb Calculator has offers the standard net range of carbs and a simple calculator to hold on to your carbs for the day
if mode == "NCC":
  print("Daily Values Typically Range from 20-50 Net Carbs")
  NetCarbs = int(input("How many Net Carbs Do You Have Left For The Day? "))
  AfterMealCarbs = int(input("How many Net Carbs was your meal? "))
  CurrentNetCarbs = NetCarbs - AfterMealCarbs
  print ("Hey " +name, "You have " + str(CurrentNetCarbs), "Left for the day" )

#LCI Low carb ideas this brings in a prompt/loop that gives you a random recipe while you say yes and when you say no the program is broken with a goodbye message.
elif mode == "LCI":
  Prompt = None
  while Prompt not in("yes," "y", "no", "n"):
    Prompt =input("would you like a Low Carb Recipe? ")
    if Prompt in("y", "yes"):
      print(random.choice(list(LowCarbRecipes.items())))
    elif Prompt in['n', 'no']:
      print("Remember subtract those net carbs from your total carbs or just start the app over again and use the calculator")
      break
      
#else is if you typed something other than NCC or LCI it will make you start over.
else:
  print("Wrong Entry " + name, "Please Try Again")