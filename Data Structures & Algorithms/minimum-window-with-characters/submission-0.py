class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count = 0
        left = 0
        min_len = float('inf')
        s_index = 0
        char_count = {}

        for ch in t:
            char_count[ch] = char_count.get(ch,0) + 1

        for right in range(len(s)):

            if s[right] in char_count:

                if char_count[s[right]] > 0:
                    count += 1

                char_count[s[right]] -= 1
            
            # try to shrink the window size and find the minimum 
            while count == len(t):

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    s_index = left

                if s[left] in char_count:

                    char_count[s[left]] += 1

                    if char_count[s[left]] > 0:
                        count -= 1
                    
                left += 1

        if min_len == float('inf'):
            return ""

        
               

        return s[s_index:min_len+s_index]

        


        
        