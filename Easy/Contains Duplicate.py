class Solution(object):
    def containsDuplicate(self, nums):
        # num = []
        ''' Sort the array first'''
        # # first = nums[0]
        # for i in range(len(nums)):
        #     min_idx = i
        #     for j in range(i+1,len(nums)):
        #         if nums[i] < nums[min_idx]:
        #             nums[i],
        #             nums[min_idx] = nums[min_idx],
        #             nums[i]
        ''' use built in sort for the sake of it'''
        nums.sort()
        # return sorted_nums
        ''' Check the adjacent list'''
        for k in range(len(nums) - 1):
            if nums[k] == nums[k + 1]:
                return True
        return False


solution = Solution()
print(solution.containsDuplicate([1, 3, 2]))
