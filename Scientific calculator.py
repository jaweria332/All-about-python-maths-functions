#      ////////////////////................NCR, NPR etc............////////////////////
#factorial
def factorial(n):

    f=1
    if n==1 or n==0:
        return 1
    elif n>0:
        for k in range(1,n+1):
            f=f*k
        return f

#exp
def exponential(x):
    s=0
    for i in range(0,100):
        s=s+(x**i)/factorial(i)
    return s


#npr
def npr ():
    nval= int(input("enter value of n :"))
    rval= int(input("enter value of r :"))
    return factorial(nval)/factorial(nval-rval)
#ncr
def ncr():
    nval= int(input("enter value of n :"))
    rval= int(input("enter value of r :"))
    return (factorial(nval)/factorial(nval-rval))/factorial(rval) #npr/fact(r)

print(ncr())


# /////////////.............NUMBER SYSTEM CONVERSION.........../////////////

def value(num):
    x=bin(num)
    print(" The number conversion is=", x)


def value1(num1):
    x1=oct(num1)
    print(" The number conversion is= ", x1)


def value2(num2):
    x2=hex(num2)
    print(" The number conversion is=", x2)


def value3(num3):
    x3=int(num3, 2)
    print("The number conversion is=", x3)


def value4(num4):
    x4=hex(int(num4, 2))
    print("The number conversion is=", x4)


def value5(num5):
    x5=oct(int(num5, 2))
    print(" The number conversion is=", x5)


def value6(num6):
    x6= int(num6, 8)
    print(" The number conversion is=", x6)


def value7(num7):
    x7= int(num7, 16)
    print(" The number conversion is= ", x7)


def value8(num8):
    x8= bin(int(num8 , 8))
    print(" The number conversion is= ", x8)

def value9(num9):
    x9= bin(int(num9, 16))
    print(" The number conversion is= ", x9)

def value10(num10):
    x10 = hex(int(num10 , 8))
    print(" The number conversion is= ", x10)


def value11(num11):
    x11 = oct(int(num11 , 16))
    print(" The number conversion is= " ,x11)

choice= " "
print(" PRESS 1 TO CONVERT DECIMAL INTO BINARY")
print(" PRESS 2 TO CONVERT DECIMAL INTO HEXADECIMAL")
print(" PRESS 3 TO CONVERT DECIMAL INTO OCTAL")
print(" PRESS 4 TO CONVERT BINARY INTO DECIMAL")
print(" PRESS 5 TO CONVERT BINARY INTO HEXADECIMAL")
print(" PRESS 6 TO CONVERT BINARY INTO OCTAL")
print(" PRESS 7 TO CONVERT OCTAL INTO DECIMAL")
print(" PRESS 8 TO CONVERT HEXADECIMAL INTO DECIMAL")
print(" PRESS 9 TO CONVERT OCTAL INTO BINARY")
print(" PRESS 10 TO CONVERT HEXADECIMAL INTO BINARY ")
print(" PRESS 11 TO CONVERT OCTAL INTO HEXADECIMAL")
print(" PRESS 12 TO CONVERT HEXADECIMAL INTO OCTAL")
while choice != 13 :
    choice = int(input(" ENTER YOUR CHOICE:  "))
    if choice == 1:
        a = int(input("ENTER ANY NUMBER : "))
        value(a)
    elif choice == 2:
        b = int(input(" ENTER ANY NUMBER : "))
        value1(b)
    elif choice == 3:
        c = int(input("ENTER ANY NUMBER : "))
        value2(c)
    elif choice == 4:
        d = input(" ENTER BINARY NUMBER : ")
        value3(d)
    elif choice == 5:
        e = input(" ENTER BINARY NUMBER: ")
        value4(e)
    elif choice == 6:
        f= input(" ENTER BINARY NUMBER : ")            #value like: 111111
        value5(f)
    elif choice == 7:
        g= input(" ENTER OCTAL NUMBER: ")              #value like: 0o117
        value6(g)
    elif choice == 8:
        h= input(" ENTER ANY HEXADECIMAL NUMBER: ")    #value like: 0x4f
        value7(h)
    elif choice == 9:
        i= input(" ENTER ANY OCTAL NUMBER:  ")         #value like: 0o117
        value8(i)
    elif choice == 10:
        j = input(" ENTER ANY HEXADECIMAL NUMNER: ")   #value like: 45ab
        value9(j)
    elif choice == 11:
        k = input(" ENTER ANY OCTAL NUMBER: ")         #value like: 0o117
        value10(k)
    elif choice == 12:
        l= input(" ENTER ANY HEXADECIMAL NUMBER: " )   #value like: 0x27e
        value11(l)
    else:
        print("  EROOR! INVALID CHOICE")




#	//////////////////////////...........TRIGONOMETRIC FUNCTION............///////////////////////

import math
def sine_function(x):

     ans = math.sin(float(x))
     print("The Sine of " , x , " is " ,float(ans))
