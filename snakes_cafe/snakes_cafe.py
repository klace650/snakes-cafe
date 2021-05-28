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
  "WINGS": 0,
  "COOKIES": 0,
  "SPRING ROLLS": 0,
  "SALMON": 0,
  "MEAT TORNADO": 0,
  "A LITERAL GARDEN": 0,
  "ICE CREAM": 0,
  "CAKE": 0,
  "PIE": 0,
  "TEA": 0,
  "UNICORN TEARS": 0,
}

def handle_input(x):
  to_upper = x.upper()
  x = to_upper
  menu[x] += 1
  return(f"** {menu[x]} order(s) of {x} have been added to your meal **")

while True:

  user_input = input("> ")
  if user_input == 'quit':
    print('Thanks for your order - BYE', menu)
    break
  print(handle_input(user_input))

