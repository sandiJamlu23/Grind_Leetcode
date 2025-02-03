
class Solution(object):
    def searchInsert(self, nums, target):
        position = []
        '''
        if it is not in the list find the closest element
         to the target.
         
         nums = [1,3,4,7], target 5
         * if it is bigger then current element, keep check the right element
         * stop if the right element is bigger then the current element
         
         if nums[i] < target < num[j]:
            
         * return the index of the current 
            element that is smaller than the target
         
        '''
        # middle = len(nums) // 2
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle_point = (left + right) // 2
            if target == nums[middle_point]:
                return middle_point
            elif target < nums[middle_point]:
                right = middle_point - 1
            elif target > nums[middle_point]:
                left = middle_point +1

        return left

solution = Solution()
print(solution.searchInsert([1,3,5,7], 4))





