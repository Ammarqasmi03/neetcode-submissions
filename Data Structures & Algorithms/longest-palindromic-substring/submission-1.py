class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        LPS = ""
        for i in range(len(s)):
            # odd length palindrome
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            palindrome = s[left+1:right]
            if len(palindrome) > len(LPS):
                LPS = palindrome

            left = i
            right = i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            palindrome = s[left+1:right]
            if len(palindrome) > len(LPS):
                LPS = palindrome
               

        return LPS


        