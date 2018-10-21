# coding:utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""

二叉搜索树：左边的节点都比根节点小，右边的节点都比根节点大

如果有P  Q， P > 当前节点，Q > 当前节点 P 和 Q 肯定都在右边的子树上得继续找

            P < 当前节点，Q < 当前节点 P 和 Q 肯定都在左边的子树上，的继续找

            不是以上两种情况，那说明P 和 Q肯定一个在左 一个在右，当前节点就是 最近公共祖先


"""

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return root

        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root

