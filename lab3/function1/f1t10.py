def uniq(lst):
    list = []
    for i in lst:
        if i not in list: 
            list.append(i) 
    return list

n = list(map(int, input().split()))
print(uniq(n))
