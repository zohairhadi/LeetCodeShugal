def solution(arr):
    toReturn = ""
    cIndx = 0
    char = ''
    for wIndx in range(len(arr)):
        toReturn += arr[wIndx][cIndx]
        wIndx += 1

        if wIndx == len(arr) - 1:
            wIndx = 0


print(solution(["Daisy", "Rose", "Hyacinth", "Poppy"]))
