basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruit=set(basket)
print fruit   #here you see no duplicate entry
a = set('abracadabra')
print a
b = set('alacazam')
print b
print a - b   #letters in a but not in b
print a&b    #letters in both a and b
print a|b    #letter in either a or b
print a ^ b  #letters in a or b but not both 
#similar to
a = {x for x in 'alacazam' if x not in 'abracadabra' }
print a

 
