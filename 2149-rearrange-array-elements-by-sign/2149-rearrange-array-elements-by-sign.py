class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0]*len(nums)
        p=0
        n=1
        for num in nums:
            if num>0:
                res[p]=num
                p+=2
            else:
                res[n]=num
                n+=2
        return res

        