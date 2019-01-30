#!/usr/bin/env python3
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)

# The item 'juniper' is added to the list
list1.extend(['juniper'])
print(list1)

# This list of IP addresses is embedded inside the list1
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)

# This prints out the embedded list that was appended to list1
print(list1[4]) 

print()

# This prints out the first element in the embedded list
print("The next line should print out. . . '10.1.0.1'")
print(list1[4][0])

