class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 2**31-1
        min = -2**31
        
        s=s.lstrip()
        if not s:
            return 0
        
        sign = 1
        index = 0
        if s[index] == "-":
            sign = -1
            index+=1
        elif s[index] == "+":
            index += 1
        
        result = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            if result <= (max-digit)//10:
                result = result * 10 + digit
            else:
                return max if sign == 1 else min
            index+=1
        return sign * result
