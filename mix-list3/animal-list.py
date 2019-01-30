#!/usr/bin/env python3
#animal_list = []
animal_list = ['bird', 'cat', 'dog', 'elephant', 'fish']
print(animal_list)

# The item 'goat' is added to the list
animal_list.append('goat')
print(animal_list)

# This list of IP addresses is embedded inside the list1
animal_list.append(['lion', 'monkey', 'panda'])
print(animal_list)

# This prints out the embedded list that was appended to list1
print(animal_list[6]) 

print()

# This prints out the first element in the embedded list
print("The next line should print out. . . lion")
print(animal_list[6][0])

print()

# This prints out the second element in the embedded list
print("The next line should print out. . . monkey")
print(animal_list[6][1])
