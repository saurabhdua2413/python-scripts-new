#!/usr/bin/python
lists=['a','b','c',4]
lists.extend([4,5,6])
print lists
rev=lists[::-1]
print rev
lists[3]="biology"
print lists
new_lists=['a','b','c',4]
del new_lists[3]
print new_lists
