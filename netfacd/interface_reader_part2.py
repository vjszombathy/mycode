#!/usr/bin/env python3

import netifaces

def return_ip_address(adapter):
    # This prints out the MAC address given, using the key 'addr'
    my_ip =netifaces.ifaddresses(adapter)[netifaces.AF_INET][0]['addr']
    print("IP address for the adapter " + adapter + ": ", my_ip)
    return my_ip

def return_mac_address(adapter):
    # This prints out the MAC address given, using the key 'addr'
    my_mac=netifaces.ifaddresses(adapter)[netifaces.AF_LINK][0]['addr']
    print("MAC address for the adapter " + adapter + ": ", my_mac)
    return my_mac


print(netifaces.interfaces())

# Loop through each network interfaces
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    
    # This prints out a list that contains a dictionary
    # Keys include: 'addr', 'broadcast', or 'peer' 
    #print(netifaces.ifaddresses(i)[netifaces.AF_LINK]) 

 

    # This also prints out the IP address, using the key 'addr'
    #print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    try: 
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message



print()

# Call the function for IP address for the ens3 adapter
new_ip =return_ip_address("ens3")

# Call the function for MAC address for the ens3 adapter
new_mac = return_mac_address("ens3")

# Call the function for IP address for the lo adapter
new_ip =return_ip_address("lo")

# Call the function for MAC address for the lo adapter
new_mac = return_mac_address("lo")
