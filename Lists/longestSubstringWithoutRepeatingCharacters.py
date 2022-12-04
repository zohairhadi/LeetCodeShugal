
"""
Given a string s, find the length of the longest substring without repeating characters.
"""

"""
why is there here?
Time Complexity: O()
"""


def my_func(s):
    subStr1 = ""
    subStr2 = ""
    isFirst = True
    for chr in s:
        if isFirst:
            if chr not in subStr1:
                subStr1 += chr
            else:
                print(subStr1.index(chr))
                subStr2 = subStr1[subStr1.index(chr)+1:] + chr
                isFirst = False
        else:
            if chr not in subStr2:
                subStr2 += chr
            else:
                subStr2 = subStr2[subStr2.index(chr)+1:] + chr

        if len(subStr2) > len(subStr1):
            subStr1 = subStr2
            subStr2 = ""
            isFirst = True

    return subStr1


def main():
    print(my_func("loddktdji"))


# abcdefdhijklmnoplu
if __name__ == '__main__':
    main()
