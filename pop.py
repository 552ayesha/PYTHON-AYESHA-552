#random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)
"""
The popped element is: 2
The dictionary is: {'orange': 3, 'grapes': 4}
"""



#2 program
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element = sales.pop('guava')
"""
KeyError: 'guava'
"""
