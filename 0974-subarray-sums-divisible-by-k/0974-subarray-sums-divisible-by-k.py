class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        mp={0:1}
        sum=0
        for num in nums:
            sum+=num
            rem=sum%k
            if rem in mp:
                c+=mp[rem]
            mp[rem]=mp.get(rem,0)+1
        return c            
        