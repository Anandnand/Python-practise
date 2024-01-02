lst1=[10,20,30,"Anand",True]

# we can add the element
lst1.append(40)
print(lst1)

# we can remove the element
lst1.remove(True)
print(lst1)

#delete the element by last index
lst1.pop()
print(lst1)

#delete the element by position
lst1.pop(3)
print(lst1)

#delete the element by index del is a keyword
del lst1[1]
print(lst1)

# we can delete all the element
lst1.clear()
print(lst1)

