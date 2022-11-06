def max_min(lst):
    # Write your code here
    for (indx, val) in enumerate(lst):
        if indx%2 == 0: #even then find latest max
            min_max_indx = find_min_or_max(lst[indx:], False) + indx # search for next max
        else: #odd then find latest min
            min_max_indx = find_min_or_max(lst[indx:], True) + indx # search for next min 

        # replace current with next max
        temp = lst[indx]
        lst[indx] = lst[min_max_indx]
        lst[min_max_indx] = temp

    return lst
    pass


def find_min_or_max(lst,is_min):
    val_to_check = lst[0]
    val_indx = 0
    for (indx, val) in enumerate(lst):
        if is_min:
            if val<val_to_check:
                val_to_check = val
                val_indx = indx
        else:
            if val>val_to_check:
                val_to_check = val
                val_indx = indx
    return val_indx

to_print = max_min([1,2,3,4,5,6])

print(to_print)