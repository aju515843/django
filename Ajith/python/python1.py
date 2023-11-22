# x=10
# y=20
# print(float(x))
# print(float(y))
# print(complex(y))
# print(complex(x))
# print(int(x))


# a=5
# b=6

# a+=5
# b-=5
# print(a)
# print(b)

# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

# a,b=b,a
# print(a,b)

# if(10<11):
#   print("greater")




# if(6>5):
#       print("greater")
# else:
#       print("smaller")


 
'''?)find greater number the 3 digits given by the user?'''
# a=int(input("enter the first value"))
# b=int(input("enter the second value"))
# c=int(input("enter the 3rd value"))    
# if(a>b):
#     if(a>c):
#         print("first value is greater")
#     else:
#          print("3rd value is greater")
# elif(b>c):
#     print("second value is greater")
# else:
#     print("3rd value is greater") 



'''?)check whether the given number is even or odd?'''
# a=int(input("enter the value"))
# elif(b>c):
#     print("second value is greater")
# if(a%2==0):
#    print("number is odd")
# else:
#    print("number is even")



'''?)leap year?'''
# a=int(input("enter year"))
# if(a%4==0):
#     print("is a leap year")
# else:
#     print("is not a leap year")



'''?)tuple'''
# t=(1,2,3,4,5,"hai")
# y=list(t)
# y[5]="hello"
# t=tuple(y)
# print(t)   



'''?)list'''
# list1=[1,2,9,4,5,6,7]
# list1[3]=3
# print(list1)



'''?)set'''
# s={1,2,3,4,5,"hai"}
# y=list(s)
# y[3]="hello"
# s=set(y)
# print(s)


'''?) WAP to check whether the last digit of a number is divisible by 3 or not?'''
# a=int(input("enter a number"))
# if(a%3!=1):
#   print("number is divisible by 3")
# elif(b>c):
#     print("second value is greater")
# else:
#   print("numbe not divisible by 3") 


   
'''?)display "HELLO" if entered number is divisible by 5 otherwise print bye'''
# a=int(input("enter number"))
# if(a%5!=1):
#   print("HELLO")
# else:
#   print("Bye") 



'''?)to accept percentage from the user and display the grade according following criteria'''
# n=int(input("enter mark"))
# if(n>90):
#   print("A grade")
# elif(n>80 and n<=90):
#   print("B grade")
# elif(n>=60 and n<=80):
#   print("C grade")
# elif(n<60):
#   print("D grade")  



'''?)wirte a program to display the last digits of a number.'''
# a=int(input("enter a number"))
# x=a%10
# print("the last digits is",x)


'''?) calculate electricity bill.'''
# a=int(input("enter the unit of electric?) calculate electricity bill.ity"))
# if(a<100):
#     print("no charge")
# elif(a>100 and a<=200):
#     x=(a-100)*5
#     print("electricity bill",x)
# elif(a>200):
#     x=500+(a-200)*10
#     print("electricity bill",x)
    



'''?)Write a program that takes a list of strings as input and outputs the length of each string using a while loop.'''
# n=int(input("Enter limit"))
# i=1
# list=[]
# count=[]
# while(i>=0 and i<=n):
#     a=input("enter the string")
#     list.append(a)
#     b=len(a) bill",x)
    





'''?)Write a program that takes a list of strings as input and outputs the length of each string using a while loop.'''
# n=int(input("Enter limit"))
# i=1
# list=[]
#     count.append(b)
#     i=i+1 
# print(list)
# print(count)    



'''# ?)Write a program that takes a string as input and outputs the number of times each character appears in the string using a while loop. '''   
# string=input("Enter string")
# print(string)
# char=input("Enter charecter to be counted")
# i=0
# count=0
# while(i<len(string)):
#     if(string[i]==char):
#         count=count+1
#     i=i+1 
# print("Number of charecter appered is",count)    


'''?)Write a program that takes two lists of integers as input and returns a list containing the common elements using a while loop.'''
# n=int(input("Enter the first limit"))
# i=1
# list1=[]
# list2=[]
# result=[]
# while(i>=0 and i<=n):
#     a=int(input("Enter the integers"))
#     list1.append(a)
#     i=i+1
# m=int(input("Enter the second limit"))
# j=1
# while(j>=0 and j<=m):
#     b=int(input("Enter the integers"))
#     list2.append(b)
#     j=j+1
# k=0
# while(k<len(list1)):
#     if(list1[k] in list2):
#         result.append(list1[k])
#         k=k+1
#     print(list1)
#     print(list2)
#     print(result)          


