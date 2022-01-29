'''
Write a Python Program to Check if a Number is Positive, Negative or Zero?
Write a Python Program to Check if a Number is Odd or Even?
Write a Python Program to Check Leap Year?
Write a Python Program to Check Prime Number?
Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

'''
def checkPrime(num):
    count=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            count+=1
    if count>1:
        return False
    else:
        return True


for i in range(1,10001):
    if checkPrime(i):
        print(i,end=' ')
print("Printed all the prime numbers from 1 to 10000") 

num=int(input('Enter number'))

if num>0:
    print("The number is positive")
elif num<0:
    print("The number is negative")
else:
    print("The number is 0")
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
if num%4==0 and (num%100!=0 or num%400==0):
    print('The number is a leap year') 
if checkPrime(num):
    print("The number is prime")
else:
    print("The number is not prime")

