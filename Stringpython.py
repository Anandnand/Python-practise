s1="pavan"
s2=s1.lower()
if id(s1)==id(s2):
    print("Id's are equal")
else:
    print("Id's are not equal")



#values
if s1==s2:
    print("values are equal")
else:
    print("values are not equal")


# String formatting
name="Rajappa"
age=15
print(f"my name is {name} and my age is {age}")

print("my name is {1} and my age is {0}".format(name,age))#based on index

#Inbuilt methods
s5="Sudeep"
print(s1.upper())

s="Rohith sharma is a great captain"
print(s.title())
print(s.capitalize())

#splits the words and into a list
print(s.split())


    

    






    

    
