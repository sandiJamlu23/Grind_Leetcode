class Solution(object):
    def removeElements(self, nums, val):
        '''
        return the number of elements in nums which are not equal to val

        requirements
        1. the first k elements must not equal to val.
        2. return k (the number of elements)
        '''

        '''
        nums = [1,2,2,3,4]
        val = 3
        
        return k -> [1,2,2,4] = 4
        
        iterate through the nums and find the element of each index.
        then compare each element with val.
        something like
        
        for i in range (len(nums)):
        
        nums[0] = 1 vs 3
        nums[1] = 2 vs 3
        nums[2] = 2 vs 3
        nums[3] = 3 vs 3
        nums[4] = 4 vs 3
        
        increment the i until it reach the len of nums
        
        if the nums does not equal to val, keep it in the new list, which is k
            
        '''
        k = 0
        for i in range(len(nums)-1):

            if nums[i] != val:
                # k.append(nums[i])
                nums[k] = nums[i]
                k += 1
        return k

solution = Solution()
print(solution.removeElements([1,2,2,3], [3]))
