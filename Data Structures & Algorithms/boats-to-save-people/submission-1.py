class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l = 0
        r = len(people) - 1
        res = 0
        people.sort()
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            res +=1
                
        return res



# 1 2 2 3 3 
#   l
#   r

# limit = 3
# res = 3
