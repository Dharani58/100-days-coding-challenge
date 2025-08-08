def delete_element_manual(arr, i):
    if not 0 <= i < len(arr):
        print("Index is out of bounds.")
        return arr
    new_arr = [None] * (len(arr) - 1)
    for j in range(i):
        new_arr[j] = arr[j]
    for j in range(i + 1, len(arr)):
        new_arr[j - 1] = arr[j]

    return new_arr

my_list = list(map(int,input("Enter the elements:").split()))
i = int(input("Enter the index number:"))

updated_list = delete_element_manual(my_list, i)
print(f"Original list: {my_list}")
print(f"List after deleting element at index {i}: {updated_list}")
