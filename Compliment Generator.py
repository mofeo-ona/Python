#mylist=["pear","apple","orange",65,7.9]
#phone=["apple","samsung","nokia","tecno","motorola","google","huawei","Blackberry"]
#print(mylist)
#print(mylist[4])
#print(phone[7])

from random import *

print("COMPLIMENT GENERATOR")
print("=="*20)
fruit=["apple","banana","cherry"]
empty=[]
#print(fruit[-1])

fruit[1]="Dates"
print(fruit)

fruit.append('orange')
print(fruit)

fruit.remove('orange')
print(fruit)

if 'pawpaw' in fruit:
    print('yes')
else:
    print('no')
