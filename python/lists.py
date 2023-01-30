# Lists is a type of Primitives 
# It called as data structure (but remember as data type)
# Example [1,2,3]
# We can have anything inside the list [1,2,"John",'john',True,False]
# [] its a Empty list
# Lsit was defined as Collection of all data types

l1 = [1,2,3]
l2 = [1,2,2.5,"John",'john',True,False,l1]

print(l1)
print(l1[0])
print(l1[1])

print(l2)

l2.append("Python")
print('Lets append the value "Python" to list ',l2)

l2.insert(2,"Python")
print('List after inserted Python',l2)

l2.remove("john")
print('List after removed john',l2)

l2.reverse()
print('Reversed list is ',l2)

l3 = [4, 8, 0, 2, 7]
l3.sort()
print('Sorted list is ',l3)

print("Length of List3 is ",len(l3))

for list3 in l3:
    print(list3)

# print(l2[0])
# print(l2[1])
# print(l2[2])
# print(l2[3])
# print(l2[4])
# print(l2[5])
# print(l2[6])
# print(l2[7])