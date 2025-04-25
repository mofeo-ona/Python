from random import *

x=True
print("COMPLIMENT GENERATOR")
print("=="*20)

adjectives=["great","awesome","amazing"]
hobbies=["painting","cooking","drawing"]
print('''
    c - get compliment
    q - quit
    a - add hobby
    r - remove hobby
      
      ''')
def printing():
      print("you are",choice(adjectives),"at",choice(hobbies),",",name)
def deleting():
    print("what would you like to remove?")
    rm=input()
    hobbies.remove(rm)
    print("Here are the list of hobbies")
    print(hobbies)
def adding():
    print("what would you like to add?")
    do=input()
    hobbies.append(do)
    print("Here are the list of hobbies")
    print(hobbies)

print("what is your name")
name=input()

print("Here are the list of hobbies")
print(hobbies)

while x==True:
    

    menuChoice = input('\n>:')

    if menuChoice=="c":
       printing()
    elif menuChoice=="q":
        x=False
    elif menuChoice=="a":
       adding()
    elif menuChoice =="r":
        deleting()
    else:
        print("choose an option")


    