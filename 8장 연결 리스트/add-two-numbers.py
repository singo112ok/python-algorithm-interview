# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def NodeToNum(node:Optional[ListNode]) -> int:
            s : string = ""
            while node:
                s = str(node.val) + s
                node = node.next
            return int(s)    
    
        def NumToNode(l1:int) ->ListNode:
            # 역방향
            # strval : string = str(l1)
            # prev : ListNode = None
            # for s in strval:
            #     node = ListNode(s)
            #     node.next = prev
            #     prev = node     
            # return node
            
            # 정방향
            strval : string = str(l1)
            strval = strval[::-1]
            prev  : ListNode = None
            first : ListNode = None           
            for s in strval:
                curr = ListNode(s)
                if first is None:
                    first = curr
                if prev is not None:
                    prev.next = curr
                prev = curr            
                    
            return first

    
        s1 = NodeToNum(l1)
        s2 = NodeToNum(l2)     
        print(s1+s2)        
        return NumToNode(s1+s2)