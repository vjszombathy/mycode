#!/usr/bin/env python3



# function to reboot all the devices contained in devicelist
def devicereboot(devicelist):
   for i, xx in enumerate(devicelist):
        print("Connecting to. . .", devicelist[i], " REBOOTING NOW!")


def easydevicereboot(mydevicelist):
   for i in mydevicelist:
       print("Connecting to . . .", i, " REBOOTING NOW!")



# function to push commands
def commandpush(devicecmd): # devicecmd == dictionary 
    # my_ip_key is used in the loop, it could be renamed something else
    # my_ip_key is used to access each key-value in the dictionary
    for my_ip_key in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + my_ip_key )
        # we'll learn to write code that connects to devices here
        
        # Access the value associated with the key, my_ip_key
        # Note that this is a list of commands
        for mycmds in devicecmd[my_ip_key]:
            print('Attempting to sending command --> ' + mycmds )


### Start our script
work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

print("Welcome to the network device command pusher") # welcome message

### get data set
print("\nData set found\n") # replace with function call that reads in data from file

### run 
commandpush(work2do) # call function to push commands to devices

### Definition of devices to be rebooted
dlist = ["10.50.0.91", "10.60.0.92", "10.70.0.93", "10.80.0.94"]
print()
print("Calling devicereboot... with using the ENUMERATE keyword to navigate the list")
devicereboot(dlist)

print()

### Definition of devices to be rebooted
mydlist = ["2.50.0.91", "3.60.0.92", "4.70.0.93", "5.80.0.94"]
print()
print("Calling easydevicereboot... simpler FOR loop to navigate the list")
easydevicereboot(mydlist)