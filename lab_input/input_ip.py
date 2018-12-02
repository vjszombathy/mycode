#!/usr/bin/env python3
# Written By:  Victoria Hill
# Collect IP address information from a user, and display it back to them.

# Collect input from the user
user_input = input('Please enter an IPv4 IP address:')

# Print out the input collected from the user
print("You told me the IPv4 address is:" + user_input)

# Collect vendor name from the user
vendor_name = input('Please enter the vendor name associated with this device at' + user_input + ": ")

# Print out the vendor name
print("You told me the VENDOR name is: " + vendor_name)