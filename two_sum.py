def two_sum(nums, target):
    for i, iel in enumerate(nums):
        for j, jel in enumerate(nums[i+1:]):
            if iel+jel == target:
                return [i, i+j+1]
    return []

nums = [3,3]
target = 6
print(two_sum(nums, target))