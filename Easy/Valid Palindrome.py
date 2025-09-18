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

