# -*- coding: utf-8 -*-

# https://docs.python.org/zh-cn/3.7/tutorial/inputoutput.html

# 7. 输入输出

## 7.1. 更漂亮的输出格式
print("-" * 20, '7.1. 更漂亮的输出格式', "-" * 20)

year = 2019
event = 'referendum'.title()

f = f'Results of the {year} {event}'

print(f)

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)

f = '{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)

print(f)

s = 'Hello, world.'
print(str(s))

print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) +  '...'

print(s)

hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
print(str(hello))

print(repr((x, y, ('spam', 'eggs'))))
print(str((x, y, ('spam', 'eggs'))))

### 7.1.1. 格式化字符串文字
print("-" * 20, '7.1.1. 格式化字符串文字', "-" * 20)

import math

print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!s}.')
print(f'My hovercraft is full of {animals!r}.')

### 7.1.2. 字符串的 format() 方法
print("-" * 20, '7.1.2. 字符串的 format() 方法', "-" * 20)

print('We are the {} who say "{}!"'.format('knight', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

print('The story of {0} {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8635}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
    'Dcab: {0[Dcab]:d}'.format(table))

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x**3))


### 7.1.3. 手动格式化字符串
print("-" * 20, '7.1.3. 手动格式化字符串', "-" * 20)

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x**3).rjust(4))


print('12'.zfill(5))
print('-3.14'.zfill(7))
print(str(math.pi).zfill(5))

### 7.1.4. 旧的字符串格式化方法
print("-" * 20, '7.1.4. 旧的字符串格式化方法', "-" * 20)


print('The value of pi is approximately %5.3f.' % math.pi)

## 7.2. 读写文件
print("-" * 20, '7.2. 读写文件', "-" * 20)

f = open('readme.md', 'r')
for line in f:
    print(line)
f.close()

print(f.closed)

with open('readme.md') as f:
    read_data = f.read()

print(read_data, ',file closed?', f.closed)


## 7.2.1. 文件对象的方法
print("-" * 20, '7.2.1. 文件对象的方法', "-" * 20)

with open('readme.md') as f:
    print('f.read() =>', f.read())

with open('readme.md') as f:
    print('f.readline() =>', f.readline())
    print('f.readline() =>', f.readline())
    print('f.readline() =>', f.readline())

with open('readme.md') as f:
    print('list(f) =>', list(f))

with open('readme.md') as f:
    print('f.readlines() =>', f.readlines())

with open('readme.md') as f:
    for line in f:
        print(line, end='')

print('\n', '-' * 60)

with open('file.txt', 'w+') as f:
    f.write('1 This is a test\n')
    f.write('2 This is a test\n')
    value = ('the answer', 42)
    f.write(str(value)+'\n')
    f.seek(0, 0)
    print(f.tell())
    f.write('the first line\n')
    f.seek(0, 2)
    f.write('the last line\n')

with open('file.txt') as f:
    for line in f:
        print(line, end='')

## 7.2.2. 使用 json 保存结构化数据
print("-" * 20, '7.2.2. 使用 json 保存结构化数据', "-" * 20)

import json

print(json.loads(json.dumps([1, 'simple', 'list'])))

data = {
    'no' : 1,
    'name' : "Runoob",
    'url' : 'http://www.baidu.com'
}

print('data:', data)

json_data = json.dumps(data, sort_keys=True, indent=4)
print('json data:', json_data)

data_from_json = json.loads(json_data)
print("from json data:", data_from_json.keys())

with open('json.txt') as jf:
    json_txt = json.load(jf)
    print("json from txt =>", json_txt)
    for k, v in json_txt.items():
        print(k,'->', v)
        if isinstance(v, list):
            for i in v:
                if isinstance(i, dict):
                    for _k, _v in i.items():
                        print('    ', _k, " : ", _v)





