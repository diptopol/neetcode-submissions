class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = True

        max_length = 0

        part_of_seq = {}
        for i in range(len(nums)):
            if nums[i] in part_of_seq:
                continue

            start = nums[i]
            seq_length = 1
            next = start + 1

            part_of_seq[start] = True
            while next in map:
                part_of_seq[next] = True
                seq_length += 1
                next += 1

            if max_length < seq_length:
                max_length = seq_length
            
        return max_length
            