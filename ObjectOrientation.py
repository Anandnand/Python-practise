class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def study(self):
        print(self.name,"is studying")
    def playing(self):
        print(self.name,"is playing")
    def writing(self):
        print(self.name,"is writing")
s1=Student("Rajappa",23,99)
print("Name is",s1.name,"age is",s1.age,"marks is",s1.marks)
s1.study()
s1.playing()
s1.writing()


        
#method overloading is not possible

class Employees:
    def has(self):
        print("Employee id is 01")
    def has(self,name):
        print("Employee id is 01 name is",name)
el=Employees()
#el.has()#error
el.has("pavan")

#Constructor overloading is not possible

class Employees:
    def __init__(self):
          print("Employee id is 01")

    def __init__(self,name):
        self.name=name
#el=Employees() #error
el=Employees("harsha")
print(el.name)





        
    




        
    
