
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

print(welcome)

menu = {
  "Wings":0,
  "Cookies":0,
  "Spring Rolls":0,

  "Salmon": 0,
  "Steak" : 0,
  "Meat Tornado" : 0,
  "A Literal Garden" : 0,

  "Ice Cream" : 0,
  "Cake" : 0,
  "Pie" : 0,

  "Coffee" : 0,
  "Tea" : 0,
  "Unicorn Tears" : 0,
}

def print_menu(lst):

  for menu_item in menu.keys():
    print(menu_item)

print_menu(menu)

user_input = input('> ')
selected_menu_items = []
input_list = []

def handle_input(x):
  while True:
    input_list.append(x)
    x = input("> ")
    
    if x == "Exit":
      print(input_list)
      break

handle_input(user_input)

  
