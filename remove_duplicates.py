nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [0,0]
# nums = [0,1,1]
# nums = [0,1]
# nums = []

def removeDuplicates(nums):
    unique = nums.copy()
    nums.clear()
    ind = 0
    for el in unique:
        if el not in nums:
            nums.append(el)
    print(nums)
    return len(nums)

def removeDuplicatesByFirstPrinciples(nums):
    writeIdx = -1
    lastVal = None
    for readIdx in range(len(nums)):
        if nums[readIdx] != lastVal:
            writeIdx += 1
            lastVal = nums[readIdx]
            nums[writeIdx] = lastVal
    return writeIdx + 1

def removeDuplicatesQuickly(nums):
    return len(list(set(nums)))

print(removeDuplicatesQuickly(nums))