class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)<20:
            for i in range(1,20):
                if i not in nums:
                    return i
        nums.sort()
        nums=list(set(nums))
        if 1 not in nums:
            return 1
        nums=nums[nums.index(1):]
        if nums[-1]==len(nums):
            return nums[-1]+1
        for i in range(1,len(nums)):
            if nums[i]!=i+1:
                return i+1
