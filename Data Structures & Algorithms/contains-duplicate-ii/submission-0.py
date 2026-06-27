class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = set()
        cur = 0
        while cur < n and cur < k:
            if nums[cur] in seen:
                return True
            seen.add(nums[cur])
            cur += 1
        while cur < n:
            if nums[cur] in seen:
                return True
            seen.add(nums[cur])
            seen.remove(nums[cur - k])
            cur += 1
        return False
