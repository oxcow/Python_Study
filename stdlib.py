# -*- coding: utf-8 -*-


# https://docs.python.org/zh-cn/3.7/tutorial/stdlib.html

# 10. 标准库简介

## 10.1. 操作系统接口
print('-' * 20, '10.1. 操作系统接口', '-' * 20)


print('''1. os 模块提供了许多与操作系统交互的函数:''')
print('-' * 80)

import os

cur_path = os.getcwd()
print(cur_path) # return the current working directory

print(os.chdir(cur_path))

print(os.getcwd())

print(os.system('mkdir today'))

print(os.system('rm -r today'))


print(dir(os))
# help(os)


print('''2. 对于日常文件和目录管理任务， shutil 模块提供了更易于使用的更高级别的接口:''')
print('-' * 80)

import shutil

copy_result = shutil.copyfile('json.txt', 'json.json')
print('copy json.txt -> json.json?', copy_result)

os.system('rm -r json.json')

## 10.2. 文件通配符
print('-' * 20, '10.2. 文件通配符', '-' * 20)


print('''3. glob 模块提供了一个在目录中使用通配符搜索创建文件列表的函数:''')
print('-' * 80)

import glob

py_files = glob.glob('*.py')
print('current directory python files:', py_files)

## 10.3. 命令行参数
print('-' * 20, '10.3. 命令行参数', '-' * 20)


print('''4. 通用实用程序脚本通常需要处理命令行参数。这些参数作为列表存储在 sys 模块的 argv 属性中:''')
print('-' * 80)

import sys

print(sys.argv)


print('''5. argparse 模块提供了一种处理命令行参数的机制。 它应该总是优先于直接手工处理 sys.argv:''')
print('-' * 80)

import argparse
from getpass import getuser

parser = argparse.ArgumentParser(description='An argparse example.')
parser.add_argument('name', nargs='?', default=getuser(), help='The name of someone to greet.')
parser.add_argument('--verbose', '-v', action='count')
args = parser.parse_args()
greeting = ["Hi", "Hello", "Greetings! its very nice to meet you"][args.verbose % 3]

print(f'{greeting}, {args.name}')

if not args.verbose:
    print('Try running this again with multiple "-v" flags!')

## 10.4. 错误输出重定向和程序终止
print('-' * 20, '10.4. 错误输出重定向和程序终止', '-' * 20)

print('''
    sys 模块还具有 stdin ， stdout 和 stderr 的属性。
    后者对于发出警告和错误消息非常有用，即使在 stdout 被重定向后也可以看到它们:
    ''')

sys.stderr.write('Warning, log file not found starting a new one\n')

print('\n终止脚本的最直接方法是使用 sys.exit() 。\n')


## 10.5. 字符串模式匹配
print('-' * 20, '10.5. 字符串模式匹配', '-' * 20)

print('''6. re 模块为高级字符串处理提供正则表达式工具。:''')
print('-' * 80)

import re

find_result = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

print('find result =>', find_result)

sub_result = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print('sub result =>', sub_result)

# 当只需要简单的功能时，首选字符串方法因为它们更容易阅读和调试:
print('tea for too'.replace('too', 'two'))


## 10.6. 数学
print('-' * 20, '10.6. 数学', '-' * 20)

print('''7. math 模块提供对浮点数学的底层C库函数的访问:''')
print('-' * 80)

import math
print('math.cos(math.pi / 4) =', math.cos(math.pi / 4))
print('math.log(1024, 2) =', math.log(1024, 2))


print('''8. random 模块提供了进行随机选择的工具:''')
print('-' * 80)

import random

for x in range(3):

    random_choice = random.choice(['apple', 'pear', 'banana'])
    print('random choice (apple, pear, banana)?', random_choice)

    random_sample = random.sample(range(100), 10) # sampling without replacement
    print('random.sample(range(100), 10) =>', random_sample)


print('''9. statistics 模块计算数值数据的基本统计属性（均值，中位数，方差等）:''')
print('-' * 80)

import statistics

data = [2.75, 1.75, 0.25, 0.5, 1.25, 3.5]

print('data:', data)

mean = statistics.mean(data)
print('statistics mean =>', mean)

median = statistics.median(data)
print('statistics median =>', median)

variance = statistics.variance(data)
print('statistics variance =>', variance)


## 10.7. 互联网访问
print('-' * 20, '10.7. 互联网访问', '-' * 20)

print('''
    有许多模块可用于访问互联网和处理互联网协议。
    其中两个最简单的 urllib.request 用于从URL检索数据，
    以及 smtplib 用于发送邮件:
    ''')

