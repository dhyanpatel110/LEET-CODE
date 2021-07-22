'''
Example 1:
  Input: head = [1,2,3,4]
  Output: [2,1,4,3]
'''

<img src="https://media.wired.com/photos/5926db217034dc5f91becd6b/master/w_582,c_limit/so-logo-s.jpg" width="250">
import urllib.request
from PIL import Image
  
urllib.request.urlretrieve(
  'https://media.geeksforgeeks.org/wp-content/uploads/20210318103632/gfg-300x300.png',
   "gfg.png")
  
img = Image.open("gfg.png")
img.show()

CODE:
  class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        d1 = d = ListNode(0)
        d.next = head
        
        while d.next and d.next.next:
            
            p = d.next
            q = d.next.next
            d.next,p.next,q.next = q,q.next,p
            d = p
        return d1.next
      
      
      
      
      
