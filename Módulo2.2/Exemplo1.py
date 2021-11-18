def my_split(string)
    split_string = []
    s = ""
    for i in range(len(string)):
        if string[i] != " ":
            s = s + string[i]
        else:
            if s != "":
                slipt_string.append(s)
            s = ""
    return split_string