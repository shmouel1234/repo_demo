import random
import os

def cls(): return os.system('cls')

cls()

print("welcome to our first github project")
name = input("what is your name? ")
print(f"welcome to you {name}")
print(f"{name.title()} your name has {len(name)} letters")
for index , letter in enumerate(name):
    print(f"{index+1}: {letter}")
    if letter== "b":
        print("🤑🤑")
    else:
        print("😛😛")
count=0 
while True:
    number = int(input("type a number: "))
    if number%5==0:
        print(f"{number} is multiple of 5")
        count += 1
    else:
        break
print(f"you typed {count} number multiple of 5")
print("456"
        
