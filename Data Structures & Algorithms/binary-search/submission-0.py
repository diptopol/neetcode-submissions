class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1) 
        

    def binarySearch(self, nums: List[int], target: int, start: int, end: int):
        middle = start + ((end - start) // 2)

        if nums[middle] == target:
            return middle
        elif (nums[middle] < target and middle < end):
            return self.binarySearch(nums, target, middle + 1, end)
        elif (nums[middle] > target and middle > start):
            return self.binarySearch(nums, target, start, middle - 1)
        else:
            return -1
    

    