'''?)Write a program that takes a string as input and outputs the string in reverse order using a while loop.'''
# n=int(input("Enter a string"))
# reverse=0
# while(n!=0):
#     x=n%10
#     reverse=reverse*10+x
#     n//=10
# print(reverse)    

'''?)Write a program that takes a list of integers as input and outputs the sum of the integers using a while loop.'''
# n=int(input("Enter the value:"))
# sum=0
# while(n>=0):
#     sum+=n
#     n-=1
    
# print("sum is",sum)




'''A
AB
ABC '''  
# for i in range (65,70):
#     for j in range(65,i+1):
#         print(chr(j),end="")
#     print()

'''A
BC
DEF'''
# n= 65
# for i in range(0,6):
#     for j in range(0,i+1):
#         char = chr(n)
#         print(char,end="")
#         n += 1?) calculate electricity bill.
#     print()

# A
# BA
# CBA
# n=65
# str="ABC"
# for i in range(0,3):
#     for j in range(0,i+1):
#         k=j-1
#         print(str[k],end="")
#     print()


'''P
PY
PYT
PYTH
PYTHO
PYTHON
PYTHO
PYTH
PYT
PY
# P'''
# str="PYTHON"
# for i in range(0,6):
#     for j in range(0,i+1):
#         print(str[j],end="")
#     print()
# for i in range(6,0,-1):
#     for j in range(i):
#         print(str[j], end='')
#     print()     




'''?)paliandrome,find the words is a string/sentence which are paliandrome and convert the words of each charecter with @.'''
# n=input("enter a string")
# y=n.split()
# s=''
# for i in y:
#     x=i[::-1]
#     if i.lower()==x.lower():
#         # print("@"*len(i))
#         s+="@"*len(i)
#     else:       
#       s+=i
#     print(s) 

 
'''?)****
  *******
  ***
  **
  *****'''
# l=[4,7,3,2,5]
# for i in range(0,len(l)):
#     for j in range(0,l[i]):
#         print("*",end="")
#     print()


'''# functions'''
# def add(a,b):
#     sum=a+b
#     print(sum)
# add(11,5)
# add(6,7)



'''# write a function that takes a  name as input and returns the name with all initials capitalized. for example, if the input is "john smith," the output should be "John Smith".?'''
# n=input("enter the name")
# def title(n):
#  print("after capitalize",)
# print(n.title())

'''# remove special charecters
# string is:"hello@#$%$@#%"
# output will be:hello'''
# n=input("Enter string:")
# print("before conversion",n)
# m=""
# for i in n:
#     if i.isalnum():
#         m+=i
# print(m)
 
        

'''factorial of number'''
# n=int(input("enter a number"))
# fact=1
# if(n<0):
#   print("negative number")
# elif(n==0):
#   print("factorial zero is 1")
# else:    
#   for i in range(1,n+1):
#       fact=fact*i
#   print("Factorial of",n,"is",fact)


'''fibanocii series'''
# n=int(input("enter a number"))
# a=0
# b=1
# print("fibanocci series is:",a,b,end="")
# for i in range(2,n):
#     k=a+b
#     a=b
#     b=k
#     print(k,end=" ")
# print()   


'''prime number series'''
# n=int(input("enter the starting limit"))
# m=int(input("enter the end point"))
# print("prime number b/w",n,"and",m,"are:")
# for num in range(n,m+1):
#     if(num>1):
#         for i in range(2,num):
#             if(num%i)==0:
#                 break
#         else:
#             print(num)
          


'''convert a decimal number to binary,octal and hexadecimal using function'''
# dec=int(input("Enter a number:"))
# def convertToBinary(n):
#     if(n>1):
#         convertToBinary(n//2)
#     print(n%2,end="")
# def convertToOctal(n):
#     if(n>1):
#         convertToOctal(n//8)
#     print(n%8,end="")
# def convertToHexadecimal(n):
#     if(n>1):
#         convertToHexadecimal(n//16)
#     print(n%16,end="")    
# convertToBinary(dec)
# print(" is a Binary number")
# convertToOctal(dec)
# print(" is a Octal number")
# convertToHexadecimal(dec)
# print(" is a Hexadecimal number")
      

