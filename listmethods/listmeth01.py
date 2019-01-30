#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
protob = ['ssh', 'http', 'https']

print(proto)
proto.append('dns') # this line will add 'dns' to the end of our list
protoa.append('dns') # this line will add 'dns' to the end of our list
print(proto)

proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print (proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print (protoa)

# Return the index value where 'https' is found in list, protob
# my_index should be equal to 2
my_index = protob.index('https')
print("my_index: " , my_index, " . . . Did it return 2?")

# Add 'ssh' to the list protob. . . three additional times
protob.append('ssh')
protob.append('ssh')
protob.append('ssh')

# Return the count of how many times 'ssh' is found in list, protob
# my_count should be equal to 4
print("protob: ", protob)
my_count = protob.count('ssh')
print("my_count: " , my_count, " . . . Did it return 4?")


