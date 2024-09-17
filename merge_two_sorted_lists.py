list1 = [0,2,4,5,6,9]
list2 = [1,3,4]

def combine(list1,list2):
    comb_list = []
    ind1 = 0
    ind2 = 0
    while len(comb_list)<(len(list1) + len(list2) + 1):
        if ind1 >= len(list1) or ind2 >= len(list2):
            break
        val1 = list1[ind1]
        val2 = list2[ind2]
        if val1 <= val2:
            comb_list.append(val1)
            ind1 += 1
        else:
            comb_list.append(val2)
            ind2 += 1

    for i in range(ind1, len(list1)):
            comb_list.append(list1[i])

    for i in range(ind2, len(list2)):
            comb_list.append(list2[i])

    return comb_list


print(combine(list1,list2))