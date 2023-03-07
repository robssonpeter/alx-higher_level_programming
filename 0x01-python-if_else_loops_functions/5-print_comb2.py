#!/usr/bin/python3
for a in range(0, 100):
    if a < 10:
        number = '0'+str(a)
    else:
        number = a
    if a != 99:
        print(number, end=", ")
    else:
        print(number)
