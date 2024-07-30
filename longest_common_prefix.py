# my_list = ['flower','flow','flight']
my_list = ['abc']

class Solution:
    def prefix(self,my_list):
        sub_str = ''
        pref = ''

        for char in my_list[0]:
            sub_str += char
            # if sub_str in my_list[1] and sub_str in my_list[2]:
            for elem in my_list:
                # if my_list[1].startswith(sub_str) and my_list[2].startswith(sub_str):
                if not elem.startswith(sub_str):
                    return pref
            pref = sub_str
        return sub_str

if __name__ == '__main__':
    print(Solution().prefix(my_list))