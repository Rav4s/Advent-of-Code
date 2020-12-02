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

def find_occurences(strings, letters):
    j = 0
    number_of_occurences = []
    for i in strings:
        corresponding_letter = letters[j]
        k = i.count(corresponding_letter)
        number_of_occurences.append(k)
        j = j+1
    return number_of_occurences

def find_max_min(nums):
    mins = []
    maxes = []
    for i in nums:
        splitted_nums = []
        splitted_nums = i.split('-')
        min = int(splitted_nums[0])
        max = int(splitted_nums[1])
        mins.append(min)
        maxes.append(max)
    return mins, maxes

def compare_occurences(number_of_occurences, mins, maxes):
    j = 0
    valids = []
    for i in number_of_occurences:
        min = mins[j]
        max = maxes[j]
        j = j+1
        if min <= i and max >= i:
            valids.append("Valid")
        else:
            valids.append("Invalid")
    return valids

list = split_into_list("day2input.txt")
nums = get_numbers(list)
letters = get_letters(list)
strings  = get_strings(list)
number_of_occurences = find_occurences(strings, letters)
mins, maxes = find_max_min(nums)
valids = compare_occurences(number_of_occurences, mins, maxes)
print(valids)
print(valids.count("Valid"))
