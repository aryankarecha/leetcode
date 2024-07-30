# def plusOne(digits):
#     rev_digits = digits[::-1]
#     carry = 1
#     for i in range(len(rev_digits)):
#         rev_digits[i] += carry
#         carry = 0
#         if rev_digits[i] == 10:
#             rev_digits[i] = 0
#             carry = 1
#         elif carry == 0:
#             break
#     if carry == 1:
#         rev_digits = rev_digits + [1]
#     return rev_digits[::-1]

def plusOne(digits):
    remainder = 1
    for i, val in enumerate(digits[::-1]):
        num = val+remainder
        digits[i], remainder = num%10, num//10
    if remainder > 0:
        digits = digits + [remainder]
    return digits[::-1]
        

print(plusOne([1,8,9,9,9]))
print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9,9]))
print(plusOne([9]))