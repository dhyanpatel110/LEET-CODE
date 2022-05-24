'''
Example 1:

    7
  /   \
 3    15
     /  \
    9   20
    
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
'''

CODE:
  # Definition for a binary tree node.
  # class TreeNode:
  #     def __init__(self, val=0, left=None, right=None):
  #         self.val = val
  #         self.left = left
  #         self.right = right
  class BSTIterator:

      def __init__(self, root: Optional[TreeNode]):
          self.stack = []
          while root:
              self.stack.append(root)
              root = root.left

      def next(self) -> int:
          res = self.stack.pop()
          cur = res.right
          while cur:
              self.stack.append(cur)
              cur = cur.left
          return res.val

      def hasNext(self) -> bool:
          return self.stack != []
        
        
        
