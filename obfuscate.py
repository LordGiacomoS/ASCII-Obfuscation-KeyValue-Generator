class Obfuscate:
#* defines a class within this file, allowing me to make the key-value set variable ('dict') non-callable outside of the class, by adding the prefix of 'self.__'.

# Combined with making the variable non-callable outside of the class, compiling this file will limit access to the key-value set used to obfuscate strings to only those who have enough skill/experience to either decompile the python file manually or competently consult google to figure out how.
    
    def __init__(self):
        self.__dict = {
          " ": "c",
          "!": "T",
          "\"": "8",
          "#": "{",
          "$": "y",
          "%": "#",
          "&": "M",
          "'": ";",
          "(": "V",
          ")": " ",
          "*": "j",
          "+": "u",
          ",": "`",
          "-": "'",
          ".": "@",
          "/": "5",
          "0": "L",
          "1": "F",
          "2": "-",
          "3": "w",
          "4": "1",
          "5": "l",
          "6": "t",
          "7": "/",
          "8": "^",
          "9": "U",
          ":": "4",
          ";": ">",
          "<": "K",
          "=": "(",
          ">": "6",
          "?": "b",
          "@": "=",
          "A": "v",
          "B": "I",
          "C": "2",
          "D": "N",
          "E": "k",
          "F": "g",
          "G": "?",
          "H": "e",
          "I": "Y",
          "J": "a",
          "K": "B",
          "L": "q",
          "M": "~",
          "N": "[",
          "O": "H",
          "P": "]",
          "Q": "3",
          "R": "+",
          "S": "|",
          "T": "&",
          "U": "7",
          "V": ".",
          "W": "!",
          "X": ",",
          "Y": "}",
          "Z": "i",
          "[": "m",
          "\\": "S",
          "]": "f",
          "^": "d",
          "_": ":",
          "`": "J",
          "a": "p",
          "b": "X",
          "c": "r",
          "d": "h",
          "e": ")",
          "f": "Q",
          "g": "G",
          "h": "o",
          "i": "O",
          "j": "x",
          "k": "%",
          "l": "Z",
          "m": "<",
          "n": "P",
          "o": "\\",
          "p": "n",
          "q": "R",
          "r": "_",
          "s": "\"",
          "t": "*",
          "u": "D",
          "v": "0",
          "w": "E",
          "x": "A",
          "y": "9",
          "z": "W",
          "{": "z",
          "|": "$",
          "}": "C",
          "~": "s"
        }
    
# Alternatively, if you want to directly import a json file as the key, removing the security that compiling the file provides as the key-value set is not hidden, you could do:
    """
    def __init__(self):
        import json
        with open("cipher_key.json") as f:
            cipher_key = json.load(f)
        self.__dict = cipher_key
    """
    
  
    def obfuscate(self, string=""):
        """Obfuscates the provided string, using the substitution cipher set in __init__.
        
        Args:
            string (str): The string to obfuscate.
            
        Returns:
            str: An obfuscated version of the string.
        """

        if string == "" or string == None:
            raise ValueError("Please provide a string to obfuscate.")
          
        obfuscated_list = []
        chars = [char for char in string]

        for i in chars:
            if i in self.__dict.keys():
                new = self.__dict[i]
            else:
                new = i
            obfuscated_list.append(new)
        obfuscated_str = ''.join(obfuscated_list)
        return obfuscated_str

    def deobfuscate(self, string=""):
        """Debfuscates the provided string, using the substitution cipher set in __init__.
        
        Args:
            string (str): The string to deobfuscate.
            
        Returns:
            str: A deobfuscated version of the string.
        """

        if string == "" or string == None:
            raise ValueError("Please provide a string to deobfuscate.")
        
        deobfuscated_list = []
        chars = [char for char in string]
      
        count = 0
        for i in chars:
            if i in self.__dict.values():
                for k, v in self.__dict.items():
                    if i == v:
                        new = k
            else:
                new = i
            count +=1
            deobfuscated_list.append(new)
        deobfuscated_str = ''.join(deobfuscated_list) 
        return deobfuscated_str