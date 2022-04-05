#================================================
#     Key-Value Set Generation & Formatting
#================================================
import key_generator as kg
#* imports the module that contains the code to generate a new key-value set for the substitution cipher.

"""
kg.buildKeyValue(filename="cipher_key")
"""
#* the line of code used to create a new key-value set file. To specify a file name, replace the string in quotes to your desired file name.
"""
kg.formatKV(format="single_line", tabs=4, filename="cipher_key", out_file="out")
"""
#* calls the function formatKV() in "key_generator.py", which is used to add spaces before every line in the specified json file to make key-value set look neater when pasted into "obfuscate.py" and if specified, turn the character set into a text block.




#================================================
#         Obfuscation & Deobfuscation:
#================================================
import obfuscate
#* imports the module that contains the code for obfuscating and obfuscating strings based on a key-value set specified within the file.
"""
obf = obfuscate.Obfuscate()
"""
#* defines and loads the Obfuscate class, which is necessary to access the key-value set specified within "obfuscate.py".


#* Example code for obfuscating a string:
"""
string_to_obfuscate = "Example"
obfuscate_out = obf.obfuscate(string_to_obfuscate)
print(obfuscate_out)
"""

#* Example code for deobfuscating a string:
"""
string_to_deobfuscate = "kAp<nZ"
deobfuscate_out = obf.deobfuscate(string_to_deobfuscate)
print(deobfuscate_out)
"""



from Extra.ASCII_Char_Table import table_formatter as tf
tf.plaintext_table()

