class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            if nums[0] == val: 
                return 0
            return 1
        prev = 0
        cur = 0
        while prev < n:
            while prev < n and nums[prev] != val:
                prev += 1
            
            cur = prev + 1
            while cur < n and nums[cur] == val:
                cur += 1
            
            if cur < n:
                nums[prev], nums[cur] = nums[cur], nums[prev]
            else:
                return prev


