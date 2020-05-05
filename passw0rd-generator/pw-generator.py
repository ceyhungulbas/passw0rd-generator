'''
  _____                        ___          _         _____                           _             
 |  __ \                      / _ \        | |       / ____|                         | |            
 | |__) |_ _ ___ _____      _| | | |_ __ __| |      | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  ___/ _` / __/ __\ \ /\ / / | | | '__/ _` |      | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |  | (_| \__ \__ \\ V  V /| |_| | | | (_| |      | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|   \__,_|___/___/ \_/\_/  \___/|_|  \__,_|       \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                                                                                                                                                                                                                                             
                                                                                               

Ceyhun Gulbas - 5.4.2020
Thanks to my friends: Oguzhan and Bugra. They helped me when i stuck.
'''

import random
import string

print("Generate your strong passw0rd!\n")

lchar4pass = string.ascii_lowercase
uchar4pass = string.ascii_uppercase
numb4pass = string.digits
schar4pass =  string.punctuation

passlen = 0

while True:
    try:
        passlen = int(input("Enter the digit of password that you want: "))
    except:
        print("\nYou can't use letter, word, blank or symbol for digit. Obviously.")
    if passlen > 11 and passlen < 83:
        break
    else:
        print("\nEnter a number between 11 and 83. I recommend at least 16 digit for your own safety.\n")

pDivided = passlen//4

pass4LowerList = "".join(random.sample(lchar4pass,pDivided))
pass4UpperList = "".join(random.sample(uchar4pass,pDivided))
pass4LDigitList = "".join(random.sample(numb4pass,pDivided))
pass4SpecialList = "".join(random.sample(schar4pass,pDivided))



passw0rd = pass4LowerList + pass4UpperList + pass4LDigitList + pass4SpecialList

if passlen % 4 == 1:
    passw0rd += "".join(random.sample(numb4pass,1))
elif passlen % 4 == 2:
    passw0rd += "".join(random.sample(uchar4pass,2))
elif passlen % 4 == 3:
    passw0rd += "".join(random.sample(schar4pass,3))



passw0rd = "".join(random.sample(passw0rd,passlen))


print("\nHere's your PW:\t" + passw0rd)

input("\nIf you're done. Press Enter to exit.")
