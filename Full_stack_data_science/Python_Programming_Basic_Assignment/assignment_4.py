'''
1. Write a Python Program to Find the Factorial of a Number?
2. Write a Python Program to Display the multiplication Table?
3. Write a Python Program to Print the Fibonacci sequence?
4. Write a Python Program to Check Armstrong Number?
5. Write a Python Program to Find Armstrong Number in an Interval?
6. Write a Python Program to Find the Sum of Natural Numbers?
'''



def factorial(num):
    product=1
    for i in range(num,0,-1):
        product*=i
    return product

def display_mult_table(num):

    for i in range(1,11):
        print(f'{num}*{i}={num*i}')

def list_fib(nums):
    fib=[0,1]
    for i in range(2,nums):
        fib.append(fib[i-1]+fib[i-2])
    return fib

def isArmstrong(num):
    digits=[]
    orig_num=num
    while(num>0):
        digits.append(num%10)
        num=num//10
    result=0
    for i in digits:
        result+=i**3

    if result==orig_num:
        return True
    else:
        return False

def sum_of_n(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum

num1=int(input("Enter number to calculate factorial"))
print(f"factorial is {factorial(num1)}")
num2=int(input("Enter number to calculate multiplication table"))
display_mult_table(num2)
num3=int(input("Enter length of fibonacci sequence"))
print(f'The fibonacci sequence is {list_fib(num3)}')
num4=int(input("Enter number to check armstrong"))
if isArmstrong(num4):
    print("its an armstrong number")
else:
    print("its not an armstrong number")
low=int(input("Enter lower number of interval to find armstrong numbers in between"))
high=int(input("Enter higher number of interval to find armstrong numbers in between"))
for i in range(low,high+1):
    if isArmstrong(i):
        print(i,end=' ')
print(f"printed armstrong numbers in betweeen {low} and {high}")
num5=int(input("Enter number to find sum of natural numbers"))
print(f'The sum of naturals numbers till {num5} is {sum_of_n(num5)}')