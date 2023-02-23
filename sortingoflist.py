
def sorting(lst):
    for i in range(0,len(lst)-1):
        if lst[i][1]>lst[i+1][1]:
            temp=lst[i]
            lst[i]=lst[i+1]
            lst[i+1]=temp
    return lst
print(sorting([[20,88],[57,18],[65,26],[13,84]]))

