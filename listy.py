"""
Playground code for Python lists

A list is a collection of Python data and data types.

Lists start with [].

Strings are arrays of bytes representing Unicode characters.

Assignment, build these lists
  1. make a family information list
  2. make a pair share and project information list
  3. make a computer equipment list
  4. add these lists to the menu

Explore online tutorials
https://www.geeksforgeeks.org/python-list/?ref=lbp
"""

print("Hello Series: listy.py")  # identification message

# Build a list of numbers
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
# Build a new list of number divisible by 5
list = []
for i in range(len(numbers)):
    if (numbers[i] % 5) == 0:
        list.append(numbers[i])
print(list)
# Build a list of numbers divisible by 5 in one step
print([*range(0, 100 + 1, 5)])

# List of numbers, referencing items in list and formatting for output
list1 = [1.2345, 2.34, 3.45678, 4.5]
list2 = [2.2345, 3.34, 4.45678, 5.555]
list3 = [3.2345, 4.34, 5.45678, 6.5666]
# Table style formatting using parameters
list1_out = "{:10.2f} {:10.2f} {:10.2f} {:10.2f}".format(list1[0], list1[1], list1[2], list1[3])
# Table formatting using f"" inline variables
list2_out = f"{list2[0]:10.2f} {list2[1]:10.2f} {list2[2]:10.2f} {list2[3]:10.2f}"
# Table formatting using logic
list3_out = ''
for l in list3:
    list3_out = list3_out + f"{l:10.2f}" + " "
# PRINT all three formats, they all produce same result
print(list1_out)
print(list2_out)
print(list3_out)
print()

# LIST copy by value and by reference
l0 = [1, 5, 4, 2, 6, 3]
l1 = []
for i in range(len(l0)):  # loop for amount of items in l0
    l1.append(l0[i])  # append to l1
l1.sort()  # sort new list
print(f"old l0: {l0}")  # print original list
print(f"new l1: {l1}")  # print sorted list
l2 = l1
l2.sort(reverse=True)  # """reference, be careful"""
print(f"reprint l1: {l1}")  # reprint l1
print(f"new l2: {l2}")  # print reverse sorted list
print()

# LIST with dictionary records
# Dictionary Tags defined as scalars
FirstName = "First"
LastName = "Last"
MaidenName = "Maiden"
DOB = "DOB"
Residence = "Residence"
Email = "email"

# Dictionary Records placed in a list
InfoDb = []
InfoDb.append({FirstName: "John", LastName: "Mortensen", DOB: "October 21", Residence: "San Diego",
               Email: "jmortensen@powayusd.com"})
InfoDb.append(
    {FirstName: "Lora", LastName: "Mortensen", MaidenName: "Morgan", DOB: "September 23", Residence: "San Diego"})
InfoDb.append({FirstName: "Trent", LastName: "Mortensen", DOB: "January 2", Residence: "Wenatchee"})
InfoDb.append({FirstName: "Corey", LastName: "Mortensen", DOB: "March 24", Residence: "Seattle"})
InfoDb.append({FirstName: "Tiernan", LastName: "Mortensen", DOB: "August 2", Residence: "San Diego"})
InfoDb.append({FirstName: "Claire", LastName: "Ring", MaidenName: "Mortensen", DOB: "July 7", Residence: "Oak Harbor"})
InfoDb.append({FirstName: "Shay", LastName: "Mortensen", DOB: "May 2", Residence: "San Diego"})
print(InfoDb)
# Walk the list and print each dictionary record
for Info in InfoDb:
    print(
        "\n",
        f"{FirstName}: {Info[FirstName]}",
        "\n",
        f"{LastName}: {Info[LastName]}",
        f"({Info[MaidenName]})" if MaidenName in Info.keys() else "",
        "\n",
        f"{Residence}: {Info[Residence]}",
        "\n",
        f"{DOB}: {Info[DOB]}",
        "\n", f"{Email}: {Info[Email]}\n" if Email in Info.keys() else "",

    )

# Make a computer inventory, as we do this learn some attributes on your computer
ComputerDb = []
ComputerDb.append({'name': 'raspberrypi', 'ram': '4GB', 'ssd': '256GB'})
ComputerDb.append({'name': 'macbook pro', 'ram': '16GB', 'ssd': '512GB'})
print(ComputerDb)
