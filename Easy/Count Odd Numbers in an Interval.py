class Solution(object):
    def countOdds(self, low, high):
        '''

        suppose
        low = 1, high = 4

        output = 2,3
        odd_output = 1

        4-1 = 3
        4-2 = 2
        4-3 = 1

        low = 2, high = 5

        output = 2,3
        odd_output = 1

        5-1 = 4
        5-2 = 3
        5-3 = 2

        my approach was
        say low = 1, high = 4

        to find the interval we need to add or subtract to match either low or high.
        e.g

        4-1 = 3
        4-2 = 2
        4-3 = 1
        4-4 = 0

        from that we can see 3 and 2 (ignore if the calculation matches the lowest which is 1) and keep it in the list.
        then to find the odd number, from the calculation above, we use module,
        and append the result in a list, then we can return the length of the list

        '''
        # i = low
        # odd_num = []
        # if low == high:
        #     return 0
        # while low < high:
        #     nums = high-i
        #     if nums % 2 == 1:
        #         odd_num.append(nums)
        #     i += 1
        #
        # return  len(odd_num)

        ''' Brute force
        odd_num = []
        for i in range(low, high+1):
            if i % 2 == 1:
                odd_num.append(i)

        return len(odd_num)
        '''



        ''' THIS IS DUMB
            # if low == high:
            #     return 1
            # if low < high and high %2 == 1:
            #     return high // 2 + 1
            #
            # if low < high and low %2 == 1:
            #     return high//2'''
        return (high+1)//2 - low //2



solution = Solution()
print(solution.countOdds(8,7))