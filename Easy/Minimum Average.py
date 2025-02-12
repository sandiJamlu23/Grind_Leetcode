class Solution(object):
    def minimumAverage(self, nums):
        '''

        1. find the smallest number in an array
        2. find the largest number in an array
        3. remove both from the list
        4. (largest + smallest) / 2 is stored in the result array
        5. sorting the number would be great
        '''

        nums.sort()
        avg_num = []

        while len(nums) > 1:
            # is 7 less than 8? yes
            # store 7 as the smallest
            # wait, it is already sorted, so the first index is indeed smaller than the next one
            # and the last index is the largest. ahhh I see
            smallest = nums.pop(0)
            largest = nums.pop(-1) # slicing. it is equal to nums[:-1]
            result = (smallest + largest) / 2.0
            # if the current avg is smaller then the next avg, keep the current smalles avg,
            # otherwise change it
            avg_num.append(result)
            # num[first].pop()
            # num[end].pop()

        # find the smallest in the min avg
        # smallest = min(min_avg)
        return min(avg_num)

solution = Solution()
number = [7,8,3,4,15,13,4,1]
ans = solution.minimumAverage(number)
print(ans)


