'''
You are given an array of integers numbers and two integers left and right.
You task is to calculate a boolean array result, where result[i] = true
if there exists an integer x, such that numbers[i] = (i + 1) * x and left ≤ x ≤ right.
Otherwise, result[i] should be set to false.
'''


def solution(numbers, left, right):
    toReturn = [False] * len(numbers)
    for indx, n in enumerate(numbers):
        if numbers[indx] % (indx+1) == 0:
            x = numbers[indx] / (indx+1)
            if x <= right and left <= x:
                toReturn[indx] = True
    return toReturn


print(solution([8, 5, 6, 16, 5], 1, 3))
