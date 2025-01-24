# class Solution:
#     def search(self, nums, target):
#         # num = []
#         for i in range (len(nums)):
#             if nums[i] == target:
#                 return i
#             return -1
#
# solution = Solution()
# print(solution.search([-1,0,3,5,9,12], 9))

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:  # Use <= for proper bounds
            mid_point = (left + right) // 2

            if nums[mid_point] == target:
                return mid_point
            elif nums[mid_point] < target:
                left = mid_point + 1  # Narrow the search range
            else:
                right = mid_point - 1  # Narrow the search range

        return -1  # Target not found

'''
left = 0
right = 4

1. 0+4 // 2 = 2
Target is bigger than 3
left = 1
2. 1+4//2 = 2
target is biger than 3
3. 2+4 //2 = 3
target is bigger than 5
4. 3+4 // 2 = 3
target is bigger than 5
5. 4+4 // 2 = 4
target == midpoint
'''