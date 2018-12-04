#!/usr/bin/env python3

# This is a list of Internet protocols
proto = ['ssh', 'http', 'https']

# This prints out the entire list
print(proto)

# Print out the second item in the list
# The index starts at 0
print(proto[1])

# Add another item to the list
# The extend option is different than the append option
proto.extend('dns') # this line will add 'd', 'n', and 's' to the end of our list



# Print out the changed list
print(proto)