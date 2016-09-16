'''
Created on Feb 2, 2016

@author: bosco
'''
def uniq(input):
    output = []
    for x in input:
        if x not in output:
            output.append(x)
    return output

# def remove_duplicates():
#     t = ['a', 'b', 'c', 'd']
#     t2 = ['a', 'c', 'd']
#     for t in t2:
#         t.append(t.remove())
#     return t\
from collections import OrderedDict 
print OrderedDict.fromkeys(['a', 'b', 'c', 'c', 'a', 'd', 'p', 'p']).keys()
