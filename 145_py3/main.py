# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        data = []
        def func(root):
            if root != None:
                func(root.left)
                func(root.right)
                data.append(root.val)
        func(root)
        return data
        