from http.cookiejar import cut_port_re


class Solution(object):
    def longestConsecutive(self, nums):
        '''

        Convert to set: num_set = {100, 4, 200, 3, 2, 1}.

        Check each number:

        1: 0 is not in the set → start of a sequence.

        Expand: 1, 2, 3, 4 → length = 4.

        2: 1 is in the set → not a start.

        3: 2 is in the set → not a start.

        4: 3 is in the set → not a start.

        100: 99 is not in the set → start of a sequence.

        Expand: 100 → length = 1.

        200: 199 is not in the set → start of a sequence.

        Expand: 200 → length = 1.

        The longest sequence is [1, 2, 3, 4] with length 4.
        '''
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # Only consider `num` if it is the start of a sequence.
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1

                # Count upward until the sequence breaks.
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest

solution = Solution()
print(solution.longestConsecutive([1,2,3,100]))

