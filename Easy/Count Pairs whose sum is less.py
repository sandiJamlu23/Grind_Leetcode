
class Solution(object):
    def countPairs(self, nums, target):

        nums.sort()

        # pairs = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] < target:
        #             pairs.append([i,j])
        #             return pairs
        count_pairs = 0
        current = 0
        last = len(nums)-1
        while current < last:
            if nums[current] + nums[last] < target:
                count_pairs += last - current
                current += 1
            else:
                last -= 1
        return count_pairs


solution = Solution()
print(solution.countPairs([-1,1,2,3,1], 2))