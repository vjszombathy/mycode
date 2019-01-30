#!/usr/bin/env python3
x = int(input("Enter a number: "))

f= 1

# The range function (start, stop) does not include the stop value
# Hence you want to make the stop value, x+ 1 (instead of x)
for i in range(1, x+1):
    f = f * i  

print(x, '! = ', f)