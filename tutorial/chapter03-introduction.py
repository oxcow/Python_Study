# -*- coding: utf-8 -*-

#

count = 3

print(2 ** count)

print(r'this is a \noriginal string')

print("this is a \n test")

print('''\
many string 
many string\
	''')

stringEnd = 'end'
joinString = 3 * 'AB' + 'CD' 'EF' 'HT' + stringEnd

print(joinString)

print(joinString[0], joinString[1], joinString[-1])

print(joinString[0:2], joinString[-4:12])

print(len(joinString))

print(joinString.capitalize())

print(joinString.casefold())

print('S' + joinString.center(20) + 'E')

print(joinString.count('AB', 0, 5))

print(joinString + " endwith 'END' (ignore case)", joinString.casefold().endswith('end'))

tabString = '01\t012\t0123\t01234'

print(tabString)

print(tabString.expandtabs(4))

print(joinString.find('CD', 4))
print('AB' in joinString)

print('the sum of 1 + 2 is {0} {1}'.format(1 + 2, 'ABC'))

class Default(dict):
	def __missing__(self, key):
		return key

output = '{name} was born in {country}'.format_map(Default(name='Guido'))

print(output)

print(joinString.index('e'), joinString.isalpha())

print(joinString.isalnum())
print('d'.isalnum(), ' d is digit:', 'd'.isdigit())
print("d is decimal:",'d'.isdecimal(), ", 12 is decimal:", '12'.isdecimal(), ", 12 is digit:", '12'.isdigit())

print(joinString, 'is lower:', joinString.islower(), ',is upper:', joinString.isupper())

print(','.join(joinString))

print(joinString.ljust(24,'*'))
print(joinString.rjust(24,'*'))
print(joinString.lstrip('AB'))
print(joinString.rstrip('edn'))
 
print(joinString.swapcase());
print("we are family".title());
print("we are family".translate({'w': "x", 'a':"y"}))

bytesString = b'this is a bytes'
print(len(bytesString))

sets = set({1,'S',4})
sets.add(2)
sets.remove('S')
print(sets, len(sets), ' 1 in sest?', 1 in sets)

frozensets = frozenset({1,'s',3,5})
print(frozensets)
print(frozensets, '>', sets, "?", frozensets > sets)

set1 = ({1,2,3,4})
set2 = set({3,4,5,6})
set1sub = set({1,3})
set3 = set({'a','b'})
print(set1sub, 'is', set1, 'sub?', set1sub.issubset(set1))
print(set1, 'is', set1sub, 'super set?', set1.issuperset(set1sub))
print(set1, 'is', set3, "disjoint?", set1.isdisjoint(set3))
print(set1, 'union', set2, "=>", set1.union(set2))
print(set1, 'intersection', set2, "=>", set1.intersection(set2))
print(set1, 'difference', set2, "=>", set1.difference(set2))
print(set1, 'symmetric_difference', set2, "=>", set1.symmetric_difference(set2))

dicts1 = {'one':1,'two':2,'three':3}
dicts2 = dict(one = 1, two = 2, three = 3)
print(dicts1, dicts2, dicts1 == dicts2)
print(len(dicts1), list(dicts1))
print(dicts1.items(), dicts1.keys())

print(dicts2)
dicts2.update(dict(three = 4))
print(dicts2)

for i in dicts2.items():
	print(i, "=>", i[0], ":", i[1])


a, b = 0, 1
while a < 10:
	print(a)
	a, b = b, a+b

