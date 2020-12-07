import re

def file_to_string(file_path):
    f = open(file_path, "r")
    string = f.read()
    f.close()
    return string

def split_on_empty_lines(string):
    return re.split(r"(?:\r?\n){2,}", string.strip())

def remove_newlines(splitted_string):
    newlist = []
    for i in splitted_string:
        i = re.sub("\n", " ", i)
        newlist.append(i)
    return newlist

def split_at_space(string):
    return string.split()

def find_letters(newlines_removed):
    amount_of_yes = []
    for i in newlines_removed:
        list_of_strings = split_at_space(i)
        letters_list = ["Yes"] * 26
        for j in list_of_strings:
            if "a" not in j:
                letters_list[0] = "No"
            if "b" not in j:
                letters_list[1] = "No"
            if "c" not in j:
                letters_list[2] = "No"
            if "d" not in j:
                letters_list[3] = "No"
            if "e" not in j:
                letters_list[4] = "No"
            if "f" not in j:
                letters_list[5] = "No"
            if "g" not in j:
                letters_list[6] = "No"
            if "h" not in j:
                letters_list[7] = "No"
            if "i" not in j:
                letters_list[8] = "No"
            if "j" not in j:
                letters_list[9] = "No"
            if "k" not in j:
                letters_list[10] = "No"
            if "l" not in j:
                letters_list[11] = "No"
            if "m" not in j:
                letters_list[12] = "No"
            if "n" not in j:
                letters_list[13] = "No"
            if "o" not in j:
                letters_list[14] = "No"
            if "p" not in j:
                letters_list[15] = "No"
            if "q" not in j:
                letters_list[16] = "No"
            if "r" not in j:
                letters_list[17] = "No"
            if "s" not in j:
                letters_list[18] = "No"
            if "t" not in j:
                letters_list[19] = "No"
            if "u" not in j:
                letters_list[20] = "No"
            if "v" not in j:
                letters_list[21] = "No"
            if "w" not in j:
                letters_list[22] = "No"
            if "x" not in j:
                letters_list[23] = "No"
            if "y" not in j:
                letters_list[24] = "No"
            if "z" not in j:
                letters_list[25] = "No"
        amount_of_yes.append(letters_list.count("Yes"))
    return amount_of_yes

def find_total_yes(amount_of_yes):
    total = 0
    for i in amount_of_yes:
        total = total + i
    return total

string = file_to_string("day6input.txt")
splitted_string = split_on_empty_lines(string)
newlines_removed = remove_newlines(splitted_string)
amount_of_yes = find_letters(newlines_removed)
total_yes = find_total_yes(amount_of_yes)
print(total_yes)
