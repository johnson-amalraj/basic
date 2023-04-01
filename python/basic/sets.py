# Get rid of duplicates
# You can not add duplicates in a set
# Its unordered

s = {'black', 'red'} 
print(s)

s.add('blue')
print(s)

s.add(7)
print(s)

s.add('blue')
print(s) # Its not print 'blue' as two times

li = [1,2,3,4,6,4,3,2,1,4]
print(li) 
se = set(li) # 'List' is casting as 'set'
print(se) # duplicates entry removed
li = list(se)
print(li)