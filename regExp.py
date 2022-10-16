#You are given a string N.
#Your task is to verify that N  is a floating point number.

#Code
import re

T = int(input())
for i in range(T):
    N = input()
    res  = re.search('^[+-]?[0-9]*[\.]?[0-9]+$', N)
    if res :
        print('True')
    else:
        print('False')
