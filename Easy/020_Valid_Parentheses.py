"""LeetCode Problem #20: Valid Parentheses

Difficulty: Easy

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example:
Input: s = "()[]{}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Approach: Stack
        Use a stack to keep track of opening brackets.
        When encountering a closing bracket, check if it matches the top of the stack.
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                # Closing bracket
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                # Opening bracket
                stack.append(char)
        
        # Stack should be empty if all brackets are matched
        return len(stack) == 0

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    s1 = "()"
    print(f"Input: s = \"{s1}\"")
    print(f"Output: {solution.isValid(s1)}")
    print()
    
    # Test case 2
    s2 = "()[]{}"
    print(f"Input: s = \"{s2}\"")
    print(f"Output: {solution.isValid(s2)}")
    print()
    
    # Test case 3
    s3 = "(]"
    print(f"Input: s = \"{s3}\"")
    print(f"Output: {solution.isValid(s3)}")
    print()
    
    # Test case 4
    s4 = "{[]}"
    print(f"Input: s = \"{s4}\"")
    print(f"Output: {solution.isValid(s4)}")
