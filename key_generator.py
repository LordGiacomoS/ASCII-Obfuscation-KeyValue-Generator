import json, random
#* imports the built-in python packages for handling json, and implementing randomness

def buildKeyValue(filename=None):
#* This character dictionary looks at the ASCII character code chart, and uses characters 32 through 126 out of the total range of 0 through 127. 
    char_dict = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

#* randomly generates a new cipher key-value set
    shuffled = random.sample(char_dict, len(char_dict))

    dict = {}

    for i in range(0, len(char_dict)):
        x = shuffled[i]
        y = char_dict[i]
        category = dict
        category[y] = x

      
#* saves the newly generated key-value set to a json file with the name specified by 'filename' argument. If the filename argument is left unspecified, it will default to "cipher_key.json"

    if filename == None:
        filename = "cipher_key"
    obj = json.dumps(dict, indent=2)
    with open(f"{filename}.json", "w") as f:
        f.write(obj)

def formatKV(format=None, tabs=None, filename=None, out_file=None):
    """Formats the key-value set in the specified file to look better when copy-pasted to define self.__dict in "obfuscate.py". (Not been thoroughly tested.)

    Args:
        format (str, optional): Desired output style. Defaults to "single_line". Choices are:
          - "single_line": has single key-value pair per line.
          - "block": puts all key-value pairs on same line, creating a block of them as IDE wraps text.

        tabs (int, optional): Desired number of tabs (with 2 spaces per tab) before each line. Defaults to 2.      
        filename (str, optional): The name of the file to reformat. Defaults to "cipher_key".
        out_file (str, optional): The name of the file to save the formatted file to. Defaults to whatever filename is set to.
    
    Raises:
        ValueError: Unknown option for 'format'.
        TypeError: Unexpected type for 'format'.
    """
#* Use caution when using this tool, as it can be used multiple times.
    if format == None:
        format = "single_line"
    if tabs == None:
        tabs = 2
    if filename == None:
        filename = "cipher_key"
    if out_file == None:
        out_file = filename

    tab = tabs*'  '
    formatted = []
    with open(f"{filename}.json", "r+") as f:
        lines = f.readlines()

    if format == "single_line":
        for line in lines:
            new = tab + line
            formatted.append(new)
        out = "".join(formatted)
    elif format == "block":
        formatted.append(tab)
        for line in lines:
            new = line.strip("[\n]|[ ]")
            formatted.append(new)
        out = ' '.join(formatted)
    elif type(format) == str:
        raise ValueError("Unknown option for 'format'.")
    else:
        raise TypeError(f"Unexpected type for 'format', expected 'str', got {type(format)}.")
      
    with open(f"{out_file}.json", "w") as f:
        f.write(out)