#!/usr/bin/env python3

loginfail = 0
loginsuccess = 0

keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')

keystone_file_lines=keystone_file.readlines()

for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1

        ### Return the IP address of the user
        ### The IP address is at the end of this line, just after the word from
        tline = keystone_file_lines[i]
        temp, ipaddress = tline.split("from")
        print('Failed attempt from ip', ipaddress)

        
 
    elif "-] Authorization failed" in keystone_file_lines[i]:
        loginsuccess +=1
 


print('The number of failed log in attempts is ' + str(loginfail))
print('The number of successful log in attempts is ' + str(loginsuccess))