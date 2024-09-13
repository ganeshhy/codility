def rotation(num,k):
    if len(num)==0:
        return num
    k=k%len(num)
    return num[k:]+num[:k]
num=[1,2,3,4,5]
k=int(input())
print(rotation(num,k))
