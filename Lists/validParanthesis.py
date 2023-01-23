"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

"""
Cause we looping over whole array once
Time Complexity: O(n)
"""


def my_func(s):
    # Write your code here
    circular = []
    para_dict = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in para_dict:
            top = circular.pop() if circular else '#'
            if top != para_dict[char]:
                return False
        else:
            circular.append(char)

    return not circular


def main():
    print(my_func("]"))


if __name__ == '__main__':
    main()
