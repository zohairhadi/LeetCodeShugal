"""
Given a string s, return the longest palindromic substring in s.
"""

"""
why is there here?
Time Complexity: O()
"""


def longestPalindrome(s):
    longest = s[0]
    temp_longest = ""
    for i in range(0, len(s)-1):

        if s[i] == s[i+1]:
            count = 1
            while (i-count >= 0 and i+1+count < len(s)) and (s[i-count] == s[i+1+count]):
                count += 1
            count -= 1
            temp_longest = s[i-count: i+1+count + 1]

        if len(temp_longest) > len(longest):
            longest = temp_longest

        if s[i-1] == s[i+1]:
            count = 2
            while (i-count >= 0 and i+count < len(s)) and (s[i-count] == s[i+count]):
                count += 1
            count -= 1
            temp_longest = s[i-count: i+count + 1]

        if len(temp_longest) > len(longest):
            longest = temp_longest

    return longest


def main():
    print(longestPalindrome("abcbccabbacba"))

    print(longestPalindrome("babad"))

    print(longestPalindrome("cbbd"))

    print(longestPalindrome("abba"))

    print(longestPalindrome("ac"))

    print(longestPalindrome("ccc"))

    print(longestPalindrome("bb"))

    print(longestPalindrome("aaaaa"))


if __name__ == '__main__':
    main()
