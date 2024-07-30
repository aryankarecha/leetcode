# def combine_all(lists):
#     comb_list = []
#     for l in lists:
#         for 
# print(combine(list1,list2))

# print(combine_all([[1,2,3,4],[0,2,2,3],[5],[3,4,7,8,9]]))

# def combine_all(lists):

# pointers = []
# low = lists[0][0]
# sort_list = []
# while 
# for l in lists:
#     n = 0
#     pointers.append(n)
#     if l[0]<low:
#         low = l[0]
#         n += 1
#         pointers[lists.index(l)] = n
    
# sort_list.append(low)
        
# print(pointers)
# print(low)
# print(sort_list)

def combine_all(lists):
    combined = []
    pointers = [0 for l in lists]
    while True:
        lowVal = None
        lowIndex = None
        for i, l in enumerate(lists):
            if pointers[i] < len(l):
                if lowVal == None or l[pointers[i]] < lowVal:
                    lowVal = l[pointers[i]]
                    lowIndex = i
        if lowVal == None:
            break
        combined.append(lowVal)
        pointers[lowIndex] += 1
    return combined

lists = [[3,4,5,9],[2,7,8],[1,2,3]]
# print(combine_all(lists))
# print(combine_all([[1,2,3,4],[],[0,2,2,3],[5],[3,4,7,8,9]]))
print(combine_all([]))