#!/usr/bin/env python3
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']

print("Printing out the entire list")
print(list1)
print()

print("Printing out one item from the list, using INDEX 1. . . ")
print("Remember that index 1 is the 2nd item in the list")
print(list1[1])
print()

# Extend the list, by adding juniper
list1.extend(['juniper'])
print("Print out the list, with the juniper added to the list")
print(list1)
print()

# Append the list, by adding a list within the list
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print("Print out the extended list, with the LIST added to this original list")
print(list1)