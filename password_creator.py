#!/usr/bin/python
# thin code help you to create strong password for your account on any where
# you can make it very very much strog when edit "size" value up.like "size =24" :D 
# hrouhi.kh@gmail.com

import sys, string, random

size = 12

def pass_creator():
  print ''.join([random.choice('abcdefghijklmnopqrstuvwxyz'
					+ 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
					+ '0123456789'
					+ '+-*@#%=?!_;./()') 
	for i in range(size)])
pass_creator()
