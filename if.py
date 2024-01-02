#Syntax for if statement
'''
age=int(input("Enter the age= "))
if age>18:
    print("He is eligible to vote")
else:
    print("He is not eligible")

'''

#Syntax for if-elseif-else statement
'''
ch=input("Enter the character=" ).lower()
if ch in 'aeiou':
  print(ch,"is a vowel")
else:
    print(ch,"is a consonent")
'''
    
#printing odd or even numbers

'''
num=int(input("Enter a integer"))
if num%2==0:
    print(num,"is a even number")
elif num==0:
    print(num ,"is a zero")
else:
    print(num,"is a odd number")
'''

#print in a number which is present or not
'''
num1=int(input("Enter a number"))
         
if num1>0 and num1<10:
    print(num1,'is a present between 1 to 10')
else:
    print(num1,'is not present between 1 to 10')

'''

#Select a choice
num1=int(input("Enter a integer= "))
num2=int(input("Enter a number= "))
choice=int(input("Enter a choice 1-add,2-sub,3-mul,4-div= "))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
else:
    print("invalid choice")
