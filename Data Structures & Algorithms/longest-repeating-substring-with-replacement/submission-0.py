class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        left = 0
        longest = 0
        count = {}
        maxf = 0
        
        for right in range(len(s)):

            count[s[right]] = count.get(s[right],0) + 1
            maxf = max(maxf,count[s[right]])
            
            # window size = right - left + 1
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest,right - left + 1)

        return longest
                


            

            


        

        