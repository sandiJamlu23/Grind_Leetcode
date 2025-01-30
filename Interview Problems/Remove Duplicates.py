class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for i in range(1, len(nums)):
            # for j in range(i+1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k

solution = Solution()
print(solution.removeDuplicates([1,1,1,2,3]))

'''
list1 = [1, 1, 2, 3]

list1[0] =  1 
            1 
            2
            3
            
'''