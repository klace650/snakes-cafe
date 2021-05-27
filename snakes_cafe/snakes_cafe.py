
welcome = ("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")
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
order_prompt = ("""
***********************************
** What would you like to order? **
***********************************
""")

submenu = ['Appetizers','Entrees','Desserts','Drinks']



def print_menu(lst):

  for menu_item in menu:
    print(menu_item)
    if menu_item == 'Wings':
      print("yes")

print_menu(menu)



selected_menu_items = []
customers_order = []


def add_to_order(x):
  print(f'** 1 order of {x} has been added to your meal **')


def handle_input():

  while True:
    x = input("> ")
    add_to_order(x)
    if x == "quit":
      print(customers_order, 'ok bye')
      break
    customers_order.append(x)

handle_input()

  
