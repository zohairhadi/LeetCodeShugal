"""
You have to implement the MinStack class which will have a min() function.
Whenever min() is called, the minimum value of the stack is returned in O(1) time.
The element is not popped from the stack. Its value is simply returned.
"""

"""
COMMENTS: No duplicates allowed in this solution, since we're using dicts, adding duplicates
we'll eventually need to traverse making it non-constant fetch.
"""

# imports here


# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()




from Stack import MyStack
class MinStack():
    # Constructor
    def __init__(self):
        self.min_stack = MyStack()
        self.main_stack = MyStack()

    # Removes and returns value from min_stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    # Pushes values into min_stack
    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > value:
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())

    # Returns minimum value from newStack in O(1) Time
    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()
        return None


stack = MinStack()
stack.push(1)
stack.push(3)
stack.push(-11)
stack.push(47)
print(stack.min())
