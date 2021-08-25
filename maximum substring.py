class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=-1
        for k in range(len(nums)):
            if nums[k]>0:
                i=k
                break
        if i==-1:
            return max(nums)
        f=0
        max1=0
        while i<len(nums):
            if nums[i]>0 and f<0:
                f=nums[i]
            else:
                f=f+nums[i]
            if f>max1:
                max1=f
            i=i+1
        return max1
            