'''implement a function that sorts a list of numbers in ascending or decending order according to the user input.'''
# list=[11,3,7,5,6]
# list.sort()
# print("Acending Order",list)  
# list.sort(reverse=True) 
# print("Descending Order",list) 


'''WAP that simulates a game of rock paper scissors.The program should ask the user for their choice.
*rock beats scissors
*scissors beats paper
*paper beats rock'''
# import random
# print("select from the list")
# print("1).Rock")
# print("2).Paper")
# print("3).Scissors")
# user=input("Enter the choice:")
# r=["rock","paper","scissors"]
# com=random.choice(r)
# if(user==com):
#     print("Its a tie")
# elif(com==r[0] and user==r[2]):
#     print("computer wins")
# elif(com==r[1] and user==r[0]):
#     print("computer wins")
# elif(com==r[2] and user==r[1]):
#     print("computer wins")
# elif(user==r[0] and com==r[2]):
#     print("user wins")
# elif(user==r[1] and com==r[0]):
#     print("user wins")
# elif(user==r[2] and com==r[1]):
#     print("user wins") 
# else:
#     print("invalid option")                           



'''write a program that asks the user for a password and checks if it means the following criteria: at least 8 charecters long,contains at least one uppercase letter,and
contains at least one digit.print "valid password" if the password meets the criteria, and "invalid password" if does not'''
# import re
# password=input("Enter your password:")
# def n(password):
#     if len(password)<8:
#         return False
#     if  re.search("[a-z]",password):
#         return True
#     if  re.search("[A-Z]",password):
#         return True
#     if  re.search("[0-9]",password):
#         return True
#     return True
# if n(password):
#     print("valid password")
# else:
#     print("invalid passsword")


'''roman numerals convert it to an integer'''
# n=input("Enter an number:")
# roman={"I":1,
#        "V":5,
#        "X":10,
#        "L":50,
#        "C":100,
#        "D":500,
#        "M":1000
#       }
# int_value=0
# i=0
# if i in range(len(n)):
#     if n[i] in roman:
#       if i+1<len(n) and roman[n[i]]<roman[n[i+1]]:
#         int_value-=roman[n[i]]
#       else:
#         int_value+=roman[n[i]]    
#       print("the integer value is:",int_value)
#     else:
#        print("invalid input.")


'''create a circle class and initialize it with radius.Make two methods getArea and getCircumference inside this class'''
# class circle:
#     def __init__(self, radius):
#         self.radius=radius
#     def circle_area(self):
#         return f"{self.radius*radius*3.14}"
#     def circle_circumferance(self):
#         return f"{self.radius*3.14*2}"
# radius=float(input("Enter the radius:"))
# circle=circle(radius)
# area=circle.circle_area()
# circumferance=circle.circle_circumferance()
# print("Area of the circle:",area)
# print("circumferance of the circle:",circumferance)  

'''create a temrature class.Make two methods
1.convertFahrenheit-it will take celsius and will print it into Fahrenheit.
2.convertCelsius-it will take Fahrenheit and will convert it into Celsius.'''
# class temrature:
#   def __init__(self,tem):
#     self.tem = tem
#   def convertFahrenheit(self):
#     return f"{(self.tem*1.8)+32}"
#   def convertCelsius(self):
#     return f"{((self.tem-32)*5)/9}"  
# tem=float(input("Enter the temrature:"))
# temrature=temrature(tem)
# Fahrenheit=temrature.convertFahrenheit()
# celsius=temrature.convertCelsius()
# print("fahrenheit temrature:",Fahrenheit)
# print("celsius temrature:",celsius)




'''bank details'''
# class bank:
#     def __init__(self,name,num,bal):
#         self.name=name
#         self.num=num
#         self.bal=bal
#     def deposit(self):
#         amt=int(input("Enter the amount:")) 
#         self.bal+=amt
#     def withdraw(self):
#         amt=int(input("Enter the amount"))
#         self.bal-=amt
#     def showbal(self):
#         print(self.name,"\n",self.bal)
# l=[]
# def details():
#     n=input("Enter name:")
#     m=input("Enter accno:")
#     p=input("Enter balanace:")
#     x=bank(n,m,p)
#     l.append(x)
# while True:
#        choice=int(input("1.details \n2.deposit \n3.withdraw \n4.Balanace \n Enter your choice:"))
#        if choice==1:
#            details()
#        elif choice==2:
#            accno=int(input("Enter accno:"))
#            for i in l:
#                if accno==i.num:
#                    i.deposit()
#                    i.showbal()
#                else:
#                    print("check the number")    
#        elif choice==3:
#            i.withdraw()
#            i.showbalcreate a base class "shape" with a method "area" create derived classes " Rectangle" and "Circle" that inherit from "Shape" and implement the "area" method.()       
#        elif choice==4:
#            i.showbal()         
#        else:
#            print("invalid option")
#            break                            
    

