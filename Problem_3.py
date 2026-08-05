# https://leetcode.com/problems/word-pattern/description/

# Time complexity: O(nm) where n is the length of strs and m is the max number of chars of any given string in strs
# Space complexity: O(nm)
# Explanation: Similar to isometric strings, we maintain two hashmaps between pattern and s (split by " ")
# If there is a mismatch at any point return false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_pat, map_word = {}, {}
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        for ch1, ch2 in zip(pattern, words):
            if (ch1 not in map_pat) and (ch2 not in map_word):
                map_pat[ch1] = ch2
                map_word[ch2] = ch1
            elif map_pat.get(ch1) != ch2 or map_word.get(ch2) != ch1:
                return False

        return True
