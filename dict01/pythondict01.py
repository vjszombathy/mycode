#!/usr/bin/env python3

## Create a dictionary called switchDict
## Key values include: hostname, ip, version, vendor
switchDict = {'hostname': 'sw1', 
              'ip': '10.0.1.1', 
              'version': '1.2', 
              'vendor': 'cisco'
              }

## Display parts of the dictionary
print("CHECKING valid keys . . .")
print( switchDict['hostname'] )   # This should print out 'sw1'
print(". . .Check that it printed out . . .sw1")
print()

print( switchDict['ip'] )         # This should print out '10.0.1.1'
print(". . . Check that it printed out. . . 10.0.1.1")
print()

## Request a 'fake' key
## This will cause the program to fail!
# print( switchDict['lynx'] )  

## Request a 'fake' key with .get() method
print( "FIRST test - .get()" )
print(". . . Querying for the KEY lynx. . .")
print( switchDict.get('lynx') )
print(". . . Check that it printed out None, as the key was not found")
print()

print( "SECOND test - .get()" )
print(". . . Querying for the KEY lynx. . .")
print( switchDict.get('lynx', "THE KEY IS IN ANOTHER CASTLE!") )
print(". . . Check that it printed out the value. . . THE KEY IS IN ANOTHER CASTLE!")

print()
print( "THIRD test - .get()" )
print(". . . Querying for the KEY version. . .")
print( switchDict.get('version') )
print(". . . Check that it printed out the value . . 1.2")

print()
print( "FOURTH test - .keys()" )
print( switchDict.keys() )

print()
print( "FIFTH test - .values()" )
print( switchDict.values() )
print()

print( "SIXTH test - .pop()" )
switchDict.pop('version') # removes this key (and value) pair
print( switchDict.keys() )   # notice the value of version is gone
print( switchDict.values() ) # notice the value 1.2
print()

print( "SEVENTH test - ADD a new value" )
switchDict['adminlogin'] = 'admin02'
print( switchDict.keys() )
print( switchDict.values() )
print()

print( "EIGHTH test - ADD a new value" )
switchDict['password'] = 'qwerty'
print( switchDict.keys() )
print( switchDict.values() )
