# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        data = []
        def func(root):
            if root != None:
                data.append(root.val)
                func(root.left)
                func(root.right)
                
        func(root)
        return data