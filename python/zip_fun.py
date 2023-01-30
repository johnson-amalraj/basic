list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']

# In python2 we can update like below
# zipped = zip(list1, list2)
# But in python3 we need to update like below
zipped = list(zip(list1, list2))
print(zipped)

# If two list are not in same length it will zip the same length content from each list

# Below iz unzip the content from zipped variable
# *zipped
unzipped = list(zip(*zipped))
print(unzipped)

# for (l1, l2) in zip(list1, list2):
#     print(l1)  
#     print(l2)  

sentences = []
items  = ['Potato', 'Tomato', 'Onion']
counts = ['7', '8', '9']
prices = ['10', '20', '30']

for (item, count, price) in zip(items,counts,prices):
    # print('I bought',count,item,'at',price,'rupees')
    item, count, price = str(item), str(count), str(price) 
 # The above line may not need (its convert as string) its casting to string 
    sentence = 'I bought'+' '+count+' '+item+'s'+' '+'at'+' '+price+' ''rupees each'+'.'
    sentences.append(sentence)

print(sentences)