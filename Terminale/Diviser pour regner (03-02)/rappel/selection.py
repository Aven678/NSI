def tri_selection(lst):
    sussy = 0
    for i in range(len(lst)-1):
        j = i
        for k in range(i+1, len(lst)):
            sussy += 1
            if lst[k] < lst[j]:
                j = k

        lst[i], lst[j] = lst[j], lst[i]

    return lst, sussy