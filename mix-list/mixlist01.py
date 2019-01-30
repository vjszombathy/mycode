#!/usr/bin/env python3

# This illustrates a mixed list
# List items do not need to have the same type
my_list = [ "192.168.0.5", 5060, "UP" ]

# The first item in the list is stored at index 0!
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )


new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
my_output_string = "When I " + new_list[5] + " into IP addresses " + new_list[3] + " or " + new_list[4]
my_output_string =  my_output_string + ", I am unable to ping ports " + str(new_list[0]) + ", " + new_list[1] + ", or " + str(new_list[2])
print(my_output_string)