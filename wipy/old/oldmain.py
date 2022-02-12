"""
The main.py file is the Python starting point for the Hello Series project. This main.py code has been designed to setup a text based menu from Menus Class

A text base menu has purpose of getting input from user and performing the selected action.  This code has been designed to run other code from the multiple files within the project.

Some of the Python files in this Project have a linear organization.  The intention of these files is to introduce, or say hello, to the features of the language.  The string, number, and list files are ommisive of structure.  Thus, these files could be considered "ploaygound", meaning the have no formality.

Abstraction is taking linear code and turning it into procedural or object oriented code.  This is typically done when the file has an overall purpose.  The menu, loop, and class code in this project introduce design, structure, and purpose.  These are key practices described in the AP CS Principles course and exam description.

"""

""" Section to execute Python files outside of the main.py file, but within the Hello Series project  """
from menuy import Menus

# String playground code
def stringy():
  exec(open("stringy.py").read())


# Number playground code
def numby():
  exec(open("numby.py").read())


# List, Dictionary, Tuple playground code
def listy():
  exec(open("listy.py").read())


# ASCII/unicode art in imperative or procdural style
def loopy():
  import loopy
  loopy.main()


# ASCII/unicode art in object oriented style
def classy():
  import classy
  cl = classy.Classy()
  cl.print_monkeys()


# Classrom utility to pick order
def randomy():
  exec(open("randomy.py").read())


# Terminal pallet to show capabilities
def termy():
  import termy
  termy.clear()
  termy.colors()
  termy.load()
  termy.loading(10)


# Introduction to binary, hex
def biny():
  import biny
  biny.main()

# Introduction to function, no function
def prefuncy():
  exec(open("prefuncy.py").read())

# Introduction to function
def funcy():
  import funcy
  funcy.ship()

# Introduction to function
def newmenuy():
  import newmenuy
  newmenuy.test_functions()
  newmenuy.menu()


""" Section to define Menu and sub Menu data and the reference methods for associated prompts  """
# Submenu to parent menu
def submenu():
  options = [
  ["Random", randomy],
  ["Termy", termy],
  ["Biny", biny],
  ["Pre-Funcy", prefuncy],
  ["Funcy", funcy],
  ["Choicey", newmenuy]
  ]
  m = Menus(options)
  #m.shell()   #shell based menu
  m.menu()   #traditional menu


# Main menu 
def mainmenu():
  options = [
    ["Strings", stringy],
    ["Numbers", numby],
    ["Lists", listy],
    ["Loops", loopy],
    ["Classes", classy],
    ["Sub Menu", submenu],
  ]
  # Menu object created from Menu class
  m = Menus(options)
  m.menu()