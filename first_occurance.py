haystack = "leetcode"
needle = "leeto"


def strStr(haystack,needle):
    count = 0
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1

print(strStr(haystack,needle))