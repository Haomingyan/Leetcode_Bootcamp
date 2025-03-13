class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        p_count = {}
        for char in p:
            
            p_count[char] = p_count.get(char,0) + 1

        window_count = {}
        result = []
        for i, char in enumerate(s):
            window_count[char] = window_count.get(char,0) + 1
            if i >= len(p):
                left_char = s[i-len(p)]
                window_count[left_char] -= 1
                if window_count[left_char] == 0:
                    del window_count[left_char]
            if window_count == p_count:
                result.append(i-len(p)+1)
        
        return result
        
