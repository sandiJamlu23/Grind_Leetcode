class trySort(object):
    def sorting(self, nums):
        '''

        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return nums

        '''

        mid_point = len(nums) // 2
        right = None
        left = None

        while left < right:
            if nums[mid_point] == mid_point:
                return mid_point

solution = trySort()
print(solution.sorting([1,2,4,3]))

