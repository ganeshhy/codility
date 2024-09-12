def tape(A):
    if len(A)<2:
        return 0
    s=sum(A)
    mindiff=3000
    si=0
    for i in range(0,len(A)-1):
        si+=A[i]
        diff=abs(2*si-s)
        mindiff=min(mindiff,diff)
    return mindiff
A=[10,20,30,50]
print(tape(A))