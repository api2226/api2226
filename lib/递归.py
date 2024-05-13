#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2024/5/8 14:10
# Author : xiaowei
# @File : 递归.py
# @Software : PyCharm

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)

print(sum(5))

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))

def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return reverse_string(s[1:])+s[0]


print(reverse_string("hello"))

def is_palindrome(s):
    if len(s)==0 or len(s)==1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])


print(is_palindrome("racecar"))



