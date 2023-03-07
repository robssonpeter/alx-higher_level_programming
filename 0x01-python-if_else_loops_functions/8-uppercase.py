#!/usr/bin/python3
def uppercase(str):
    length =  len(str)
    index = 0
    for a in str:
        print("*", end="")
        if (ord(a) >= 97 and ord(a) <= 122) or a == " " or (ord(a) >= 48 and ord(a) <= 57):
            diff = 0 if(ord(a) < 97) else 32
            print(chr(ord(a) - diff), end="")
        index+=1
        if (index == length):
            print("")
            
