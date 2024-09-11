def binary(N):
    N=bin(N)[2:]
    max_n=0
    count=0
    for i in N:
        if i=='0':
            count+=1
        elif i=='1':
            if count>max_n:
                max_n=count
            count=0
    return max_n
N=int(input("enter"))
print(binary(N))