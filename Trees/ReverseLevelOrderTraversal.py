"""
Given the root of a binary tree, display its level-order traversal.
"""
from BinaryTree import BinaryTree
import queue
# from mypackage.mymodule import as_int

# imports here

"""
why is there here?
Time Complexity: O()
"""


def traverse(root, q):
    stack = []
    while q.queue.len > 0:
        cur_node = q.get()
        stack.append(cur_node.data)

        if cur_node.left is not None:
            q.put(cur_node.left)
        if cur_node.right is not None:
            q.put(cur_node.right)

    while stack:
        print(stack.pop())


def my_func(root):
    q = queue.Queue()
    q.put(root)
    traverse(root, q)


def main():
    # Creating a binary tree
    input1 = [100, 50, 200, 25, 75, 350]
    tree1 = BinaryTree(input1)

    my_func(tree1.root)


if __name__ == '__main__':
    main()
