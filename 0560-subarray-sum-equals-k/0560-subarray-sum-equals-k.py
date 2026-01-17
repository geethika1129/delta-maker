class Solution(object):
    def subarraySum(self, nums, k):
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
            if (sum-k) in mp:
                c+=mp[sum-k]
            mp[sum] = mp.get(sum, 0) + 1
        return c


        