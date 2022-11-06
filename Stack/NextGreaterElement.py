"""
You are required to implement the next_greater_element() function. 
For each element i in a list, the function finds the first element to its 
right which is greater than element i. If for any element such a value does not exist, 
the answer is -1.
"""

from Stack import MyStack

"""
Come in reverse order of iteration and as push values into stack. 
If new val is smaller than top value in stack, then put top value in stack in its place, else pop it
Time Complexity: O(n) since we only go through lst once i.e. the for loop
"""


def next_greater_element(lst):
    my_stack = MyStack()
    to_return = [-1] * len(lst)
    for val in range(len(lst) - 1, -1, -1):
        if not my_stack.is_empty():
            while not my_stack.is_empty() and my_stack.peek() <= lst[val]:
                my_stack.pop()
        if not my_stack.is_empty():
            to_return[val] = my_stack.peek()
        my_stack.push(lst[val])
    return to_return


print(next_greater_element([4, 6, 3, 2, 8, 1]))
