
from Stack import MyStack
import operator

"""
Using operator lib to convert char operators using a look up table
"""


def evaluate_post_fix_lookup(exp):
    my_stack = MyStack()
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ops = {"+": operator.add, "-": operator.sub,
           "*": operator.mul, "/": operator.floordiv}
    for char in exp:
        if char in nums:
            my_stack.push(char)
        else:
            if my_stack.is_empty():
                continue
            v1 = my_stack.pop()
            v2 = my_stack.pop()
            my_stack.push(ops[char](int(v2), int(v1)))
    return my_stack.pop()


"""
Using str eval ftn to convert string to an expression
Time Complexity: O(n)
"""


def evaluate_post_fix_str(exp):
    my_stack = MyStack()
    for char in exp:
        if char.isdigit():
            my_stack.push(char)
        else:
            if my_stack.is_empty():
                continue
            v1 = my_stack.pop()
            v2 = my_stack.pop()
            my_stack.push(str(eval(v2+char+v1)))
    return my_stack.pop()


print(evaluate_post_fix_str("921*-8-4+"))
