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













