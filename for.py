'''
s1="kodnest"
for i in s1:
    print(i ,end=" ")



#printig 1 to 10
for i in range(0,10,1):
  print(i ,end=" ")

print("============================================================")


#printing prime numbers
a=0
b=30
count=0
  for i in range(a,b,1):
      for j in a%b==0:
          count++
'''
print("============================================================")

'''
lst=list(eval("10,20,30,40,50"))
print(lst)

t1=eval("1,2,3,4,5,6")
print(t1,type(t1))  #default type is tuple
'''
print("============================================================")

#print all the even numbers from the list by taking element by the user
'''
count=int(input("Enter the size of elements to be taken= "))
lst1=[]
for i in range(count):
  lst2=int(input("enter the number= "))
  lst1.append(lst2)
print(lst1,type(lst1))

El=[]
for i in lst1:
  if i%2==0:
    El.append(i)
print(El)
'''

print("============================================================")
#comprehensive
lst=input("Enter the number, separated with spaces")
even_list=[int(i) for i in lst.split()]
El=[i for i in even_list if i%2==0]
print(El)


#print square of number
sq=input("Enter the numbers to be squared,separated with spaces")
num_list=[int(i) for i in sq.split()]

squared=[i**2 for i in num_list]
print(squared)


'''
print("============================================================")

#Break
for i in range(1,11):
  if i==7:
    break
  print(i)

print("============================================================")

#continue
for i in range(1,11):
  if i==7:
    continue
  print(i)
'''




