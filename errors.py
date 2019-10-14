# -*- coding: utf-8 -*-

# https://docs.python.org/zh-cn/3.7/tutorial/errors.html

# 8. 错误和异常

## 8.1. 语法错误
print('-' * 20, '8.1. 语法错误', '-' * 20)

# while True print("Hello world")

# 10 * (1/0)

# 4 + spam * 3

# '2' + 2


while True:
    try:
        x = int(input('Please enter a number: '))
        break;
    except ValueError:
        print('Oops! That was no valid number. Try again...')



class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')


import sys

try:
    with open('readme1.md') as f:
        s = f.readline()
        i = int(s.strip())
except OSError as err:
    print('OS error: {0}'.format(err))
except ValueError:
    print('Could not convert data to an integer.')
except:
    print('Unexpected error:', sys.exc_info()[0])
    raise

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print('Error type?', type(inst))    # the exception instance
    print('Error args:', inst.args)    # argments stored in .args
    print('Error:', inst)    # __str__ allows args to be printed directly,
                   # but may be overridden in exception subclasses uppack args

    x, y = inst.args
    print('x =', x)
    print('y =', y)


def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


## 8.4. 抛出异常
print('-' * 20, '8.4. 抛出异常', '-' * 20)

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    # raise

## 8.5. 用户自定义异常
print('-' * 20, '8.5. 用户自定义异常', '-' * 20)


class Error(Exception):
    '''Base class for exceptions in this module.'''
    pass

class InputError(Error):
    """Exception raised for errors in the input.
    
    Attributes:
        expression -- input expression in which the errro ocurred
        message -- explanation of the error
    """

    def __init_(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts as state transition that's not allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the sepcific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

## 8.6. 定义清理操作
print('-' * 20, '8.6. 定义清理操作', '-' * 20)

try:
    raise KeyboardInterrupt
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    print('Goodbye, world!')

def bool_return():
    try:
        return True
    finally:
        return False

print('bool return?', bool_return())


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero!')
    except:
        print('Other exception!', sys.exc_info()[0])
    else:
        print('result is', result)
    finally:
        print('executing finally clause')

divide(2, 1)
print('-' * 60)

divide(2, 0)
print('-' * 60)

divide('2', '1')
print('-' * 60)


## 8.7. 预定义的清理操作
print('-' * 20, '8.7. 预定义的清理操作', '-' * 20)

'''
for line in open('readme.md'):
    print(line, end="")
'''

with open('readme.md') as f:
    for line in f:
        print(line, end="")

print()