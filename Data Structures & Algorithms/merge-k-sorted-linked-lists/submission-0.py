# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
        dummy = ListNode(0)
        res = dummy
        i = len(lists)
        while len(min_heap) > 0:
            cur = heapq.heappop(min_heap)
            cur_val = cur[0]
            res.next = ListNode(cur_val)
            res = res.next
            if cur[2].next:
                cur_next = cur[2].next
                heapq.heappush(min_heap, (cur_next.val, i, cur_next))
            i += 1
        return dummy.next
        
