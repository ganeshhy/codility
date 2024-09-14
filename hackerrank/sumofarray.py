def sumarray(arr,s):
    arr.sort()
    left=0
    right=len(arr)-1
    while (left<=right):
        if arr[left]+arr[right]>s:
            right-=1
        elif arr[left]+arr[right]<s:
            left+=1
        elif arr[left]+arr[right]==s:
            print(arr[left],arr[right])
            right-=1
            left+=1
arr=[5,7,4,3,9,8,19,21]
s=17
sumarray(arr,s)