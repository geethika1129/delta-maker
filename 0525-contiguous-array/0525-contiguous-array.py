class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp={0:-1}
        sum=0
        len=0
        for i,num in enumerate(nums):
            if num==0:
                num=-1
            sum+=num
            if sum in mp:
                len=max(len,i-mp[sum])
            else:
                mp[sum]=i
        return len


            
        