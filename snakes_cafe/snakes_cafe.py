from os import X_OK, pardir


print("""

**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")

menu = {
  "Wings": 0,
  "Cookies": 0,
  "Spring Rolls": 0,
  "Salmon": 0,
  "Meat Tornado": 0,
  "A Literal Garden": 0,
  "Ice Cream": 0,
  "Cake": 0,
  "Pie": 0,
  "TEA": 0,
  "Unicorn Tears": 0,
}

def handle_input(x):
  to_upper = x.upper()
  x = to_upper
  menu[x] += 1
  return(f"** {menu[x]} order(s) of {x} have been added to your meal **")

while True:

  user_input = input("> ")
  if user_input == 'quit':
    print('ok byeeee')
    break
  print(handle_input(user_input))

  