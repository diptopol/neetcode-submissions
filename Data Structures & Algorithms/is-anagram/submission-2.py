class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = {}

        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] = map[c] + 1 

        for c in t:
            if c not in map:
                return False
            else:
                if map[c] == 0:
                    return False
                else:
                    map[c] = map[c] - 1
                
        for c in map:
            if map[c] != 0:
                return False

        return True 