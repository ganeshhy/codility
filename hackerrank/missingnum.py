def missingnumber(num):
    a=num[-1]
    su=(a*(a+1))//2
    val=su-sum(num)
    return val
num=[1,2,4,5,6,7]
print(missingnumber(num))