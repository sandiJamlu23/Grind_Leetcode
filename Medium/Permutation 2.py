class Solution(object):
    def permuteUnique(self, nums):
        def backtrack(used, current):
            '''
                1.  - start from 1, include 1 in the list = [1]
                    - include 1 in the previous list = [1,1]
                    - include 2 = [1,1,2]

                2.  - start from 1, include 1 in the list = [1]
                    - include 2 = [1,2]
                    - include 1 = [1,2,1]

                3.  - start from 2, include 2 in the list = [2]
                    - include 1 = [2,1]
                    - include 1 = [2,1,1]
            '''
            # base case
            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):
                if i in used:
                    continue
                # Skip duplicates when previous same element is not used
                if i > 0 and nums[i] == nums[i - 1] and (i - 1 not in used):
                    continue
                # Choose the current index
                used.add(i)
                current.append(nums[i])
                # Recurse
                backtrack(used, current)
                # Unchoose
                current.pop()
                used.remove(i)

        nums.sort()  # Sort to handle duplicates
        result = []
        backtrack(set(), [])
        return result

solution = Solution()
n = [1,1,2]
print(solution.permuteUnique(n))