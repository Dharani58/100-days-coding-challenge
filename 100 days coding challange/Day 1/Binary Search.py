def binary_search(l1,target):
    low=0
    high=len(l1)-1
    while low<=high:
        mid=low+(high-low)//2
        if l1[mid]==target:
            return mid
        elif l1[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

l1=list(map(int,input("Enter the elements:").split()))
target=int(input("Enter a target value:"))
result=binary_search(l1,target)
if result==-1:
    print("Element is not present in the given list")
else:
    print("Element is present at index",result)
