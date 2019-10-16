# -*- coding: utf-8 -*-

# https://docs.python.org/zh-cn/3.7/tutorial/modules.html

# 6. 模块
print("-" * 20, '6. 模块', "-" * 20)

import fibo

fibo.fib(1000)

result = fibo.fib2(100)

print(result)

print('fibo moules name:', fibo.__name__)

fib = fibo.fib

fib(400)

## 6.1. 更多有关模块的信息
print("-" * 20, '6.1. 更多有关模块的信息', "-" * 20)

from fibo import fib, fib2

fib(100)
print(fib2(100))

import fibo as fib
fib.fib(500)

from fibo import fib as fibonacci
fibonacci(500)

### 6.1.1. 以脚本的方式执行模块
print("-" * 20, '6.1.1. 以脚本的方式执行模块', "-" * 20)

# see the fibo.py if condition part

## 6.2. 标准模块
print("-" * 20, '6.2. 标准模块', "-" * 20)

import sys
print('sys.path:', sys.path)

## 6.3. dir() 函数
print("-" * 20, '6.3. dir() 函数', "-" * 20)

import fibo
print(dir(fibo))

import builtins
print(dir(builtins))


## 6.4. 包
print("-" * 20, '6.4. 包', "-" * 20)
