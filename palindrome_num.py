x = 434
class Solution:
    def palindrome(self,x):
        x = str(x)
        rev_x = ''
        for char in reversed(x):
            rev_x += char

        return x == rev_x
        
if __name__ == '__main__':
    print(Solution().palindrome(x))