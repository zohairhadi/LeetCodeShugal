# Definition for singly-linked list.
from LinkedList import LinkedList

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

"""
why is there here?
Time Complexity: O()
"""


def removeNthFromEnd(head, n, c=0):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if head == None:
        return 1
    else:
        c += removeNthFromEnd(head.next_element, n, c)
        if c == n:
            print(head.data)
            return 1

    return c+1


def main():
    ulist1 = LinkedList()
    ulist1.insert_at_tail(1)
    ulist1.insert_at_tail(2)
    ulist1.insert_at_tail(3)
    ulist1.insert_at_tail(4)
    ulist1.insert_at_tail(5)

    print("List: ")
    ulist1.print_list()

    deleted, tempp = removeNthFromEnd(ulist1.get_head(), 2)

    print("Node being deleted", deleted)


if __name__ == '__main__':
    main()
