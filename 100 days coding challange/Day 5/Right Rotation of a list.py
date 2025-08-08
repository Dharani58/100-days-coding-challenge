def right_rotate_manual(arr, n):
    if not arr:
        return []
    n = n % len(arr)
    new_arr = [None] * len(arr)
    for i in range(len(arr)):
        new_index = (i + n) % len(arr)
        new_arr[new_index] = arr[i]
    return new_arr
my_list = list(map(int,input("Enter the elements:").split()))
n = int(input("No of rotation:"))
rotated_list = right_rotate_manual(my_list, n)
print(f"Original list: {my_list}")
print(f"List after {n} right rotations: {rotated_list}")