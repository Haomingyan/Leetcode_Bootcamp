class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1
        
        freq_lst = []
        for num in freq_dict:
            freq_lst.append((freq_dict[num],num))
        
        freq_lst.sort(reverse = True)

        result = []
        for i in range(k):
            result.append(freq_lst[i][1])
        return result
