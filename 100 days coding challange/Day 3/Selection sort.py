def selection_sort(l1):
    n=len(l1)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if l1[j]<l1[min_index]:
                min_index=j
        l1[i],l1[min_index]=l1[min_index],l1[i]
    return l1
l1=list(map(int,input("Enter the elements:").split()))
print("Sorted Array:",selection_sort(l1))