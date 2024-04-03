"""
File: list_merge.py
Author: Ravindu Gunasekara
Date: 09/25/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    User creates two lists based
    on their inputs, then those
    lists and a merged list are
    printed out.
"""
size = int(input("How many elements do you  want in each list? "))
list_one = list()
list_two = list()
merged_list = list()

for i in range(size):
    element = input("What do you want to put in the first list? ")
    list_one.append(element)

for i in range(size):
    element = input("What do you want to put in the second list? ")
    list_two.append(element)

for i in range(size):
    merged_list.append(list_one[i])
    merged_list.append(list_two[i])

print(f"The first list is: {list_one}")
print(f"The second list is: {list_two}")
print(f"The merged list is: {merged_list}")
