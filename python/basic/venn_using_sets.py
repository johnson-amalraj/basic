# venn diagrams can be implement by using sets

colors_1 = {'black', 'red', 'blue', 'green'}
colors_2 = {'grey', 'black', 'red'}

# A 'union' B
all_colors = colors_1.union(colors_2)
print(all_colors)

# A 'intersect' B
common_colors = colors_1.intersection(colors_2)
print(common_colors)

# A 'difference' B
odd_colors_1 = colors_1.difference(colors_2)
odd_colors_2 = colors_2.difference(colors_1)
print(odd_colors_1) 
print(odd_colors_2) 