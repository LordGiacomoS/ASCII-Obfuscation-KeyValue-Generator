def chars_getter():
    with open("chars.txt") as f:
        contents = f.readlines()

    chars = []
    for line in contents:
        chars.append(line.strip())

    with open("chars_dict.txt", "w") as f:
        f.write(str(chars))