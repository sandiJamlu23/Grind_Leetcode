from collections import Counter
class Solution(object):
    def numTilePossibilities(self, tiles):
        def backtrack(index, current):
            # convert string to list
            # str_to_list = [char for char in tiles]
            # make the copy of current
            print("current count",counts)
            print("current combination", current)
            result.add("".join(current)) # avoid duplicates
            '''
            tiles = "AAABBC"
                counts = Counter(tiles)
                print(counts)  # Output: Counter({'A': 3, 'B': 2, 'C': 1})
            '''
            #  iterate three times: once for 'A', once for 'B', and once for 'C'
            for char, count in counts.items():
                if count > 0 : # check if the character is available
                    current.append(char)
                    # counts['A'] -= 1 becomes counts['A'] = 2 - 1 = 1.
                    # So, now counts is Counter({'A': 1, 'B': 1}).

                    # On the next recursive call, if we choose 'A' again, the loop will again look at 'A' and see that count is now 1.
                    # counts['A'] -= 1 becomes counts['A'] = 1 - 1 = 0. So, now counts is Counter({'A': 0, 'B': 1})
                    counts[char] -= 1
                    backtrack(index+1, current)
                    counts[char] += 1
                    current.pop()
                # undo the last index

        counts = Counter(tiles)
        result = set()
        backtrack(0, [])
        return len(result) - 1
        # return result

solution = Solution()
til = "ABC"
print(solution.numTilePossibilities(til))
