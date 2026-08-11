# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #if have no children then return or is empty return
        if root is None: 
            return None 
        
        #swap the two children
        temp = root.left 
        root.left = root.right 
        root.right = temp

        #run the function on each of the subtrees 
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        