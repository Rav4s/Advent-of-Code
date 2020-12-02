import re

def split_into_list(file_path):
    f = open(file_path, "r")
    list_of_lists = []
    for line in f:
        stripped_line = line.strip()
        stripped_line = str(stripped_line)
        #line_list = stripped_line.split()
        list_of_lists.append(stripped_line)

    f.close()
    return(list_of_lists)

def get_numbers(list):
    nums = []
    for i in list:
        x = re.search("^([\S]+)", i).group(0)
        nums.append(x)
    return nums

def get_strings(list):
    strings = []
    for i in list:
        y = re.sub(r".*?(\w+)\s*$", r"\1", i)
        strings.append(y)
    return strings

def get_letters(list):
    letters = []
    for i in list:
        z = re.match("([^:]+)", i).group(0)
        z = z.split('.')[0].lstrip().split(' ')[1]
        letters.append(z)
    return letters

def find_positions(nums):
    pos1 = []
    pos2 = []
    for i in nums:
        splitted_nums = []
        splitted_nums = i.split('-')
        posx = int(splitted_nums[0])
        posy = int(splitted_nums[1])
        pos1.append(posx)
        pos2.append(posy)
    return pos1, pos2

def find_valids(strings, pos1, pos2, letters):
    j = 0
    valids = []
    for i in strings:
        string = strings[j]
        low_pos = pos1[j] - 1
        high_pos = pos2[j] - 1
        #print(string)
        #print([letters[j]])
        #print(string[low_pos])
        #print(string[high_pos])
        if string[low_pos] != string[high_pos]:
            if string[low_pos] == letters[j]:
                valids.append("Valid")
            elif string[high_pos] == letters[j]:
                valids.append("Valid")
            else:
                valids.append("Invalid")
        else:
            valids.append("Invalid")
        j = j+1
    return valids

list = split_into_list("day2input.txt")
nums = get_numbers(list)
letters = get_letters(list)
strings  = get_strings(list)
pos1, pos2 = find_positions(nums)
valids = find_valids(strings, pos1, pos2, letters)
print(valids)
print(valids.count("Valid"))
