# from collections import deque
from BinaryTree import BinaryTree


def dig_left(root):
    if root is None:
        return None

    while root.left:
        root = root.left

    return root


def parent_stream_successor(root):
    while root.parent:
        if root.parent.left == root:
            return root.parent
        root = root.parent

    return None


def find_inorder_successor_helper(root):
    if root is None:
        return None
    elif root.right:
        return dig_left(root.right)

    return parent_stream_successor(root)


def find_inorder_successor(root, predecessor_data):
    while root:
        if predecessor_data < root.data:
            root = root.left
        elif predecessor_data > root.data:
            root = root.right
        else:
            return find_inorder_successor_helper(root)

    if root is None:
        return -1


def main():
    input_val = [100, 50, 200, 25, 75, 125, 350]
    tree = BinaryTree(input_val)
    tree.populate_parents()

    # Adding non-existing nodes to look for in BST
    input_val.append(10)
    input_val.append(150)
    input_val.append(400)

    input_val.sort()

    # Displaying binary tree
    print("Binary tree:")
    # display_tree(tree.root)
    print()

    index_val = 0
    for node_value in input_val:
        index_val += 1
        # Function call to get the in-order successor
        successor = find_inorder_successor(tree.root, node_value)
        print(str(index_val) + ".", end="")
        print("\tNode Value: " + str(node_value))
        if successor != None:
            print("\t" + "Successor Node Value: " + str(successor.data))
        else:
            print("\tSuccessor Node Value: " + "None")
        print(
            "----------------------------------------------------------------------------------------------------\n")


if __name__ == '__main__':
    main()
