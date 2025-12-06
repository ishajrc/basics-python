def longest(nums):
    nums = sorted(set(nums))
    long = 1
    current = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current+= 1
        else:
            long= max(long, current)
            current = 1
    return long
arr = [100, 4, 200, 1, 3, 2]
print(longest(arr))
