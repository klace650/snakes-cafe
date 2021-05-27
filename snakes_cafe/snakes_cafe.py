
welcome = ("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")

order_prompt = ("""
***********************************
** What would you like to order? **
***********************************
""")

submenu = ['Appetizers','Entrees','Desserts','Drinks']

menu = {

  "Wings",
  "Cookies",
  "Spring Rolls",
  "Salmon",
  "Steak",
  "Meat Tornado",
  "A Literal Garden",
  "Ice Cream",
  "Cake",
  "Pie",
  "Coffee",
  "Tea",
  "Unicorn Tears",

}

def print_menu(lst):

  for menu_item in menu:
    print(menu_item)

print_menu(menu)
print(order_prompt)

selected_menu_items = []
input_list = []

def handle_input():

  while True:
    x = input("> ")
    if x == "Exit":
      print(input_list)
      break
    input_list.append(x)
    print(f'** 1 order of {x} has been added to your meal **')

handle_input()

  
