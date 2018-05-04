# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # return " -> ".join(str(sum(map(lambda x: int("".join(reversed(list(filter(lambda y: 48 <= ord(y) <= 57, x))))), a.split("+"))))) 以为输入是字符串....
        '''
        data = []
        index = 0
        l1_len = len(l1)
        l2_len = len(l2)
        back = 0
        while back or (index < l1_len and index < l2_len):
            l1_val = 0
            if index < l1_len:
                l1_val = l1[index]
            l2_val = 0
            if index < l2_len:
                l2_val = l2[index]
            s = l1_val+ l2_val+ back
            data.append(s%10)

            back = s // 10
            index+=1
        return " -> ".join(map(str, data))
        看测试用例 以为是list...醉了 
        ''' 
        
        data = []

        back = 0
        while back or l1 or l2:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
                l1=l1.next
            if l2:
                l2_val = l2.val
                l2=l2.next
            s = l1_val+l2_val + back
            data.append(s%10)

            back = s // 10
            
            
        return data
