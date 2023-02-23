def sumdict(d):
    sum=0
    for i,v in d.items():
        sum=sum+int(v)
    return sum
d={"a":2, "b":3, "c":5}
print(sumdict(d))
