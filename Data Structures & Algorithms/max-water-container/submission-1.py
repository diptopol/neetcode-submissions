class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        area = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights), 1):
                if i != j:
                    h = min(heights[i], heights[j])
                    w = abs(j - i)

                    if (area < h * w):
                        area = h * w

        return area



