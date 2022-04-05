import re, os

def plaintext_table():
    from prettytable import PrettyTable
    dir = "Extra/ASCII_Char_Table/"
    with open(f"{dir}ASCII_Characters.csv") as f:
        lines = f.readlines()

    saved_len_a = 0
    saved_len_b = 0
    saved_len_c = 0
    saved_len_d = 0
    saved_len_e = 0
    saved_len_f = 0

    PT = PrettyTable()
    count = 0
    for line in lines:
        if len(re.split(",(?!\")", line)) == 5:
            a, b, c, d, e = re.split(",(?!\")", line)
        elif len(re.split(",(?!\")", line)) == 6:
            a, b, c, d, e, f = re.split(",(?!\")", line)
    
        if len(a) > saved_len_a:
            saved_len_a = len(a)
          
        if len(b) > saved_len_b:
            saved_len_b = len(b)
          
        if len(c) > saved_len_c:
            saved_len_c = len(c)

        if len(d) > saved_len_d:
            saved_len_d = len(d)
        
        if len(e) > saved_len_e:
            saved_len_e = len(e)
          
        if len(f) > saved_len_f:
            saved_len_f = len(f)
      
        if count == 0:
            PT.field_names = [a, b, c, d, e, f]
        else:
            PT.add_row([a, b, c, d, e, f])

        count += 1

    print(f"A:{saved_len_a}, B:{saved_len_b}, C:{saved_len_c}, D:{saved_len_d}, E:{saved_len_e}, F:{saved_len_f}")
    PT._max_width = {"Dec" : 5, "Hex" : 5, "Binary" : 9, "HTML" : 10, "Char" : 13, "Description" : 26}
    with open(f"{dir}plaintext_table.txt", "w") as f:
        f.write(str(PT))