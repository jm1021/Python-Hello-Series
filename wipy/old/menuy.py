"""
The Menu code in this file is organized in an objected oriented style.
"""

class Menus:
  def __init__(self, opts):
    #number menu setup
    self.options = {}
    self.options[0] = ["Exit", None]
    for i in range(len(opts)):
      self.options[i+1] = opts[i]
    #command menu setup
    self.commands = {}
    self.commands["Exit".lower()] = None
    for opt in opts:
      self.commands[opt[0].lower()] = opt[1]
    

  def display(self):
    print()
    print("=" * 25)  # print character "=" 25 times
    print("Please Select An Option")
    print("=" * 25)
    # menu options
    items = len(self.options)
    for i in range(items):
      print(str(i) + "; " + self.options[i][0])

  def select(self):
    # get choice from user
    index = input("Select Option: ")

    # validate choice and run
    try:  # protects/traps errors from user
        # convert input into integer type
        index = int(index)
        # test if choice is in menu index
        if index in self.options:
            if index == 0:    # exit condition
                return False  # exit out of menu_control
            # runs the choice
            exe_func = self.options[index][1]
            # test if func exists
            if exe_func is not None:
              #print(str(type(exe_func)) + " " + str(exe_func))0
              exe_func()  # 
        else:
            # raises index error
            raise IndexError()
    except ValueError:  # not a number error occurs if int(index) fails
        print("Not a number, {0} is not  valid.".format(index))
    except IndexError:  # error raised above
        print("Out of range. {0} is not a valid option.".format(index))
    return True

  
  #traditional menu based execution
  def menu(self):
    self.display()        #display options
    run = self.select()   #user choice
    if not run:           #stop
      return
    self.menu()           # recursion


  #command prompt
  def command(self): 
    print()
    c = input("Typa a command (h for help)> ").lower()
    if c == "h":
      for command in self.commands:
        print(command)
    elif c == "Exit".lower():
        return False
    else:
      try:  # protects/traps errors from user
        exe_func = self.commands[c]
        exe_func()
      except:
        print("Not a command")
    return True
  

  #shell based execution
  def shell(self):
    if not self.command():  #commnad prompt
      return                #exut condition   
    self.shell()            #recursion
