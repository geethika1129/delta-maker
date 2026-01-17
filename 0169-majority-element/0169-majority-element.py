class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        c=Counter(nums)
        for a in nums:
            if c[a]>n//2:
                return a
        