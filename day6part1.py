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
        letters_list = [None] * 26
        for j in list_of_strings:
            if "a" in j:
                letters_list[0] = "Yes"
            if "b" in j:
                letters_list[1] = "Yes"
            if "c" in j:
                letters_list[2] = "Yes"
            if "d" in j:
                letters_list[3] = "Yes"
            if "e" in j:
                letters_list[4] = "Yes"
            if "f" in j:
                letters_list[5] = "Yes"
            if "g" in j:
                letters_list[6] = "Yes"
            if "h" in j:
                letters_list[7] = "Yes"
            if "i" in j:
                letters_list[8] = "Yes"
            if "j" in j:
                letters_list[9] = "Yes"
            if "k" in j:
                letters_list[10] = "Yes"
            if "l" in j:
                letters_list[11] = "Yes"
            if "m" in j:
                letters_list[12] = "Yes"
            if "n" in j:
                letters_list[13] = "Yes"
            if "o" in j:
                letters_list[14] = "Yes"
            if "p" in j:
                letters_list[15] = "Yes"
            if "q" in j:
                letters_list[16] = "Yes"
            if "r" in j:
                letters_list[17] = "Yes"
            if "s" in j:
                letters_list[18] = "Yes"
            if "t" in j:
                letters_list[19] = "Yes"
            if "u" in j:
                letters_list[20] = "Yes"
            if "v" in j:
                letters_list[21] = "Yes"
            if "w" in j:
                letters_list[22] = "Yes"
            if "x" in j:
                letters_list[23] = "Yes"
            if "y" in j:
                letters_list[24] = "Yes"
            if "z" in j:
                letters_list[25] = "Yes"
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
