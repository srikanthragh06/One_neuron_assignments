'''
Write a Python Program to Find LCM?
Write a Python Program to Find HCF?
Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
Write a Python Program To Find ASCII value of a character?
Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
'''
def only_positive_int(val):
    '''
    raises exception if argument is not of int type and less than zero
    '''
    if type(val)!=int:
        raise Exception('Only integers allowed as arguments')
    if val<0:
        raise Exception('Only positive integers allowed as arguments')
def get_lcm(*args):
    '''
    only positve integers allowed as arguments.
    returns lcm of any given number of arguments
    '''
    for i in args:
        only_positive_int(i)
    try:
        result=0
        high=1
        for i in args:
            high*=i
        maximum=max(args)
        for i in range(maximum,high+1,maximum):
            val=i
            is_lcm=True
            for j in args:
                if val%j!=0:
                    is_lcm=False
                    break
            if is_lcm:
                result=val
                break
    except Exception as e:
        print(e)
    else:
        return result
def get_hcf(*args):
    '''
    only positve integers allowed as arguments.
    returns hcf of any given number of arguments
    '''
    for i in args:
        only_positive_int(i)
    try:
        result=0
        minimum=min(args)
        for i in range(minimum+1,0,-1):
            val=i
            is_hcf=True
            for j in args:
                if j%val!=0:
                    is_hcf=False
                    break
            if is_hcf:
                result=val
                break
    except Exception as e:
        print(e)
    else:
        return result
def decimalToBinary(val):
    '''
    returns binary value taking decimal number as argument
    '''
    try:
        result=bin(val).replace("0b", "")
    except Exception as e:
        print(e)
    else:
        return result
def decimalToOct(val):
    '''
    returns octal value taking decimal number as argument
    '''
    try:
        result=oct(val).replace("0o", "")
    except Exception as e:
        print(e)
    else:
        return result
def decimaltoHexa(val):
    '''
    returns hexa-decimal value taking decimal number as argument
    '''
    try:
        result=hex(val).replace("0x", "")
    except Exception as e:
        print(e)
    else:
        return result
def return_ascii(string):
    '''
    returns ascii value of a string charecter
    '''
    try:
        result=ord(string)
    except Exception as e:
        print(e)
    else:
        return result
def calc(a,b,oper):
    try:
        result=None
        if oper=='+':
            result=a+b
        elif oper=='-':
            result=a-b
        elif oper=='*':
            result=a*b
        elif oper=='/':
            result=a/b
    except Exception as e:
        print(e)
    else:
        return result

try:
    num1=int(input('Enter first number to find lcm'))
    num2=int(input('Enter second number to find lcm'))
    print('The lcm of {} and {} is {}'.format(num1,num2,get_lcm(num1,num2)))
    num1=int(input('Enter first number to find hcf'))
    num2=int(input('Enter second number to find hcf'))
    print('The hcf of {} and {} is {}'.format(num1,num2,get_hcf(num1,num2)))
    num1=int(input('Enter decimal number to convert'))
    print('{} in binary is {}, in octal is {}, in hexadecimal is {}'.format(num1,decimalToBinary(num1),decimalToOct(num1),decimaltoHexa(num1)))
    string=(input('Enter string charecter to convert to ascii'))
    print('{} in ascii is {}'.format(string,return_ascii(string)))
    num1=int(input('Enter first number'))
    num2=int(input('Enter second number'))
    oper=input('Enter operator')
    print("{} {} {} = {}".format(num1,oper,num2,calc(num1,num2,oper)))
except Exception as e:
    print(e)


