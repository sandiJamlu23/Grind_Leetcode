class Solution(object):
    def combine(self, n, k):
        def backtrack(index, current_combination):
            # result.sort() # this is for the k case, which I am still not sure what that mean
            if len(current_combination) == k: # Base case: Combination of length k is formed
                final_result.append(current_combination[:])
                return
            for i in range(index, len(intervals)): # iterate from start to n
                # choose the current number
                num = intervals[i]
                current_combination.append(num)
                # backtrack
                backtrack(i + 1, current_combination) # Explore further combinations, starting from the next number
                # pop the current number
                current_combination.pop()

        intervals = []
        for i in range(1, n+1):
            intervals.append(i)
        # backtrack(0, [])
        # # find the interval
        # i = 0
        # while i < n:
        #     interval = i + 1
        #     result.append(interval)
        #     i += 1
        final_result = []
        backtrack(0,[])  # Start from the beggining of intervals, with an empty combination
        return final_result

solution = Solution()
print(solution.combine(4,2))
