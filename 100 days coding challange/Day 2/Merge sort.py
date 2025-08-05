def merge_sort(l1):
    if len(l1) > 1:
        mid = len(l1) // 2
        left_half = l1[:mid]
        right_half = l1[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                l1[k] = left_half[i]
                i += 1
            else:
                l1[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            l1[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            l1[k] = right_half[j]
            j += 1
            k += 1

l1 = list(map(int,input("Enter the elements:").split()))
merge_sort(l1)
print("Sorted list elements:",l1)
