#You are given a string S.
#Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.
#Code

import re

S = input()
for i in range(len(S)):
    text = S[i:len(S)]
    c = re.match(r'([a-zA-Z0-9]?)([a-zA-Z0-9]?)',text)
    if (c.group(1) == c.group(2)) :
        print(c.group(1))
        break
