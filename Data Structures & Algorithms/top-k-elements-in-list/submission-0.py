class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, f in freq.items():
            freq_buck = buckets[f]
            freq_buck.append(num)

        most_freq_nums = []
        count = 0
        for f in range(len(nums), 0, -1):
            if buckets[f]:
                for num in buckets[f]:
                    most_freq_nums.append(num)
                    count += 1

                    if count == k:
                        return most_freq_nums

        
        return []
