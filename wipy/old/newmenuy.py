# part 1 function calls
# String playground code
def stringy():
  exec(open("stringy.py").read())

# Number playground code
def numby():
  exec(open("numby.py").read())

def classy():
  import classy
  cl = classy.Classy()
  cl.print_monkeys()

commands = {
    1: stringy,
    2: numby,
    3: classy
  }

#function to turn number into a day
def functions(i):
  return commands.get(i,"Invalid function: "+str(i))

#functon to that tests day of week
def test_functions(): 
  print(functions(1))
  print(functions(2))
  print(functions(3))
  print(functions(4))
  print(functions("a"))

# Main menu example
def menu():
  print()
  print("=" * 25)  # print character "=" 25 times
  print("Please Select An Option")
  print("=" * 25)

  print("0: Exit")
  print("1: Strings")
  print("2: Numbers")
  print("3. Lists")

  # Input and validation
  choice = int(input("Type your choice> "))
  if choice == 0:
    return

  try:  # protects/traps errors from user
    exe_func = commands.get(choice, "Invalid choice: " + str(choice))
    exe_func()
  except:
    print("Function not defined: " + str(commands.get(choice)))
  menu()