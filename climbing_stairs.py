import math
n = 5

def climbStairs(n):
    # x + 2y = n
    x = 0   # Number of ones
    y = 0   # Number of twos
    combinations = 0
    while x != n + 1:
        if (n-x)%2 == 0:
            y = (n - x)//2
            print('x :', x, 'y :', int(y))
            combinations += math.factorial(x+y)/(math.factorial(x)* math.factorial(y))
        x += 1
    return int(combinations)

print(-1, climbStairs(-1))
print(0, climbStairs(0))
print(1, climbStairs(1))
print(2, climbStairs(2))
print(3, climbStairs(3))
print(4, climbStairs(4))
print(11, climbStairs(11))