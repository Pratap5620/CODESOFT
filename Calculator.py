# -*- coding: utf-8 -*-
"""
Created on Mon Sep  12 15:07:30 2023

@author: om123
"""



def calculator():
    # Creating input for user to enter number

    inp1 = float(input("Enter first number: "))

    inp2 = float(input("Enter second number: "))
    print("you entered :", inp1,"; ",inp2)

    # Defining Operations

    op = input("Enter operation (+,-,*,/,**) to be performed: ")

    # Defining conditionality of an operation
    if op == "+":
        res = inp1 + inp2
    elif op == "-":
        res = inp1 - inp2
    elif op == "*":
        res = inp1 * inp2
    elif op == "/":
        res = inp1 / inp2
    else:
        res = inp1 ** inp2

    return res

xh = calculator()
print(xh)
