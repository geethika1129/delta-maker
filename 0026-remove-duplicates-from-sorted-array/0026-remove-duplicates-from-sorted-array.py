class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        for h in range(1,len(nums)):
            if(nums[h]!=nums[l]):
                l+=1
                nums[l]=nums[h]
        return l+1
        