result=float(input("ENTER THE VALUE ")     )
sine_function(result)

def cos_function(x):

      ans = math.cos(float(x))
      print("The Cos of " , x , "is" ,float(ans))
result=float(input("ENTER THE VALUE ")   )
cos_function(result)

def tan_function(x):

      ans = math.tan(float(x))
      print("The Tan of " , x , "is" ,float(ans))
result=float(input("ENTER THE VALUE ")       )
tan_function(result)


def cosec_function(x):               

      ans= (1/math.sin(x))
      print("The Cosec of " , x , "is" ,float(ans))
result=float(input("ENTER THE VALUE ")   )
cosec_function(result)


def sec_function(x):

      ans = (1/math.cos(x))
      print("The Sec of " , x , "is" ,float(ans))
result=float(input("ENTER THE VALUE ")   )
sec_function(result)


def cot_function(x):

      ans =(1/ math.tan(x))
      print("The Cot of " , x , "is" ,float(ans))
result=float(input("ENTER THE VALUE ")  )
cot_function(result)

def degree_to_radians(x):

         ans = math.radians(x)
         print("The radian of " ,x ," is ",float(ans))
result=float(input("Input degree: "))
degree_to_radians(result)

def radians_to_degree(x):

         ans = math.degrees(x)
         print("The degree of " , x ," is ",float(ans) )
result=float(input("Input radians: "))
radians_to_degree(result)



#	///////////////////////........ARITHMETIC OPERATIONS..............///////////////////


def addition( ):
 num1=input("Enter first number for addition : ")
 num2=input("Enter second number for addition : ")
 res=float(num1)+float(num2)
 print(f"Result : {num1} + {num2} = {res}")


def subtraction( ):
 num1=input("Enter first number for subtraction : ")
 num2=input("Enter second number for subtraction : ")
 res=float(num1)-float(num2)
 print(f"Result : {num1} - {num2} = {res}")


def multiplication( ):
 num1=input("Enter first number for multiplication : ")
 num2=input("Enter second number for multiplication : ")
 res=float(num1)*float(num2)
 print(f"Result : {num1} * {num2} = {res}")


def division( ):
 num1=input("Enter dividend : ")
 num2=input("Enter divisor : ")
 if num2==0:
  print("Zero division error ")
 else:
  res=num1/num2
  mod=num1%num2
  print(f"Result : {num1} / {num2} = {res}")
  print(f"Remainder of above division = {mod} ")


def power( ):
 num1=input("Enter any number : ")
 p=input("Enter power for the above number for calculatio : ")
 res=int(num1)**(p)
 print(f"Result : {num1} raise to the power {p} = {res}")


def square_root( ):
 num1=int(input("Enter number whose square root you want to calculate :"))
 res=sqrt(num1)
 if sqrt<0 :
  print(f"This calculator does not show result in imaginary values")
 else:
  print(f"Result :Square root of {num1} = {res}")


# ////////////////............LOGICAL OPERATOR............../////////////////


def Not():
    print ("NOT OPERATOR")
    print (" Enter any binary number")
    a=int(input(""))
    if a<0 or a>1:
        print (" Invalid Input ")
        exit()
    else:
        if a==0:
            res=1
        else:
            res=0
    print(res)

def Or():
    print("OR OPERATOR")
    print(" Enter first binary number")
    a=int(input(""))
    print(" Enter second binary number")
    b=int(input(""))
    if a<0 or a>1 or b<0 or b>1:
        print (" Invalid Input ")
        exit()
    else:
        res=a+b
        if res>1:
            res=1
    print(res)

def Nor():
    print("NOR OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a<0 or a>1 or b<0 or b>1:
        print (" Invalid Input ")
        exit()
    else:
        res=a+b
        if res>1:
            res=1
    res=res+1
    if res>1:
        res = 0
    print(res)

def And():
    print("AND OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a<0 or a>1 or b<0 or b>1:
        print (" Invalid Input ")
        exit()
    else:
        res=a*b
    print(res)

def nand():
    print("NAND OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a<0 or a>1 or b<0 or b>1:
        print (" Invalid Input ")
        exit()
    else:
        res=a*b
    res = res + 1
    if res > 1:
        res = 0
    print(res)

def xor():
    print("XOR OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a<0 or a>1 or b<0 or b>1:
        print (" Invalid Input ")
        exit()
    else:
        if a==b:
            res=0
        else:
            res=1
    print(res)

def xnor():
    print("XNOR OPERATOR")
    print(" Enter first binary number")
    a = int(input(""))
    print(" Enter second binary number")
    b = int(input(""))
    if a<0 or a>1 or b<0 or b>1:
        print (" Invalid Input ")
        exit()
    else:
        if a==b:
            res=0
        else:
            res=1
    res = res + 1
    if res > 1:
        res = 0
    print(res)

Not()
Or()
Nor()
And()
nand()
xor()
xnor()

