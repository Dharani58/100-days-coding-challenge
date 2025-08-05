def quick_sort(l1):
    if len(l1)<=1:
        return l1
    else:
        pivot=l1[len(l1)//2]
        left=[x for x in l1 if x < pivot]
        mid=[x for x in l1 if x == pivot]
        right=[x for x in l1 if x > pivot]
    return quick_sort(left)+mid+quick_sort(right)

l1=list(map(int,input("Enter the elements:").split()))
print("Sorted list Elements:",quick_sort(l1))