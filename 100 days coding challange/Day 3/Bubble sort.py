def bubble_sort(l1):
    n=len(l1)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if l1[j]>l1[j+1]:
                l1[j],l1[j+1]=l1[j+1],l1[j]
                swapped=True
        if not swapped:
            break
    return l1
l1=list(map(int,input("Enter the elements:").split()))
print("Sorted Array : ",bubble_sort(l1))