# '''create a base class "shape" with a method "area" create derived classes " Rectangle" and "Circle" that inherit from "Shape" and implement the "area" method.'''
# class Shape:
#     def __init__(self,radius):
#         # self.length=length
#         # self.width=width
#         self.radius=radius
#     def Circle_area(self):
#         return f"{self.radius*radius*3.14}"
# radius=int(input("Enter the radius of the circle:"))
# Shape=Shape(radius)
# area_circle=Shape.Circle_area()  
# print("area of the circle is:",area_circle)    
# class Rectangle_shape:        
#     def Rectangle_area(self,length,width):
#         self.length=length
#         self.width=width
#         return f"{self.length*width}"
# length=int(input("Enter the length of the rectangle:"))
# width=int(input("Enter the width of the rectangle:"))   
# Rectangle_shape=Rectangle_shape(length,width)
# area_rectagle=Shape.Rectangle_area()
# print("area of the rectagle is:",area_rectagle)



'''python create,read and remove using file handling function files'''
# def rem():
#  import os
#  if os.path.exists("file1.txt"):
#     os.remove("file1.txt")
# def read():
#   f=open("file1.txt","r")
#   print(f.read())
# def write():
#    f=open("file1.txt","a")
#    f.write("\nAl-Nassr")
#    f.close()   
# print("FILE HANDLING")
# while True:
#     print("Choose Option")
#     print("1.Read")
#     print("2.Write")
#     print("3.Delete")
#     print("4.Exit")
#     Choice=int(input("Enter your choice:"))
#     if Choice==1:
#        print("***Reading file***")
#        read()
#     elif Choice==2:
#        print("***Writing file***")
#        write()
#     elif Choice==3:
#         print("***Removing file***")
#         rem()
#     elif Choice==4:
#        print("***Thank You! See you again***")
#        break


'''calculator'''
# from tkinter import *
# w=Tk()
# w.config(background='black')
# w.geometry('300x300')
# l1=Label(w,text='num1')
# e1=Entry(w,width=20)
# l2=Label(w,text='num2')
# e2=Entry(w,width=20)
# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)
# e1.grid(row=0,column=1,padx=10)
# e2.grid(row=1,column=1,padx=10)
# def add():
#     r=(int(e1.get())+int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)
# def sub():
#     r=(int(e1.get())-int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)
# def mul():
#     r=(int(e1.get())*int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)
# def div():
#     r=(int(e1.get())/int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)  
# b1=Button(w,text='ADD',command=add).grid(row=3,column=0)
# b2=Button(w,text='SUB',command=sub).grid(row=3,column=1)
# b3=Button(w,text='MUL',command=mul).grid(row=3,column=2)
# b4=Button(w,text='DIV',command=div).grid(row=3,column=3)
# e3=Entry(w,width=20)
# e3.grid(row=5,column=2)
# w.mainloop()


'''width,height,area'''
# from tkinter import *
# w=Tk()
# w.config(background='pink')
# w.geometry('300x300')
# l1=Label(w,text='Width')
# e1=Entry(w,width=25)
# l2=Label(w,text='Height')
# e2=Entry(w,width=25)
# l3=Label(w,text='Area')
# e3=Entry(w,width=25)
# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)
# l3.grid(row=2,column=0)
# e1.grid(row=0,column=1,padx=10)
# e2.grid(row=1,column=1,padx=10,pady=10)
# e3.grid(row=2,column=1,padx=10)
# def area():
#     r=(int(e1.get())*int(e2.get()))
#     e3.delete(0,END)
#     e3.insert(END,r)   
# b1=Button(w,text='Submit',command=area).grid(row=3,column=0,pady=10)
# w.mainloop()    

