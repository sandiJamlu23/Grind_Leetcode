# Learn hashmap
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for s in strs:
            # sort all the word
            sorted_strs = tuple(sorted(s)) # tuple is a imutable list
            # assign the word as the key in the hashmap
            result[sorted_strs].append(s) # Append the word to the corresponding key

        return list(result.values())

solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))