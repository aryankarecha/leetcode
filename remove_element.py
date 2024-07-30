nums = [0,1,2,2,3,0,4,2]
val = int(input('Enter a value : '))

def removeElement(nums,val):
    unique = nums.copy()
    nums.clear()
    for el in unique:
        if el != val:
            nums.append(el)
    return len(nums)

print(removeElement(nums,val))

