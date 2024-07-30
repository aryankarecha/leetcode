# s = 'Hello World'
s = "   fly me   to   the moon  "
# s = 'Hello'

# def lengthOfLastWordusingmethods(s):
#     words = s.split()
#     return len(words[-1])

# print(lengthOfLastWordusingmethods(s))


def lengthOfLastWord(s):
    count = 0
    for char in s[::-1]:
        if char == ' ':
            if count > 0:
                break
        else:
            count += 1
    return count

print(lengthOfLastWord(s))