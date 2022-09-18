def find_sum(lst, k):
    for (inx,val) in enumerate(lst):
        toReturn = []
        toFind = abs(val - k)
        toReturn.append(val)
        
        if toFind in lst:
            toReturn.append(toFind)
            break

    return toReturn


print(find_sum([1,5,2,10,3], 12))