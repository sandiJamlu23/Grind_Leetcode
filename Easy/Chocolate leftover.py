class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        '''
        price = [1,2,3], money = 3

        so if I want to buy the chocolate, my debt would be 0

        sum_debt = money

        price [0] = 1 
        price [1] = 2
        price [2] = 3

        if price[i] + price[j] == money:
            return sum_debt

        elif price[i] + price[j] < money:
            return how much is the leftover
            sum_debt = money - (price[i] + price[j])
            return sum_debt
        else:
            return sum_debt

        price = [2,2,3], money = 3
        the debt would be 1

        price = [4,4,4], money = 3
        just return the money

        '''
        min_leftover = money
        pairs = False

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                cost = prices[i] + prices[j]
                if cost <= money:
                    leftover = money - cost
                    if leftover < min_leftover:
                        min_leftover = leftover
                        pairs = True

        return min_leftover if pairs else money


solution = Solution()
print(solution.buyChoco([98, 54, 6, 34, 66, 63, 52, 39], 62))