#!/usr/bin/env python3

## Prompt the user for the input file
#file_name = input('Enter the name of the file to read')
file_name = 'vlanconfig.cfg'

## create file object in "r"ead mode
configfile = open(file_name, 'r')

## display file to the screen - .read()
configblog = configfile.read()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## line_cnt is the number of lines in the input file
## Since the configlist was built using the line boundaries
## line_cnt is equal to the length of the configlist
line_cnt = len(configlist)

## display list with no '\n'
print("configlist: = " ,configlist)

## Display the number of lines in the input file
print("line_cnt: = ", line_cnt)

## Always close your file
configfile.close()