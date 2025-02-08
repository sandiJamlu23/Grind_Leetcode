class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit

solution = Solution.maxProfit([7,1,5,3,6,4])
print(solution)
            '''
            Input: prices = [7,1,5,3,6,4]
            Output: 5
            Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
            Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
        
            find the max profit
             7 & 1 = 1-7 -> return 0
             7 & 5 = 5-7 -> return 0
             7 & 3 = 3-7 -> return 0
             7 & 6 = 6-7 -> return 0
        
             1 & 5 = 5- 1 -> return 4
             1 & 3 = 3-1 -> return 2
             1 & 5 = 5-1 -> return 4
                            return 5
                            return 3
        
            create an empty array to store the result, which is the max profit.
            to do that, we need to compare current element 'i' with the next element, we can use for loop.
            in the loop, compare each element with the one next to it, we can use brute force.
        
            now, to find the profit, the current element is substracted by the next element,
                if the next element is smaller then current element, return 0
                else keep the result as the current max profit, if the next profit is bigger then the current profit...
                    keep it, else the current profit is the biggest profit
        
            find the max element in the empty list
            '''

