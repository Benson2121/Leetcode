class Solution:
    def jump(self, nums: List[int]) -> int:
        k=0
        while len(nums)>1:
            big=0
            for i,num in enumerate(nums):
                if num>=len(nums)-1-i>big:
                    big=len(nums)-1-i
            k=k+1
            nums=nums[:-big]
        return s
        return k
