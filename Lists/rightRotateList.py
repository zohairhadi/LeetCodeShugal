


def right_rotate(lst, k):
    l = len(lst)
    to_return = [0] * l
    for (indx, val) in enumerate(lst):
        new_indx = (indx + k) % l
        # temp = lst[new_indx]
        # lst[new_indx] = lst[indx]
        # lst[indx] = temp
        to_return[new_indx] = lst[indx]
    return to_return


print(right_rotate([-1,-100,3,99], 2))
