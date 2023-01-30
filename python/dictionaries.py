# Super Organized data (mini database)
# Fast as hell (constant time)
# get()
# items()
# keys()
# values()
# pop()
# popitem()
# clear()
# from collections import OrderedDict

# dictionary = {'key':value}
fruits_dic = {'banana':8, 'orange':7}
print(fruits_dic.get('orange')) # same as 'print(fruits_dic['banana'])'
print(fruits_dic.get('apple')) # if we use 'print(fruits_dic['apple'])' -> it will throw error as 'KeyError'

print()
# ordered dictionary
print('Ordered Dictionary')
print(   sorted(  list(fruits_dic.values())  )   )

print()
# .items()
print(fruits_dic.items())
print(list(fruits_dic.items())) # prints like a 'list'

print()
# .keys()
print(fruits_dic.keys())
print(list(fruits_dic.keys())) # prints like a 'list'

print()
# .values()
print(fruits_dic.values())
print(list(fruits_dic.values())) # prints like a 'list'

print()
# adding entry to dictionary
print(fruits_dic)
fruits_dic['apple'] = 10
print(fruits_dic)

print()
print(fruits_dic)
# .clear()
print(fruits_dic.clear())
print('cleared dictionary')

print()
fruits_dic = {'banana':5, 'orange':7}
# to delete selected entry from dictionary
# .pop(key)
print(fruits_dic)
fruits_dic.pop('banana')
print(fruits_dic)

print()
fruits_dic = {'banana':5, 'apple':9, 'orange':7}
# to delete last entry from dictionary
# .pop(key)
print(fruits_dic)
fruits_dic.popitem()
print(fruits_dic)



# inside the dictionary we can use list to store multiple data
contacts = {
    'name1' : [76765198976, 'email_addr1', 'home_addr1'],
    'name2' : [72657772987, 'email_addr2', 'home_addr2']
}   
print()
print(contacts['name1'])

# inside the dictionary we can use dictionary also
contacts = {
    'name1' : {'phone' :76765198976, 'email': 'email_addr1', 'Addr': 'home_addr1'},
    'name2' : {'phone' :72657772987, 'email': 'email_addr2', 'Addr': 'home_addr2'}
}   
print()
print(contacts['name1']) # TODO need to know about how to print phone alone in above dictionary


