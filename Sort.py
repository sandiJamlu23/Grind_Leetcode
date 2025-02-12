# class trySort(object):
#     def sorting(self, nums):
#         '''
#
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)-1):
#                 if nums[j] > nums[j+1]:
#                     temp = nums[j]
#                     nums[j] = nums[j+1]
#                     nums[j+1] = temp
#         return nums
#
#         '''
#
#         mid_point = len(nums) // 2
#         right = None
#         left = None
#
#         while left < right:
#             if nums[mid_point] == mid_point:
#                 return mid_point
#
# solution = trySort()
# print(solution.sorting([1,2,4,3]))

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pair = {}

        for i, num in enumerate(nums):
            if target - num in pair:
                return [i, pair[target - num]]
            pair[num] = i

solution = Solution()
solution.twoSum([1, 2, 3, 4], 5)