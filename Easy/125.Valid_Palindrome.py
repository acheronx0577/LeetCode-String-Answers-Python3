# First Solution
import time


# Reverse String Solution. This solution is not recommended because it uses built-in functions and extra memory.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""  # We create a new string to remove non-alphanumerical characters

        # Iterate through every single character (c) in the string (s)
        for c in s:
            if c.isalnum():  # Check if character (c) is alphanumerical
                newStr += c.lower()  # If alphanumerical, add it to the new string and convert to lowercase
        # Check if the new string is exactly the same when reversed
        return newStr == newStr[::-1]

# The reason you don't want to use this approach is that it uses extra memory to build a new string
# and reverses the string. Also, it uses built-in functions which are sometimes not allowed in interviews.


# Don't copy the code below this in LeetCode
sol = Solution()
start = time.time()
result = sol.isPalindrome("A man, a plan, a canal: Panama")
end = time.time()
print(f"Result: {result}, Time: {(end-start)*1000:.3f} ms")


# Second Solution (Prefered Solution)
import time

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize two pointers: 
        # l (left pointer) starts at the BEGINNING of the string (index 0)
        # r (right pointer) starts at the END of the string (index len(s)-1)
        l, r = 0, len(s) - 1
        
        # Continue this process until the pointers meet or cross each other
        # When l >= r, we've checked all character pairs
        while l < r:
            
            # Skip any non-alphanumeric characters from the LEFT side
            # Keep moving left pointer RIGHT → until we find a valid character
            while l < r and not self.alphaNum(s[l]):
                l += 1  # Move left pointer one position to the right
            
            # Skip any non-alphanumeric characters from the RIGHT side  
            # Keep moving right pointer LEFT ← until we find a valid character
            while r > l and not self.alphaNum(s[r]):
                r -= 1  # Move right pointer one position to the left
            
            # Compare the characters at both pointers (convert to lowercase for case-insensitive comparison)
            # If they don't match, immediately return False - it's not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            
            # Move both pointers toward the center for the next comparison
            l, r = l + 1, r - 1  # Left moves → right, Right moves ← left
        
        # If we exit the loop, it means all character pairs matched
        # The string is a palindrome!
        return True

    # ======== HELPER FUNCTION ========
    def alphaNum(self, c):
        """
        Checks if character c is alphanumeric (A-Z, a-z, 0-9) using ASCII values.
        Returns True if c is: 
        - Uppercase letter (A-Z, ASCII 65-90) OR
        - Lowercase letter (a-z, ASCII 97-122) OR  
        - Digit (0-9, ASCII 48-57)
        Returns False for spaces, punctuation, symbols.
        """
        return (ord('A') <= ord(c) <= ord('Z') or  # A-Z check
                ord('a') <= ord(c) <= ord('z') or  # a-z check
                ord('0') <= ord(c) <= ord('9'))    # 0-9 check


# Don't copy the code below this in LeetCode
sol = Solution()
start = time.time()
result = sol.isPalindrome("A man, a plan, a canal: Panama")
end = time.time()
print(f"Result: {result}, Time: {(end - start) * 1000 :.2f} ms")
