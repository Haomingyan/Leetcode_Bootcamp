class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            if char != "]":
                stack.append(char)
            else: 
                encoded_str = []
                while stack and stack[-1] != "[":
                    encoded_str.append(stack.pop())
                stack.pop()

                k = []
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                
                count = int("".join(k[::-1]))
                k.pop()

                decoded_str = "".join(count * encoded_str[::-1])
                
                for item in decoded_str:
                    stack.append(item)

        return "".join(stack)
