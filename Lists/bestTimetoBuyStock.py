"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

"""
why is there here?
Time Complexity: O()
"""


def my_func(prices):
    toReturn = 0
    minPrice = 0
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        elif prices[i] - minPrice > maxProfit:
            maxProfit = prices[i] - minPrice
        # for j in range(i+1, len(prices)):
        #     comp = prices[j]-prices[i]
        #     if comp > 0 and comp > toReturn:
        #         toReturn = comp

    return toReturn


def main():
    print(my_func([7, 6, 4, 3, 1]))


if __name__ == '__main__':
    main()
