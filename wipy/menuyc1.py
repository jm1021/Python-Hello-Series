"""
menuyc.py - class style menu
"""
class Prompt:
  def __init__(self, prompt, action):
    self.Db = []
    self.prompt = prompt
    self.action = action

class Menus:
  #Initializes dictionaries
  def __init__(self, options):
    #Parameter options is a list with format:
    #[0] - Prompt
    #[1] - Command

    #Exit prompt
    self.exit = "Exit"
    self.banner = None
    self.singlepass = False
    self.lastchoice = None

    #Dictionaries for Menus class
    self.options = {}   #menu option
    self.commands = {}  #command line options

    #Exit for menu
    self.options[0] = Prompt(self.exit, None)
    #Exit for commands
    self.commands[self.exit.lower()] = None

    #Loop options to build dictionaries
    for op in options:
      index = len(self.options)
      self.options[index] = Prompt(op[0], op[1])
      self.commands[op[0].lower()] = op[1]

  #setter for single or multiple pass
  def set_recurse(self, recurse):
    self.singlepass = not recurse

  #setter for alternate banner
  def set_banner(self, banner):
    self.banner = banner

  #getter for last user choice
  def get_choice(self):
    return self.lastchoice

  #menu prompts
  def print_menus(self):
    print()
    if self.banner == None:
      #standard menu heading
      print("Class Menu")
      print("=" * 25)  # print character "=" 25 times
      print("Please Select An Option")
      print("=" * 25)
    else:
      #alternate heading
      print(self.banner)
    
    #menu prompts
    for key, value in self.options.items():
      #no exit option on single pass
      if key == 0 and self.singlepass:
        continue
      print(key, '->', value.prompt)

  #menu selection and execute
  def choice(self):
    # get choice from user
    choice = input("Select Option: ")
    # validate choice and run
    #execute selection
    try: #try converting to integer
      #convert to number
      choice = int(choice)
      if choice == 0: #exit choice, stop loop
        return True  #stop 
      try:  #try as function function
        self.lastchoice = choice
        prompt = self.options[choice]
        action = prompt.action
        action()
      except:
        try:  #try as playground style
          exec(open(action).read())
        except:
          print(f"Bad action: {action}")
        #end function try
      #end playground try
    except ValueError: #not a number error
      print(f"Not a number: {choice}")
    except: #traps all other errors
      print(f"Invalid choice: {choice}")
    #end validation try
    return False or self.singlepass

  #command prompt and execute
  def command(self): 
    print()
    print("Class Menu with Shell style")
    choice = input("Typa a command (h for help)> ")
    #help prints commands
    if choice == "h":
      for command in self.commands:
        #no exit help on single pass
        if command == self.exit.lower() and self.singlepass:
          continue
        print(command)
      self.command() #help stays
    #exit get out of function
    elif choice == self.exit.lower():
        return True
    #all others try executions
    else:
      try:  # protects/traps errors from user
        self.lastchoice = choice
        action = self.commands[choice]
        action()
      except:
        try:
          exec(open(action).read())
        except:
          print(f"Not a command: {choice}")
        #end open try
      #end command try
    return False or self.singlepass

  #traditional menu
  def menu(self):
    self.print_menus()      #menu options
    stop = self.choice()    #user action
    if stop:                #stop
      return
    self.menu()             #continue via recursion

  #shell based style
  def shell(self):
    stop = self.command()   #commnad prompt
    if stop:                #stop
      return                   
    self.shell()            #continue via recursion