# -*- coding: utf-8 -*-

# https://docs.python.org/zh-cn/3.7/tutorial/classes.html

# 9. 类

## 9.1. 名称和对象
print('-' * 20, '9.1. 名称和对象', '-' * 20)

## 9.2. Python 作用域和命名空间
print('-' * 20, '9.2. Python 作用域和命名空间', '-' * 20)


## 9.2.1. 作用域和命名空间示例
print('-' * 20, '9.2.1. 作用域和命名空间示例', '-' * 20)
print('''
global 语句可被用来表明特定变量生存于全局作用域并且应当在其中被重新绑定；
nonlocal 语句表明特定变量生存于外层作用域中并且应当在其中被重新绑定。
    ''')

def scope_test():
    def do_local():
        spam = 'local spam'

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal spam'

    def do_global():
        global spam
        spam = 'global spam'

    spam = 'test spam'

    do_local()
    print('After local assigment:', spam)

    do_nonlocal()
    print("After nonlocal assigment:", spam)

    do_global()
    print("After global assigment:", spam)

    do_local()
    print("do local:", spam)

scope_test()
print('In global scope:', spam)

## 9.3. 初探类
### 9.3.1. 类定义语法
print('-' * 20, '9.3.1. 类定义语法', '-' * 20)


class MyClass:
    '''A simple example class'''
    i = 12345

    def f(self):
        return 'hello world'

print(MyClass.i, MyClass.f)

x = MyClass()
print(x.i, x.f(), MyClass.f(x))
'''
# 成立的
x = MyClass
print(x().i, x().f(), MyClass.f(x()))
'''

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

### 9.3.4. 方法对象
print('-' * 20, '9.3.4. 方法对象', '-' * 20)

print(
'''\
    方法的特殊之处就在于实例对象会作为函数的第一个参数被传入
    x = MyClass()
    x.f() === MyClass.f(x)
''')

### 9.3.5. 类和实例变量
print('-' * 20, '9.3.5. 类和实例变量', '-' * 20)

class Dog:

    kind = 'canine'

    def __init__(self, name):
        self.name = name

d = Dog('Fido')
e = Dog('Buddy')

print('d.kind:', d.kind)
print('e.kind:', e.kind)
print('d.name:', d.name)
print('e.name:', e.name)

class Dog:

    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')

print('d.tricks', d.tricks)

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def out(self):
        print(self.abc)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print('d.tricks', d.tricks)
print('e.tricks', e.tricks)

print('-' * 40)

Dog.abc = 1
print(Dog.abc, 'e.abc:', e.abc,'d.abc:', d.abc) # output: 1 1 1
print('-' * 40)

Dog.out(e) # 1
Dog.out(d) # 1
e.out() # 1
d.out() # 1

## 9.4. 补充说明
print('-' * 20, '9.4. 补充说明', '-' * 20)

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        # print('invoke add')
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

    def staticMethod():
        print('static method')

bag = Bag()
bag.add('x')
bag.addtwice('x')
print('bag.data =>', bag.data)

Bag.staticMethod()
# bag.staticMethod() # TypeError: staticMethod() takes 0 positional arguments but 1 was given

## 9.5. 继承
print('-' * 20, '9.5. 继承', '-' * 20)

print('''
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>


Python有两个内置函数可被用于继承机制：

isinstance()
    isinstance(obj, int)

issubclass()
    issubclass(bool, int) => True
    issubclass(float, int) => False

''')


### 9.5.1. 多重继承
print('-' * 20, '9.5.1. 多重继承', '-' * 20)

print('''
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
''')


## 9.6. 私有变量
print('-' * 20, '9.6. 私有变量', '-' * 20)

print('''
那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。
但是，大多数 Python 代码都遵循这样一个约定：
    
    带有一个下划线的名称 (例如 _spam) 应该被当作是 API 的非仅供部分 (无论它是函数、方法或是数据成员)。 

这应当被视为一个实现细节，可能不经通知即加以改变。

''')

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

## 9.7. 杂项说明
print('-' * 20, '9.7. 杂项说明', '-' * 20)

## 9.8. 迭代器
print('-' * 20, '9.8. 迭代器', '-' * 20)

for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one':1, 'two': 2}:
    print(key)

for char in '123':
    print(char)

with open('readme.md') as f:
    for line in f:
        print(line)

s = 'abc'
it = iter(s)
print('iter(s) =>', it)

try:
    print('next(it) =>', next(it))
    print('next(it) =>', next(it))
    print('next(it) =>', next(it))
    print('next(it) =>', next(it)) # exception
except StopIteration:
    print('StopIteration')

class Reverse:
    '''Iterator for looping over a sequence backwards.'''
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char)


## 9.9. 生成器
print('-' * 20, '9.9. 生成器', '-' * 20)

def reverse(data):
    # print(list(range(len(data)-1, -1, -1)))
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)


## 9.10. 生成器表达式
print('-' * 20, '9.10. 生成器表达式', '-' * 20)

sums = sum(i*i for i in range(10))
print('sum(i*i for i in range(10)) => ', sums)

xvec = [10, 20, 30]
yvec = [7, 5, 3]
sums = sum(x*y for x,y in zip(xvec, yvec))
print('sum(x*y for x,y in zip(xvec, yvec)) => ', sums)

from math import pi, sin

sin_table = {x: sin(x*pi/180) for x in range(0, 91)}

print('sin_table =>', sin_table)

# unique_words = set(word for line in page for word in line.split())

# valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'glof'

print(list(data[i] for i in range(len(data)-1, -1, -1)))






