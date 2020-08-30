"""
@file: aiml_combo.py
@author: Sureshkumar Chandran
@purpose: to print the string combinations in loop
"""

from random import randrange

# Define the List of words or strings
sS2 = ['artificial', 'intelligence', 'machine', 'learning']
sS1 = ['a', 'i', 'm', 'l']
sS3 = ['This ', 'That ', 'It ']

r = 0
p = 0

# Carry over the Cross-join
sGen = ((i, j, k, l) for i in sS1 for j in sS1 for k in sS1 for l in sS1)

# Filter-out the over-lap and print the possibilities result
print('artificial.intelligence.machine.learning')
for u, v, w, x in sGen:
    if (u != v) and (u != w) and (u != x) and \
       (v != w) and (v != x) and \
       (w != v) and (w != x) and \
       (x != u): 
        # print(u, v, w, x)
        p += 1
        r = randrange(0,3)
        # print(p, '==> ', sS3[r] + 'is ' + u + '.'  + v + '.' + w + '.' + x + '.')
        print(p, '==> ', u + '.'  + v + '.' + w + '.' + x + '.')

# End of Script
        