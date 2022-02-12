"""
The main.py file is the Python starting point for the Hello Series project.
"""
import menuy
import loopy
import classy
from wipy import termy
from wipy import biny
from wipy import funcy


#string playground code
def stringy():
  exec(open("stringy.py").read())


#number playground code
def numby():
  exec(open("numby.py").read())


# List, Dictionary, Tuple playground code
def listy():
  exec(open("listy.py").read())


# Classrom utility to pick order, playground code
def randomy():
  exec(open("wipy/randomy.py").read())


# Introduction to function, playground code
def prefuncy():
  exec(open("wipy/prefuncy.py").read())

#submenu dictionary
def submenu():
  func_sub = {
    1: ["Random", randomy],
    2: ["Termy", termy.main],
    3: ["Biny", biny.main],
    4: ["Pre-Funcy", prefuncy],
    5: ["Funcy", funcy.main],

  }
  menuy.menu(func_sub)

#function dictionary
func_dict = {
    1: ["Stringy",stringy],
    2: ["Numby", numby],
    3: ["Listy", listy],
    4: ["Loopy", loopy],
    5: ["Classy", classy],
    6: ["Submenu", submenu]
}

def main(): 
  #menu as function
  menuy.menu(func_dict)