# -*- coding: utf-8 -*-

# https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html

# 4.1. if 语句

x = int(input('Please enter an integer:'))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print('zero'.title())
elif x == 1:
    print('Single')
else:
    print('More')


# 4.2. for 语句

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)

print(words)

# 4.3. range() 函数

for i in range(5):
    print(i, end=',')
print()

for i in range(5, 10, 2):
    print(i, end = ',')
print()

a = ['Marry', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 4.4. break 和 continue 语句，以及循环中的 else 子句

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# 4.5. pass 语句

def initlog(*args):
    print('TODO: Remeber to implement this!')
    pass # TODO: Remeber to implement this!

initlog()

# 4.6. 定义函数

def fib(n):    # write Fibonacci series up to n
    '''docstring: Print a Fibonacci series up to n.'''
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print(fib, fib(0))
fib(2000)
f = fib
f(100)

def fib2(n):    # return Fibonacci series up to n
    '''Return a list containing the Fibonacci series up to n.'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)
print("Fib(100) =>", f100)

# 4.7. 函数定义的更多形式

## 4.7.1. 参数默认值

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5

def f(arg=i):
    print(arg)

i = 6
f() # print 5 not 6

# 重要警告： 默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要

def f(a, L=[]):
    L.append(a)
    return L

print(f(1)) # [1]
print(f(2)) # [1,2]
print(f(3)) # [1,2,3]

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1)) #[1]
print(f(2)) #[2]
print(f(3)) #[3]

## 4.7.2 关键字参数

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print('if you put', voltage, 'volts through it.')
    print('-- Lovely plumage, the', type)
    print("-- It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOOM')
parrot(action='VOOOOOM', voltage=1000000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", 
    "It's very runny, sir.", 
    "It's really very, VERY runny, sir.",
    shopkeeper="Michael Plain",
    client="John Cleese",
    sketch="cheese shop sketch".title())

## 4.7.3 任意的参数列表

def concat(*args, sep="/"):
    return sep.join(args)

print(concat('earth', 'mars', 'venus'))
print(concat('earth', 'mars', 'venus', sep='.'))

## 4.7.4. 解包参数列表

print(list(range(3, 6)))
args = [3, 6]
print(list(range(*args)))

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", 'state': "bleedin' demised", 'action': 'VOOM'}
parrot(**d)

## 4.7.5. Lambda 表达式

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4,'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

## 4.7.6. 文档字符串

def my_function():
    '''Do nothing, but document it.

    No, really, it doesn't do anything.
    '''

    pass

print(my_function.__doc__)

## 4.7.7. 函数标注

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

# 4.8. 小插曲：编码风格

description = '''
几个要点：

1. 使用4个空格缩进，不要使用制表符。

2. 4个空格是一个在小缩进（允许更大的嵌套深度）和大缩进（更容易阅读）的一种很好的折中方案。制表符会引入混乱，最好不要使用它。

3. 换行，使一行不超过79个字符。

这有助于使用小型显示器的用户，并且可以在较大的显示器上并排放置多个代码文件。

4. 使用空行分隔函数和类，以及函数内的较大的代码块。

5. 如果可能，把注释放到单独的一行。

6. 使用文档字符串。

7. 在运算符前后和逗号后使用空格，但不能直接在括号内使用： a = f(1, 2) + g(3, 4)。

8. 以一致的规则为你的类和函数命名；按照惯例应使用 UpperCamelCase 来命名类，而以 lowercase_with_underscores 来命名函数和方法。 始终应使用 self 来命名第一个方法参数 (有关类和方法的更多信息请参阅 初探类)。

9. 如果你的代码旨在用于国际环境，请不要使用花哨的编码。Python 默认的 UTF-8 或者纯 ASCII 在任何情况下都能有最好的表现。

10. 同样，哪怕只有很小的可能，遇到说不同语言的人阅读或维护代码，也不要在标识符中使用非ASCII字符。
'''












