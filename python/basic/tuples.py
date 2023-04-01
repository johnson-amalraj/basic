# Its a data type
# Its defined as list with constarins
# Stable and structured kind of data type
# Every element of tuple has consistent meaning

tup = (1,2,3,4,5,6,7)
print(tup[6])
print()

card1 = (4567321245, 'name1' , '25/2020', 456)
card2 = (4583157245, 'name2' , '18/2020', 789)

cards = [card1, card2]
print(cards)
print()

# Packing of tuple
(card_num, name, expiry, cvv) = card1
# We can use like this -> card_num, name, expiry, cvv = card1
print('PACKING TUPLE')
print(card_num)
print(name)
print(expiry)
print(cvv)
print()

# Unpacking tuple
for card_num, name, expiry, cvv in cards:
    print('UNPACKING TUPLE')
    print(card_num)
    print(name)
    print(expiry)
    print(cvv)
    print()