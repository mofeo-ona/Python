
from random import *
score = 0
running=True

print ('''
  ________                        _________.__                   
 /  _____/_____    _____   ____  /   _____/|  |__   ______  _  __
/   \  ___\__  \  /     \_/ __ \ \_____  \ |  |  \ /  _ \ \/ \/ /
\    \_\  \/ __ \|  Y Y  \  ___/ /        \|   Y  (  <_> )     / 
 \______  (____  /__|_|  /\___  >_______  /|___|  /\____/ \/\_/  
        \/     \/      \/     \/        \/      \/               
       
       [door 1]     [door2]     [door3]
''')

while running == True:
    print('There is a prize in one of these doors')
    print( 'Choose a door (1,2 or 3)')

    chosenDoor=input()
    chosenDoor=int(chosenDoor)

    winnningDoor= randint(1,3)

    if chosenDoor == winnningDoor:
        print('congratulations! You won!')
        score = score+1
        
    else:
        print('try again')

    print(f"The chosen Door is {chosenDoor}")
    print(f"The winning door is {winnningDoor}")

    print("Do you want to continue?")
    quit=input().lower

    if quit == "no":
        running=False

            
print(f"your final score is {score}")