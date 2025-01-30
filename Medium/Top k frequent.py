import heapq


class Solution(object):
    def topFrequent(self, nums, k):

        # freq_nums = 0
        # topFreq = []
        # for i in range(len(nums)):
        #     '''
        #      k = 0
        #     nums = [1,1,2,2,3]
        #     frequent 1 = 2
        #     frequent 2 = 2
        #     frequent 3 = 1
        #
        #     if nums[frequent] >= k:
        #         # return the element
        #
        #     '''
        #     if nums[i] == nums[i+1]:
        #         nums[freq_nums] = freq_nums + i
        #         freq_nums = nums[freq_nums]
        #
        # if freq_nums >= k:
        #     topFreq.append(freq_nums)
        #     # return the element e.g topFreq = [1,2]
        heap = []
        counter = {} # a dictionary to keep the number and its occurance
        for n in nums:
            counter[n] = 1 + counter.get(n,0)

        for key, freq in counter.items():
            heapq.heappush(heap, (freq, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [key for freq, key in heap]

solution = Solution()
print(solution.topFrequent([1,1,2,2,3], 2))



