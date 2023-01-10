"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
"""

# imports here

"""
why is there here?
Time Complexity: O()
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for x in range(0, len(nums)):
        for y in range(x+1, len(nums)):
            # if nums[x] > target:
            #     continue
            # else:
            if (nums[x] + nums[y]) == target:
                return [x, y]


def main():
    print(twoSum([2, 7, 11, 15], 9))

    print(twoSum([3, 2, 4], 6))

    print(twoSum([3, 3], 6))

    print(twoSum([-1, -2, -3, -4, -5], -8))


if __name__ == '__main__':
    main()
