# -*- coding: utf-8 -*-

# https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html

# 5. 数据结构

## 5.1 列表的更多特性

print('-' * 20, '5.1. 列表的更多特性', '-' * 20)

fruits = ['orange', 'apple', 'pear', 'banana']

fruits.append('banana')

print(fruits)

fruits.extend(["a","b"])
fruits.extend(("c","d"))

print("after extend:", fruits)

fruits.insert(0, 'start')

print('insert elemen at begin:', fruits)

fruits.remove('a')

print('after remove a:', fruits)

last = fruits.pop()
print('pop last element is:',last, fruits)

first = fruits.pop(0)
print('pop first element is:', first, fruits)

clone_fruits = fruits[:] # eq fruits.copy()
print('clone fruits is:', clone_fruits)

fruits.clear() # equal del fruits[:]

print('after clean fruits.', fruits)

banana_count = clone_fruits.count('banana')
print("banana display count:", banana_count)

print('fruits sort before:', clone_fruits)
clone_fruits.sort()
print('fruits sort after:', clone_fruits)
clone_fruits.reverse()
print('fruits reverse after:', clone_fruits)

### 5.1.1. 列表作为栈使用

print('-' * 20, '5.1.1. 列表作为栈使用', '-' * 20)

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print(stack)

print(stack.pop())
print(stack.pop())

### 5.1.2. 列表作为队列使用

print('-' * 20, '5.1.2. 列表作为队列使用', '-' * 20)

# 使用列表实现队列比较低效，可用collections.deque实现

from collections import deque

queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.append('Graham')

print(queue)

print(queue.popleft())
print(queue.pop())

print(queue)

### 5.1.3. 列表推导式

print('-' * 20, '5.1.3. 列表推导式', '-' * 20)

squares = []
for x in range(10):
    squares.append(x**2)

print(squares, ',x:', x)

squares1 = list(map(lambda y: y**2, range(10)))
print(squares1)  # y is not defined

squares2 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print (squares2)

# 下面代码等价squares2
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
print(combs, ", squares2 == combs?", squares2 == combs)

vec = [-4, -2, 0, 2, 4]

vec1 = [x*2 for x in vec]
print(vec1)

vec2 = [x for x in vec if x >= 0]
print(vec2)

vec3 = [abs(x) for x in vec]
print(vec3)

freshfruit = [' banana', '  loganberry', 'passion fruit  ']

freshfruit1 = [weapon.strip() for weapon in freshfruit]
print(freshfruit1)

print([(x, x**2) for x in range(6)])

# print([x, x**2 for x in range(6)]) # invalid syntax

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

from math import pi

pi_test = [str(round(pi, i)) for i in range(1, 10)]

print(pi_test)

### 5.1.4. 嵌套的列表推导式

print('-' * 20, '5.1.4. 嵌套的列表推导式', '-' * 20)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

change_col_row = [[row[i] for row in matrix] for i in range(4)]

print(matrix)
print(change_col_row)


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

transposed.clear()
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print (transposed)

print(list(zip(*matrix)))

## 5.2 del 语句

print('-' * 20, '5.2. del 语句', '-' * 20)

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)

del a[0]
print("after del a[0]:", a)

del a[2:4]
print("after del a[2:4]:", a)

del a[:]
print("after del a[:]:", a)

## 5.3. 元组和序列
print('-' * 20, '5.3. 元组和序列', '-' * 20)

t = 12345, 54321, 'hello!'
print(t[0], t)

u = t, (1, 2, 3, 4, 5)
print(u, ', u[0]', u[0][1])

empty = ()
signleton = 'hello',
print("empty len:", len(empty), ',signleton len:', len(signleton))

print("empty:", empty, ", signleton:", signleton)

x, y, z = t
print('x =', x, ", y =", y, ', z =', z)


## 5.4. 集合
print('-' * 20, '5.4. 集合', '-' * 20)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

print('oragne in basket?', 'orange' in basket)
print('crabgrass in basket?', 'crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')

print("a:", sorted(a))
print("b:", sorted(b))
print("a - b =", sorted(a - b))
print("a | b =", sorted(a | b))
print("a & b =", sorted(a & b))
print("a ^ b =", sorted(a ^ b))

empty_set = set()
print('empty set:', empty_set, ', len:', len(empty_set))

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)


## 5.5. 字典
print('-' * 20, '5.5. 字典', '-' * 20)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print('dict tel:', tel, ', jack is tel is:', tel['jack'])

del tel['sape']
tel['irv'] = 4127
print('del sape tel add irv:', tel)

print('list tel:', list(tel), ', sorted tel:', sorted(tel))
print('guido in tel?', 'guido' in tel, '; jack not in tel?', 'jack' not in tel)

c = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('c dict is:', c)

e = {x: x**2 for x in (2, 4, 6)}
print('e dict is:', e)

f = dict(sape=4139, guido=4127, jack=4098)
print('f dict is:', f)


## 5.6. 循环的技巧
print('-' * 20, '5.6. 循环的技巧', '-' * 20)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

enums = enumerate(['tic', 'tac', 'toe'])
print("enums:", enums)
for i, v in enums:
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print("What's your {0}? It is {1}.".format(q, a))

for i in reversed(range(1, 10, 2)):
    print(i)

for f in sorted(set(basket)):
    print(f)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)


## 5.7. 深入条件控制
print('-' * 20, '5.7. 深入条件控制', '-' * 20)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'

non_null = string1 or string2 or string3
print("non null?", non_null)

print(3 < 2 == 2)

## 5.8. 比较序列和其他类型
print('-' * 20, '5.8. 比较序列和其他类型', '-' * 20)

print('(1,2,3) < (1,2,4) ?', (1,2,3) < (1,2,4))
print('[1,2,3] < [1,2,4] ?', [1,2,3] < [1,2,4])

print('(1,2,3,4) < (1,2,4) ?', (1,2,3,4) < (1,2,4))
print('(1,2) < (1,2,-1) ?', (1,2) < (1,2,-1))
print('(1,2,3) == (1.0,2.0,3.0) ?', (1,2,3) < (1.0,2.0,3.0))
print("(1, 2, ('aa', 'ab')) == (1, 2, ('abc', 'a'), 4) ?", (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
