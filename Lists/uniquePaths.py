"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

"""
why is there here?
Time Complexity: O()
"""




import os
def printMaze(m, n, r, c):
    os.system('clear')
    for i in range(r):
        for j in range(c):
            if i == m and j == n:
                print("1 ", end='')
            else:
                print("0 ", end='')
        print()


def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    r, c = m, n
    recursive(0, 0, r, c)


def recursive(current_row, current_column, r, c):
    if current_row == r - 1 and current_column == c - 1:
        print("found")
        return 1
    elif current_row == r or current_column == c:
        return 0
    else:
        recursive(current_row + 1, current_column, r, c)
        recursive(current_row, current_column + 1, r, c)


def main():
    print("Total Count: ", uniquePaths(3, 7))


if __name__ == '__main__':
    main()
