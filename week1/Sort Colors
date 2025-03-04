class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        0 is red, 1 is white, 2 is blue. We want to sort the order in red, white, blue
        """
        left, mid = 0,0
        right = len(nums)-1
        while mid <= right:
            if nums[mid] == 0:
                nums[left],nums[mid] = nums[mid], nums[left]
                mid += 1
                left += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[right] = nums[right], nums[mid]
                right -= 1
