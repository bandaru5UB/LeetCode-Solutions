"""LeetCode Problem #9: Palindrome Number

Difficulty: Easy

Problem:
Given an integer x, return true if x is a palindrome, and false otherwise.

Example:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Time Complexity: O(log n) where n is the value of x
        Space Complexity: O(1)
        
        Approach: Mathematical reversal
        Reverse the second half of the number and compare with first half.
        Handle negative numbers and numbers ending in 0.
        """
        # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even length: x == reversed_half
        # For odd length: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    x1 = 121
    print(f"Input: x = {x1}")
    print(f"Output: {solution.isPalindrome(x1)}")
    print()
    
    # Test case 2
    x2 = -121
    print(f"Input: x = {x2}")
    print(f"Output: {solution.isPalindrome(x2)}")
    print()
    
    # Test case 3
    x3 = 10
    print(f"Input: x = {x3}")
    print(f"Output: {solution.isPalindrome(x3)}")
    print()
    
    # Test case 4
    x4 = 12321
    print(f"Input: x = {x4}")
    print(f"Output: {solution.isPalindrome(x4)}")
