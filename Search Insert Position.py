class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target>nums[-1]:
            return len(nums)
        else:
            i=0
            while target>nums[i]:
                i=i+1
            return i
