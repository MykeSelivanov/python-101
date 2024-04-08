# DeMorgan's Law
# not (x and y) == (not x) or (not y)
# not (x or y) == (not x) and (not y)

# Example
# not (w and z or (not w)) => 
# (not(w and z)) and (not(not w)) =>
# ((not w) or (not z)) and w =>

# Truth table
'''
W Z
---
F F -> True or True and False -> True or False -> True
T F -> False or True and True -> False or True -> True
F T -> True or False and False -> True or False -> True
T T -> False or False and True -> False or False -> False
'''
