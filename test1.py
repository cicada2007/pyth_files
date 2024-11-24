#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:52:21 2024

@author: ak2007
"""
print("---------------CALCULATOR---------------")
x=int(input("Enter first no: "))
y=int(input("Enter second no: "))
print("PRESS 1 FOR ADDITION")
print("PRESS 2 FOR SUBTRACTION")
print("PRESS 3 FOR MULTIPICATION")
print("PRESS 4 FOR DIVISION")
print("PRESS 5 FOR ALL ARITHMETIC OPERATIONS")
op=int(input("Enter Corres. No. for the operation: "))
if op==1:
    print("Addition: ",x+y)
elif op==2:
    print("Subtraction: ",x-y)
elif op==3:
    print("Multiplication:", x*y)
elif op==4:
    if y==0:
        print("INVALID OPERATION")
    else:
        print("Division:", x/y)
elif op==5:
    print("Addition: ",x+y)
    print("Subtraction: ",x-y)
    print("Multiplication:", x*y)
    if y==0:
        print("INVALID OPERATION")
    else:
        print("Division:", x/y)
else:
    print("WRONG OPERATION NO.")
    