import ipdb
def is_isogram(string):
    original_length = len(string)
    string_array = string.lower().split()
    
    ipdb.set_trace()
    
    unique_length = len(string_array)
    return original_length == unique_length
print(is_isogram("Odion"))

# ///////////////////////////////////////////////

def yell_greeting(string):
    name = string
    ipdb.set_trace()
    name = name.upper()
    greeting = f"WASSAP, {name}!"
    print(greeting)
yell_greeting("bob")