# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q : list = []
 
        if not head:
            return True

        node = head.val
        while node is not None:
            q.append(node.val)
            node = node.next

        if q == q.reverse():
            return True
        else:
            return False

        

head = ListNode[1,2,2,1]        
sol = Solution()
print(sol.isPalindrome(head))