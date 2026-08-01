class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()

        for str_elm in strs:
            freq = [0]*26

            for ch in str_elm:
                freq[ord(ch)-ord('a')] += 1

            if tuple(freq) not in d:
                str_lst = []
                d[tuple(freq)] = str_lst
                d[tuple(freq)].append(str_elm)
            else:
                d[tuple(freq)].append(str_elm)

        return list(d.values())


        


        