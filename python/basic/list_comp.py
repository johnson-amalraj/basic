# List Comprehension 

names = ['name1', 'name2', 'name3']

new_list = []
for person in names:
    new_list.append(person)
print(new_list)

print([person for person in names])
# it will do same thing like above for loop    

# we can do numerical operationon list
new_list = []
for person in names:
    new_list.append(person + '_python')
print(new_list)

print([person + '_python' for person in names])
# it will do same thing like above for loop    


movies = {'movie1' : 9, 'movie2': 8, 'movie3': 7, 'movie4': 2, 'movie5': 1}
movie = []

for rate in movies:
    if movies[rate] > 6:
        movie.append(rate)
print(movie)   

print( [movie for movie in movies if movies[movie] > 6] )
# it will do same thing like above for loop    