#!/usr/bin/env python3



# function to reboot all the devices contained in devicelist
def devicereboot(devicelist):
   for i, xx in enumerate(devicelist):
        print("Connecting to. . .", devicelist[i], " REBOOTING NOW!")


def easydevicereboot(mydevicelist):
   for i in mydevicelist:
       print("Connecting to . . .", i, " REBOOTING NOW!")





# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd.keys():
        print()
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to send command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

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