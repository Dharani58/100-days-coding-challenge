def linear_search(l1,target):
    for i in range(len(l1)):
        if l1[i]==target:
            return i
    return -1

l1=list(map(int,input("Enter elements:").split()))
target=int(input("Enter a value:"))

result=linear_search(l1,target)
if result==-1:
    print("Target value is not present in the given list")
else:
    print("Target value is present at index ",result)