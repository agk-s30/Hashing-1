# https://leetcode.com/problems/group-anagrams/

# Time complexity: O(nm) where n is the length of strs and m is the max number of chars of any given string in strs
# Space complexity: O(nm)
# Explanation: Use a hashmap to store a mapping between the sorted string (key) and then every string in strs (value); return the values of this map
# an optimization on top of this is to create a key which does not require sorting, which is a mlog(m) time complexity
# so instead a tuple which is the counts of each char in a string can be used


class Solution:                                                       
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        # for s in strs:
        #     res[tuple(sorted(s))].append(s)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())

