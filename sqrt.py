x = 626

# def mySqrtusingmethods(x):
#     import math
#     return math.floor(math.sqrt(x))
    
# print(mySqrt(x))

# def mySqrt(x):
#     diff = x
#     odd = 1
#     diff = diff - odd
#     count = 1
#     while True:
#         if diff > 0:
#             odd += 2
#             diff -= odd
#             count += 1
#         elif diff == 0:
#             return count
#         else:
#             return count - 1
            

# print(mySqrt(x))

def mySqrt(x):
    if x == 0:
        return 0
    
    left, right = 1, x
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        
        if mid_squared == x:
            return mid
        elif mid_squared < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result

print(mySqrt(x))