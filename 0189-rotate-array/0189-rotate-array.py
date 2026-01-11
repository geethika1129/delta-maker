class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        def rev(l,h):
            while l<h:
                nums[l],nums[h]=nums[h],nums[l]
                l+=1
                h-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)