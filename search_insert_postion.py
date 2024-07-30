nums = [1,3,5,6]
target = int(input('Enter target val : '))

def searchInsert(nums,target):
    for ind in range(len(nums)):
        if nums[ind] >= target:
            return ind
    return len(nums)


print(searchInsert(nums,target))