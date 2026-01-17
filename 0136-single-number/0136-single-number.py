class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        for num in nums:
            k^=num
        return k
        