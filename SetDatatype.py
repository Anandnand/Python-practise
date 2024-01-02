s1={10,20,30,"Anand",True}

# we can add the element
s1.add(40)
print(s1)

# we can remove the element
s1.remove(True)
print(s1)

#delete the element by last index
s1.pop()
print(s1)

#Union of sets
s3={1,2,3}
s4={3,4,5}
s5=s3|s4
print(s5)

#intersection of sets
s6=s3&s4
print(s6)

#isSuperset of set
#subset of set
s2={2,1}
s7=s2.issubset(s3)
print(s7)

s8=s2.issubset(s4)
print(s8)

#difference of set
s9=s4-s3
print(s9)

#update of set
print(s3.update(s4))#none
s3.update(s4)
print(s3)

# we can delete all the element
#s1.clear()
#print(s1)

