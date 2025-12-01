"""LeetCode Problem #2: Add Two Numbers

Difficulty: Medium

Problem:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each node contains a single digit.
Add the two numbers and return the sum as a linked list.

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(max(m, n)) where m and n are lengths of the lists
        Space Complexity: O(max(m, n)) for the result list
        
        Approach: Iterate through both lists simultaneously
        Track carry and create new nodes for the result
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Helper function to create linked list
    def create_list(arr):
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    
    # Helper function to convert linked list to array
    def list_to_array(head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr
    
    # Test
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Input: l1 = [2,4,3], l2 = [5,6,4]")
    print(f"Output: {list_to_array(result)}")
