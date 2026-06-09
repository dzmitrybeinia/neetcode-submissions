class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxSize = (r - l) * min(heights[l], heights[r])
        while l < r:
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
            curSize = (r - l) * min(heights[l], heights[r])
            maxSize = max(maxSize, curSize)
        return maxSize