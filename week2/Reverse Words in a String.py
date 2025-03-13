class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        if not words:
            return None
        reversed_str = words[::-1]
        return " ".join(reversed_str)
        
        
