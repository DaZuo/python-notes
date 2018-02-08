"""Test"""

# 操作符

A = 8 / 5
print(A) # 输出 1.6

B = 17 // 3
print(B) # 输出 5

C = 17 % 3
print(C) # 输出 2

D = 5 ** 2
print(D) # 输出25

# 字符串

STR_1 = "I'm a coder!"
STR_2 = 'I\'m a coder!'
print(STR_1) # 输出 I'm a coder!
print(STR_2) # 输出 I'm a coder!

# 输出
# C:\some
# ame
print('C:\\some\name')
# 输出
# C:\some\name
print(r'C:\some\name')

# 第一行，没有换行
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# 第一行，有换行
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 输出 unununium
print(3 * 'un' + 'ium')
# 输出 unununium
print('un' * 3 + 'ium')

# 输出 Python
print('Py'    'thon')

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
