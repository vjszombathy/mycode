#!/usr/bin/env python3

# Original List of protocols
proto = ['ssh', 'http', 'https']

# Another list of protocols
protoa = ['ssh', 'http', 'https']

# Print the original list of protocols
print("PRINTING the original list of protocols")
print(proto)
print()

# Appending a string to the end of the list
proto.append('dns') # this line will add 'dns' to the end of our list
protoa.append('dns') # this line will add 'dns' to the end of our list

# Print the changed list of protocols
print("PRINTING the updated list of protocols. . . it now has added 'dns'")
print(proto)
print()

# New list of common ports
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
print("PRINTING the list of common ports, identified as proto2")
print(proto2)
print()


#Adding the common ports list, to the original list
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print("PRINTING the original list, with proto2 list EXTENDED")
print(proto)
print()

#Adding the common ports list, to the protoa list
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print("PRINTING list protoa list, with proto2 list APPENDED")
print("NOTE that the APPENDED list made a SECOND list inside of the original list")
print(protoa)
print()


# Print out the changed list
print("PRINTING the original list, with proto2 list EXTENDED")
print("NOTE that the EXTENDED list keeps a single list")
print(proto)