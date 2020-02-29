def until_1st_space(string: str):
    for i in range(len(string)):
        if string[i] == " ":
            return string[:i]
    return string


def after_spaces(string: str):
    while string.startswith(" "):
        string = string[1:]
    return string


def after_1st_space(string: str):
    fst = until_1st_space(string)
    return after_spaces(string[len(fst):])


def keyOfValue(dic: dict, value):
    return list(dic.keys())[list(dic.values()).index(value)]