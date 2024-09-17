nums1 = []
m = 1 
nums2 = [2]
n = 0

def comb_list(nums1,m,nums2,n):
    nums1 = nums1[0:m]
    nums2 = nums2[0:n]
    ind1 = 0
    ind2 = 0
    while ind2 < len(nums2):
        if ind1 >= len(nums1):
            nums1.append(nums2[ind2])
            ind2 += 1
        elif nums2[ind2] <= nums1[ind1]:
            nums1.insert(ind1,nums2[ind2])
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1
        
    return nums1
        

print(comb_list(nums1,m,nums2,n))