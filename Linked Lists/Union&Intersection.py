from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    # Write your code here
    l1_cur_node = list1.get_head()
    while l1_cur_node.next_element is not None:
        l1_cur_node = l1_cur_node.next_element

    l1_cur_node.next_element = list2.get_head()

    l1_cur_node.next_node = None
    list1.remove_duplicates()
    return list1

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    # Write your code here

    return list1


# main
ulist1 = LinkedList()
ulist2 = LinkedList()
ulist1.insert_at_head(8)
ulist1.insert_at_head(22)
ulist1.insert_at_head(15)

print("List 1")
ulist1.print_list()

ulist2.insert_at_head(21)
ulist2.insert_at_head(14)
ulist2.insert_at_head(7)

print("List 2")
ulist2.print_list()

new_list = union(ulist1, ulist2)

print("Union of list 1 and 2")
new_list.print_list()
