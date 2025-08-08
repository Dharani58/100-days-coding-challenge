def insert_element_manual(arr, x, y):
    new_arr = [None] * (len(arr) + 1)
    for i in range(y):
        new_arr[i] = arr[i]
    new_arr[y] = x
    for i in range(y, len(arr)):
        new_arr[i + 1] = arr[i]

    return new_arr

my_list = list(map(int,input("Enter the elements:").split()))
x = int(input("Enter a value:"))
y = int(input("Enter the index number:"))

updated_list = insert_element_manual(my_list, x, y)
print(f"Original list: {my_list}")
print(f"List after inserting {x} at index {y}: {updated_list}")