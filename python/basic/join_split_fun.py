months = 'jan feb mar apr may jun jul'
print(months)

# Split the sentence
M = months.split(' ')
print(M)
# Here M working as 'list'

M = months.split('apr')
print(M)

# Join operation
joined = '=>'.join(M)
print(joined)

joined = ''.join(M)
print(joined)