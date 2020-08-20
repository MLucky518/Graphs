lst = {
    "cat": "bob",
    "dog": 23,
    19: 18,
    90: "fish"
}


def dict_sum(data):
    sum = 0
    for val in data.values():
        if isinstance(val,int):
            sum += val

    return sum


print(dict_sum(lst))