from urllib.request import urlopen

'''
with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
    for line in response:
        line = line.decode('utf-8') # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line: # look for Eastern Time
            print(line)
'''

with urlopen('http://www.baidu.com') as baidu:
    for line in baidu:
        print(str(line))
        break;


'''
# 需要在localhost上运行的邮件服务器

import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    """To: jcaesar@example.org
    From: soothsayer@example.org

    Beware the Ides of March.
    """)
server.quit()
'''


## 10.8. 日期和时间
print('-' * 20, '10.8. 日期和时间', '-' * 20)

print('''
    datetime 模块提供了以简单和复杂的方式操作日期和时间的类。
    虽然支持日期和时间算法，但实现的重点是有效的成员提取以进行输出格式化和操作。
    该模块还支持可感知时区的对象。
    ''')

from datetime import date

now = date.today()
print('now: ', now)

dt = date(2019, 12, 12)
print('dt:', dt)

print('now.format:', now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'))

birthday = date(1985, 4, 20)
age = now - birthday
print('age days:', int(age.days / 365))


## 10.9. 数据压缩
print('-' * 20, '10.9. 数据压缩', '-' * 20)

print('''
    常见的数据存档和压缩格式由模块直接支持，
    包括：zlib, gzip, bz2, lzma, zipfile 和 tarfile。:
    ''')

import zlib

s = b'witch which has which withches wrist watch'
print('befor compress:', s, ', length:', len(s))

t = zlib.compress(s)
print('after compress:', t, ', length:', len(t))

print('decompress:', t, '.Result:', zlib.decompress(t))

print('zlib crs32 "', s, '", output:', zlib.crc32(s))


## 10.10. 性能测量
print('-' * 20, '10.10. 性能测量', '-' * 20)

print('''
    一些Python用户对了解同一问题的不同方法的相对性能产生了浓厚的兴趣。 
    Python提供了一种可以立即回答这些问题的测量工具。
        例如，元组封包和拆包功能相比传统的交换参数可能更具吸引力。
        timeit 模块可以快速演示在运行效率方面一定的优势:

    与 timeit 的精细粒度级别相反， profile 和 pstats 模块提供了用于在较大的代码块中识别时间关键部分的工具。
    ''')

from timeit import Timer

time = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print("Timer('t=a; a=b; b=t', 'a=1; b=2').timeit() =>", time)

time = Timer('a,b = b,a', 'a=1; b=2').timeit()
print("Timer('a,b = b,a', 'a=1; b=2').timeit() =>", time)


# 10.11. 质量控制
print('-' * 20, '10.11. 质量控制', '-' * 20)

print('''
    doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试
    ''')

def average(values):
    """Computes the arithmetic mean of a list of numbers.
        
    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest

doctest.testmod() # 针对文档中的 >>> 起作用

print('''
    unittest 模块不像 doctest 模块那样易于使用，但它允许在一个单独的文件中维护更全面的测试集:
    ''')

import unittest

class TestStatisticalFunction(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
'''
# 下面的代码放在最后，否则其后的代码不会被执行
unittest.main() # Calling from the command line invokes all tests
'''

# 10.12. 自带电池
print('-' * 20, '10.12. 自带电池', '-' * 20)

print('''
    Python有“自带电池”的理念。通过其包的复杂和强大功能可以最好地看到这一点。例如:

        xmlrpc.client 和 xmlrpc.server 模块使得实现远程过程调用变得小菜一碟。尽管存在于模块名称中，但不需要直接了解或处理XML。

        email 包是一个用于管理电子邮件的库，包括MIME和其他符合 RFC 2822 规范的邮件文档。与 smtplib 和 poplib 不同（它们实际上做的是发送和接收消息），电子邮件包提供完整的工具集，用于构建或解码复杂的消息结构（包括附件）以及实现互联网编码和标头协议。

        json 包为解析这种流行的数据交换格式提供了强大的支持。 csv 模块支持以逗号分隔值格式直接读取和写入文件，这种格式通常为数据库和电子表格所支持。 XML 处理由 xml.etree.ElementTree ， xml.dom 和 xml.sax 包支持。这些模块和软件包共同大大简化了 Python 应用程序和其他工具之间的数据交换。

        sqlite3 模块是 SQLite 数据库库的包装器，提供了一个可以使用稍微非标准的 SQL 语法更新和访问的持久数据库。

        国际化由许多模块支持，包括 gettext ， locale ，以及 codecs 包。
    ''')



unittest.main() # Calling from the command line invokes all tests