# Mutability -> Changeable (Flexible data)
# Example:- list, dictionary, ordered dictionary
# Immutability -> Unchangeable (Secure data) 
# Examples:- tuple, int, float, string, boolean


tup = (1,2,3) # Tuple
print(tup);
# tup[0] = 7 --> This will give error
# We can not add like above because its immutable

tup = (1,2, [3,5,7]) # Tuple with a List
print(tup);

# Here list is mutable
tup[2][2] = 9; 
# We can change the value inside the tuple because [2] index of tuple is a list
# List is mutable
print(tup);