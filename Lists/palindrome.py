def solution(inputString):
    e = len(inputString) - 1
    for (indx, w) in enumerate(inputString):
        if indx > e/2:
            break
        if inputString[indx] != inputString[e - indx]:
            return False
    return True


print(solution("abbba"))
