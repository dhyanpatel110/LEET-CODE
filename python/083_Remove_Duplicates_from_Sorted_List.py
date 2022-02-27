'''
Example 1:
Input: head = [1,1,2]
Output: [1,2]
  
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

#CODE:
  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
          curr = head
        
          while curr and curr.next:
          	if curr.val == curr.next.val:
        	  	curr.next = curr.next.next
        	  else:
	          	curr = curr.next
          return head
