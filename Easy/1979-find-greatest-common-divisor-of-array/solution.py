class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minimum = nums[0]
        maximum = nums[0]
        for num in nums:
            minimum = min(minimum, num)
            maximum = max(maximum, num)
        while maximum != 0:
            minimum, maximum = maximum, minimum % maximum
        return minimum
