def longestConsecutive(nums):
    nums = sorted(list(set(nums)))
    longest = 1
    temp_long = 1
    i=0
    print(nums)
    for i in range(len(nums)-1):
        if nums[i+1]==nums[i]+1:
            temp_long = temp_long + 1
            print(longest)
        else:
            if temp_long > longest:
                longest = temp_long
            temp_long = 1
    return longest
print(longestConsecutive([100,4,200,1,3,2]))
