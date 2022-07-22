def _find_(p, f):
    l = os.listdir(p)
    for i in l:
        if i == f:
            print(os.path.abspath(p) + '/' + f)
        if os.path.isdir(p + '/' + i):
            _find_(p + '/' + i, f)

def _tree_(p, large):
    l = os.listdir(p)
    for i in l:
        print(large + i)
        if os.path.isdir(p + '/' + i):
            _tree_(p + '/' + i, large + '    ')

import os
p=input()
f=input()
large = '    '
_find_(p, f)
_tree_(p, large)
