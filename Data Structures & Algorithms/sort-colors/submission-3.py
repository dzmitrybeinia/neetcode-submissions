class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero = 0
        one = 0
        two = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            elif nums[i] == 1:
                one += 1
            else:
                two += 1
        cur = 0
        while zero != 0:
            nums[cur] = 0
            zero -= 1
            cur += 1
        while one != 0:
            nums[cur] = 1
            one -= 1
            cur += 1
        while two != 0:
            nums[cur] = 2
            two -= 1
            cur += 1
        