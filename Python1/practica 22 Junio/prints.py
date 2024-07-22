def is_isogram(string):
    original_length = len(string)
    string_array = string.lower()
    print(string_array)
    unique_length = len(set(string_array))
    return original_length == unique_length
print(is_isogram("Odin"))