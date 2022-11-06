'''
Implement a function rearrange(lst) which rearranges the elements such that all the negative 
elements appear on the left and positive elements appear at the right of the list. 
Note that it is not necessary to maintain the sorted order of the input list.
'''

def rearrange(lst):
    # Write your code here
    exchange_indx = 0
    for (indx,val) in enumerate(lst):
        if val<0:
            temp = lst[exchange_indx]
            lst[exchange_indx] = lst[indx]
            lst[indx] = temp
            exchange_indx += 1
    return lst 


print(rearrange([1,-3,4,-4]))