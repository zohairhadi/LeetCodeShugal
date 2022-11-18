def minNumOfPlayers(chatOfPlayers: str):
    minNumOfPlayers = 0
    countC = 0
    countH = 0
    countA = 0
    countT = 0

    for ch in chatOfPlayers:
        if ch == 'c':
            countC += 1
            minNumOfPlayers = max(countC, minNumOfPlayers)
        elif ch == 'h':
            countH += 1
            if countH > countC:
                return -1
        elif ch == 'a':
            countA += 1
            if countA > countH:
                return -1
        elif ch == 't':
            countT += 1
            if countT > countA:
                return -1

            countC -= 1
            countH -= 1
            countA -= 1
            countT -= 1

    if countC == 0 and countH == 0 and countA == 0 and countT == 0:
        return minNumOfPlayers
    else:
        return -1


def main():
    print(minNumOfPlayers("cchathat"))


if __name__ == '__main__':
    main()
