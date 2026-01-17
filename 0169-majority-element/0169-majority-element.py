class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n=len(nums)
        # c=Counter(nums)
        # for a in nums:
        #     if c[a]>n//2:
        #         return a
    
        c=0
        for i in range(len(nums)):
            if c==0:
                k=nums[i]
                c=1
            elif nums[i]==k:
                c+=1
            else:
                c-=1
        return k

        