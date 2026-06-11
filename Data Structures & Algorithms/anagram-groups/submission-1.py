class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {}

        for s in strs:
            key = self.getFrequencyKey(s)

            if key in map:
                map[key].append(s)
            else:
                map[key] = []
                map[key].append(s)
                
        
        return list(map.values())

    
    def getFrequencyKey(self, s: str):
        frequencyVals = [0] * 26

        for c in s:
            frequencyVals[ord(c) - ord('a')] += 1

        return ",".join([str(v) for v in frequencyVals])
