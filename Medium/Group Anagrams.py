'''
Consideration
def sorted_word(strs):

word = list(strs)
for i in range(len(word)):
    for j in range(0, len(word) -i-1):
        if word[j] > word[j+1]:
            temp = word[j]
            word[j] = word[j+1]
            word[j+1] = temp

return ''.join(word)

num = [ 1,3,2,4]

1 vs 3
1 vs 2
1 vs 4

3 vs 2 ->
    temp = 3
    3 = word[j+1]
    2 = temp

    2,3

3 vs 4
4 vs 4
'''


class Solution(object):
    def groupAnagrams(self, strs):

        '''


        "eat", "tea", "tan"

        sorted strs: "aet" , "aet", "ant"

        if strs[i] == strs[j]:
            return true
        else:
            return False

        '''
        groups = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []
            groups[sorted_word].append(word)

        # result = []
        # for group in groups.values():
        #     result.append(group)

        return  list(groups.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))