#def rectangle_area (a,b):
    #result=a*b
    #return result

#print("What is the length")
#a = input()
#a=float(a)

#print("What is the width")
#b = input()
#b=float(b)

#area = rectangle_area(a,b)
#print(area)

#Write a function called check_even_or_odd that takes a number and prints whether it is even or odd

def check_even_or_odd (a):
    if a % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")

check_even_or_odd(5)
check_even_or_odd(4)
check_even_or_odd(7)

#Write a function fizz_buzz_advanced(n) that loops from 1 to n and:
#Prints "Fizz" if the number is divisible by 3
#Prints "Buzz" if divisible by 5
#Prints "FizzBuzz" if divisible by both
#Otherwise, prints the number itself

def fizz_buzz (n):
    for i in range (1,n+1):
        if i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 ==0:
            print("FizzBuzz")
        else:
            print(i)

fizz_buzz(12)
fizz_buzz(10)
fizz_buzz(15)

#Write a function group_by_remainder(numbers, divisor) that groups numbers in a dictionary by their remainders when divided by divisor.
