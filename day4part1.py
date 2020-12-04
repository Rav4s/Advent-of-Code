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
        i = i.replace('\r', '').replace('\n', '')
        newlist.append(i)
    return newlist

def compare_j_value(j):
    if j == 7:
        return "Valid"
    else:
        return "Invalid"

def find_attributes(newlines_removed):
    newlist = []
    for i in newlines_removed:
        j = 0
        if "byr:" in i:
            j = j + 1
        if "iyr:" in i:
            j = j + 1
        if "eyr:" in i:
            j = j + 1
        if "hgt:" in i:
            j = j + 1
        if "hcl:" in i:
            j = j + 1
        if "ecl:" in i:
            j = j + 1
        if "pid:" in i:
            j = j + 1
        newlist.append(compare_j_value(j))
    return newlist

string = file_to_string("day4input.txt")
splitted_string = split_on_empty_lines(string)
newlines_removed = remove_newlines(splitted_string)
list_of_valids_invalids = find_attributes(newlines_removed)
print(list_of_valids_invalids)
print(list_of_valids_invalids.count("Valid"))
