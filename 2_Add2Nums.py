"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Explanation: 342 + 465 = 807.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        A_val = 0
        i=0
        C_val = []
        carry = 0;
        while(l1 or l2):
            tmp = l1.val + l2.val + carry
            carry = 0
            if tmp > 9:
                tmp = tmp%10
                carry = 1;
            C_val.append(int(tmp))
            l1 = l1.next
            l2 = l2.next
            if l1 == None:
                while(l2):
                    tmp = l2.val+carry
                    carry = 0
                    if tmp > 9:
                        tmp = tmp%10
                        carry = 1;
                    C_val.append(tmp)
                    l2=l2.next
            if l2 == None:
                while(l1):
                    tmp = l1.val+carry
                    carry = 0
                    if tmp > 9:
                        tmp = tmp%10
                        carry = 1;
                    C_val.append(tmp)
                    l1=l1.next
        if carry == 1:
            C_val.append(1)
        return C_val

def main():
	l1=ListNode(342)
	l2=ListNode(465)
	obj = Solution()
	print(obj.addTwoNumbers(l1, l2))

main()

