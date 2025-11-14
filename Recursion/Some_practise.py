def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(4))

# Check array is Shorted or Not

def isSorted(arr,n):
    if n==0 or n==1:
        return True
    return arr[n-1]>=arr[n-2] and isSorted(arr,n-1)

print(isSorted([1,2,3,4,7,6],6))

# using recursion performing Binary serach

def BinSearch(arr,tar,st,end):
    mid= int(st+(end-st)/2)
    if st<=end:
     if arr[mid]==tar:
        return mid
     elif arr[mid]<tar:
        return BinSearch(arr,tar,mid+1,end)
     else :
        return BinSearch(arr,tar,st,mid-1)
    return -1

print(BinSearch([1,2,3,4,5,6,7,8,9,10],5,0,9))