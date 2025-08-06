def insertion_sort(l1):
    n=len(l1)
    for i in range(1,n):
        key=l1[i]
        j=i-1
        while j>=0 and key<l1[j]:
            l1[j+1]=l1[j]
            j-=1
        l1[j+1]=key
    return l1
l1=list(map(int,input("Enter the elements:").split()))
print("Sorted Array:",insertion_sort(l1))