#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if int(str(number)[-1]) > 5:
    compare = "is greater than 5"
elif int(str(number)[-1]) == 0:
    compare = "is 0"
elif int(str(number)[-1]) < 6:
    compare = "is less than 6 and not 0"
print(f"Last digit of {number} is {str(number)[-1]} and {compare}")
