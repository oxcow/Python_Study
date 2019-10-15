# -*- coding: utf-8 -*-

# https://docs.python.org/zh-cn/3.7/tutorial/stdlib2.html

# 11. 标准库简介 —— 第二部分

## 11.1. 格式化输出
print('-' * 20, '11.1. 格式化输出', '-' * 20)

print('''
    reprlib 模块提供了一个定制化版本的 repr() 函数，用于缩略显示大型或深层嵌套的容器对象:
    ''')

import reprlib

long_set = set('supercalifragilistcexpialidocious')
simple_display = reprlib.repr(long_set)

print(long_set)
print(simple_display)


print('''
    pprint 模块提供了更加复杂的打印控制，其输出的内置对象和用户自定义对象能够被解释器直接读取
    ''')

import pprint

t = [[[['blank', 'cyan'], 'white', ['green', 'red']],[['magenta', 'yellow'], 'blue']]]

print(t)

pprint.pprint(t, width=30)


print('''
    textwrap 模块能够格式化文本段落，以适应给定的屏幕宽度:
    ''')

import textwrap

doc = """The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."""

print(doc, '\n')
print(textwrap.fill(doc, width=40))


print('''
    locale 模块处理与特定地域文化相关的数据格式。
    locale 模块的 format 函数包含一个 grouping 属性，可直接将数字格式化为带有组分隔符的样式:
    ''')

import locale

# locale.setlocale(locale.LC_ALL, 'English_United States.1252')

conv = locale.localeconv()
x = 1234567.8
print(locale.format_string('%d', x, grouping=True))

print(locale.format_string("%s%.*f", (conv['currency_symbol'],
    conv['frac_digits'], x), grouping=True))


## 11.2. 模板
print('-' * 20, '11.2. 模板', '-' * 20)


print('''
    string 模块包含一个通用的 Template 类，具有适用于最终用户的简化语法。
    ''')

from string import Template

t = Template('${village}folk send $$10 to $cause.')
t_str = t.substitute(village='Nottingham', cause='the ditch fund')

print("Template:", t)
print(t_str)


t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')

try:
    t.substitute(d)
except KeyError as err:
    print('KeyError', err)

print(t.safe_substitute(d))



import time, os.path

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')

for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


## 11.3. 使用二进制数据记录格式
print('-' * 20, '11.3. 使用二进制数据记录格式', '-' * 20)

print('''
    struct 模块提供了 pack() 和 unpack() 函数，用于处理不定长度的二进制记录格式。
    ''')

import struct

with open('json.txt.zip', 'rb') as f:
    data = f.read()

start = 0

try:
    for i in range(3):                      # show the first 3 file headers
        start += 14
        fields = struct.unpack('<IIIHH', data[start:start+16])
        crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

        start += 16
        filename = data[start:start+filenamesize]
        start += filenamesize
        extra = data[start:start+extra_size]
        print(filename, hex(crc32), comp_size, uncomp_size)

        start += extra_size + comp_size     # skip to the next header

except Exception as err:
    print(err)


# 11.4. 多线程
print('-' * 20, '11.4. 多线程', '-' * 20)

import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished brackground zip of:', self.infile)

brackground = AsyncZip('json.txt', 'json.zip')
brackground.start()
print('The main program continues to run in foreground.')

brackground.join()
print('Main program waited unitl background was done.')

import os

os.system('rm json.zip')

print('''
    实现多任务协作的首选方法是将对资源的所有请求集中到一个线程中，然后使用 queue 模块向该线程供应来自其他线程的请求。
    应用程序使用 Queue 对象进行线程间通信和协调，更易于设计，更易读，更可靠。
    ''')

# 11.5. 日志记录
print('-' * 20, '11.5. 日志记录', '-' * 20)

print('''
    logging 模块提供功能齐全且灵活的日志记录系统。
    在最简单的情况下，日志消息被发送到文件或 sys.stderr
    ''')

import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical("Critical error -- shutting down")

# 11.6. 弱引用
print('-' * 20, '11.6. 弱引用', '-' * 20)

import weakref, gc

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10) # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a    # does not create a reference

print(d['primary'])    # fetch the object if it is still alive

del a    # remove the one reference

print(gc.collect())    # run garbage collection right away

try:
    print(d['primary'])    # entry was automatically removed
except KeyError as err:
    print(err)


# 11.7. 用于操作列表的工具
print('-' * 20, '11.7. 用于操作列表的工具', '-' * 20)

print('''
    array 模块提供了一种 array() 对象，它类似于列表，但只能存储类型一致的数据且存储密集更高。
    ''')

'''
下面的例子演示了一个以两个字节为存储单元的无符号二进制数值的数组 (类型码为 "H")，
而对于普通列表来说，每个条目存储为标准 Python 的 int 对象通常要占用16 个字节:
'''

from array import array

a = array('H', [4000, 10, 700, 22222])
print(a, 'sum(a) =', sum(a), ', a[1:3] =', a[1:3])


print('''
    collections 模块提供了一种 deque() 对象，它类似于列表，但从左端添加和弹出的速度较快，而在中间查找的速度较慢。 
    此种对象适用于实现队列和广度优先树搜索:
    ''')

from collections import deque

d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print('deque: ', d)
print('deque: ', d, ', d.popleft() =', d.popleft())

'''
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
'''

print('''
    bisect 模块具有用于操作排序列表的函数:
    ''')

import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))

print(scores)

print('''
    heapq 模块提供了基于常规列表来实现堆的函数.
    最小值的条目总是保持在位置零。 
    这对于需要重复访问最小元素而不希望运行完整列表排序的应用来说非常有用:
    ''')

from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print('data:', data)
heapify(data)    # rearrange the list into heap order
print('heapify data:', data)
heappush(data, -5)    # add a new entry
print('heap push data:', data)

small = [heappop(data) for i in range(3)]    # fetch the three samllest entries
print(small)

# 11.8. 十进制浮点运算
print('-' * 20, '11.8. 十进制浮点运算', '-' * 20)

print('''
decimal 模块提供了一种 Decimal 数据类型用于十进制浮点运算。 
相比内置的 float 二进制浮点实现，该类特别适用于
    1. 财务应用和其他需要精确十进制表示的用途，
    2. 控制精度，
    3. 控制四舍五入以满足法律或监管要求，
    4. 跟踪有效小数位，或
    5. 用户期望结果与手工完成的计算相匹配的应用程序。
    ''')

from decimal import *

n = round(Decimal('0.70') * Decimal('1.05'), 2)
print("round(Decimal('0.70') * Decimal('1.05'), 2) =", n)

n = round(.70 * 1.05, 2)
print("round(.70 * 1.05, 2) =", n)


z = Decimal('1.00') % Decimal('.10')
print("Decimal('1.00') % Decimal('.10') =", z)

print('1.00 % 0.10 =', 1.00 % 0.10)

s = sum([Decimal('0.1')] * 10) == Decimal('1.0')
print("sum([Decimal('0.1')] * 10) == Decimal('1.0') ?", s)

getcontext().prec = 36    # 设置精度
print('Decimal(1) / Decimal(7) =', Decimal(1) / Decimal(7))