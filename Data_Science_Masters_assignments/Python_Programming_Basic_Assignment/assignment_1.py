import numpy as np
'''
1. Write a Python program to print "Hello Python"?
2. Write a Python program to do arithmetical operations addition and division.?
3. Write a Python program to find the area of a triangle?
4. Write a Python program to swap two variables?
5. Write a Python program to generate a random number?
'''
print("Hello Python")
a=24
b=4
print(f'24 + 4 = {a+b}')
print(f'24 / 4 = {int(a/b)}')
base=2
height=3
print(f'area of the triangle of base {base} and height {height} is {base*height/2}')
num1=42
num2=21
print(f'value of num1 is {num1} and value of num2 is {num2}')
temp=num1
num1=num2
num2=temp
print('After swapping')
print(f'value of num1 is {num1} and value of num2 is {num2}')
print(f'Random number is {int(np.random.randint(1,10,1))}')