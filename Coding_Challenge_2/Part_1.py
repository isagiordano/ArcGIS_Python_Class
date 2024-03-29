# For this coding challenge, for each item below produce a Python file that addresses each task (total of 5 files in your repo):

# 1. List values
# Using this list:

# [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
# You need to do two separate things here and report both in your Python file. 
# You should have two solutions in this file, one for item 1 and one for item 2. 
# Item 2 is tricky so if you get stuck try your best (no penalty), for a hint check out the solution by desiato here.

# Make a new list that has all the elements less than 5 from this list in it and print out this new list.
number_list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
del number_list[3:10]
print(number_list)

# or 

for i in number_list:
     if i < 5:
         print(str(i))

# Write this in one line of Python (you do not need to append to a list just print the output).
number_list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
filtered =  [ i for i in number_list if i < 5]
print(filtered)

# !!referenced from link provided in assignment
