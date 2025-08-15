def remove_duplicates_inplace(char_list):
    if not char_list:
        return 0
    write_ptr = 0
    seen = set()
    for read_ptr in range(len(char_list)):
        current_char = char_list[read_ptr]
        if current_char not in seen:
            seen.add(current_char)
            char_list[write_ptr] = current_char
            write_ptr += 1
    return write_ptr

input_str = "programming is fun"
char_array = list(input_str)
print(f"Original list: {char_array}")

new_length = remove_duplicates_inplace(char_array)
print(f"New length: {new_length}")

unique_chars = char_array[:new_length]
print(f"List after removing duplicates: {unique_chars}")
print(f"Result as a string: '{''.join(unique_chars)}'")