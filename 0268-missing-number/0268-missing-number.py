class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        for num in nums:
            a^=num
        for i in range(len(nums)+1):
            b^=i
        return a^b



        