'''
Write a Python program to convert kilometers to miles?
Write a Python program to convert Celsius to Fahrenheit?
Write a Python program to display calendar?
Write a Python program to solve quadratic equation?
Write a Python program to swap two variables without temp variable?
'''

from datetime import date

distance=float(input("Enter value in kilometers"))
print(f'Value in miles={round(distance*0.621371,2)} miles')

temperature=float(input('Enter temperature in celcius'))
print(f'Temperature in farenheit = {round((temperature*9/5)+32,2)} F')

today = date.today()
print(f"today's calender: {today}")

print("Enter the coefficients for the terms of the quadratic equation")
a=int(input('for x^2'))
b=int(input('for x'))
c=int(input('for constant'))
root1=(-b+(b**2-4*a*c)**(1/2))/2*a
root2=(-b-(b**2-4*a*c)**(1/2))/2*a
print(f"The two roots of the quad ratic equation are {root1} and {root2}")
num1=4
num2=5
print(f'num1 = {num1} nd num2 = {num2}')
num1,num2=num2,num1
print('AFter swaping')
print(f'num1 = {num1} nd num2 = {num2}')