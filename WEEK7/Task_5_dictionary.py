def pattern () :
    data = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    return data


def display_keys (data) :
    for key in data.keys() :
        print(key)

def display_values (data) :
    for value in data.values() :
        print(value)


def display_items (data) :
    for keys, values in data.items() :
        print(f"{keys}:,{values}")

def run():
        data = pattern
        print (f"dictionary:\n{data}")
        display_keys(data)
        display_values(data)
        display_items(data)
run ()

