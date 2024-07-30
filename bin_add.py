# a = "11"
# b = "1"
# num_1 = 0
# num_2 = 0
# for ind,val in enumerate(a[::-1]):
#    num_1 += int(val)*(2**ind) 

# for ind,val in enumerate(b[::-1]):
#     num_2 += int(val)*(2**ind)

# print(num_1)
# print(num_2)

# dec_sum = num_1 + num_2
# print(dec_sum)

# floor = dec_sum//2
# rem = dec_sum%2

# def bin_add_using_methods(a,b):
#     import builtins
#     num_1 = int(a,2)
#     num_2 = int(b,2)
#     # for ind,val in enumerate(a[::-1]):
#     #     num_1 += int(val)*(2**ind) 

#     # for ind,val in enumerate(b[::-1]):
#     #     num_2 += int(val)*(2**ind)

#     dec_sum = num_1 + num_2
#     bin_sum = str(bin(dec_sum)[2::])
#     return bin_sum

# print(bin_add_using_methods(a,b))
a = "1010"
b = "1011"

def addBinary(a,b):
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2

    return ''.join(reversed(s))

print(addBinary(a,b))

