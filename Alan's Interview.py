class Solution(object):
    def findEven(self, nums):
        '''

        nums = [1,2,3,4]
        odd_num = [2,4]

        1 / 2 = fract
        3 / 2 = fract
        2 / 2 = 1
        4 / 2 = 2

        if nums[i] % 2 == 0:
            return odd_num.append([i])

        '''

        even_num = []
        for num in nums:
            if num % 2 == 0:
                even_num.append(num)
                # even_num = even_num[i]

        return even_num

solution = Solution()
print(solution.findEven([1,2,3,4]))
