class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for idx, i in enumerate(nums):
            if ((target - i) not in map):
                map[i] = idx
            else:
                return [map.get(target - i), idx]

        return []