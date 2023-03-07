#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    no = 0 - int((str(number)[-1]))
    if (no < 0):
        compare = "is less than 6 and not 0"
    else:
        compare = "is 0"
elif int(str(number)[-1]) > 5:
    no = str(number)[-1]
    compare = "is greater than 5"
elif int(str(number)[-1]) == 0:
    no = str(number)[-1]
    compare = "is 0"
elif int(str(number)[-1]) < 6:
    no = str(number)[-1]
    compare = "is less than 6 and not 0"
print(f"Last digit of {number} is {no} and {compare}")
