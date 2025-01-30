class Solution(object):
    def productExceptSelf(self, nums):
        '''https://www.youtube.com/watch?v=tSRFtR3pv74'''

        '''
        If nums = [1, 2, 3, 4], then:

            answer[0] = 2 * 3 * 4 = 24 (product of all elements except nums[0] = 1)
            
            answer[1] = 1 * 3 * 4 = 12 (product of all elements except nums[1] = 2)
            
            answer[2] = 1 * 2 * 4 = 8 (product of all elements except nums[2] = 3)
            
            answer[3] = 1 * 2 * 3 = 6 (product of all elements except nums[3] = 4)
        '''
        n = len(nums)

        left_prod = [1] * n
        right_prod = [1] * n

        out_arr = []

        # fill left product
        for i in range(1,n):
            left_prod[i] = nums[i-1] * left_prod[i-1]

        for i in range(n-2, -1,-1):
            right_prod[i] = nums[i+1] * right_prod[i+1]

        for i in range(n):
            out_arr.append(left_prod[i] * right_prod[i])

        return out_arr

solution = Solution()
print(solution.productExceptSelf([1,2,2,3]))
# print(solution)
