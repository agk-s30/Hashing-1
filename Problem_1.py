# https://leetcode.com/problems/isomorphic-strings/

# Time complexity: O(n)
# Space complexity: O(1) because only 256 valid values
# Explanation: Use hashmap to store the mapping between s and t, and also another hashmap to store the reverse mapping between t and s

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}
        for sch, tch in zip(s, t):
            if (sch not in s_map) and (tch not in t_map):
                s_map[sch] = tch
                t_map[tch] = sch
            elif s_map.get(sch) != tch or t_map.get(tch) != sch:
                return False
        
        return True
