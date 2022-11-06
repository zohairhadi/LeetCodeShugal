import copy


def find_max_sum_sublist(lst):
    # Write your code here!
    lst_to_return = copy.deepcopy(lst)
    max_sum = sum(lst_to_return)

    # TODO: if we modify lst duing loop what will happen
    for (indx, val) in enumerate(lst_to_return):
        reduced_lst_sum = max_sum + val
        if reduced_lst_sum < max_sum:
            lst_to_return.remove(val)  # remove val from lst_to_return
            # cal new sum without that val and put in max_sum
            max_sum = sum(lst_to_return)

    return sum(lst_to_return)


print(find_max_sum_sublist([-2, 10, 7, -5, 15, 6]))

# print(find_max_sum_sublist([-4, 2, -5, 1, 2, 3, 6, -5, 1]))
