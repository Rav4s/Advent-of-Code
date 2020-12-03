def split_into_list(file_path):
    f = open(file_path, "r")
    list_of_lists = []
    for line in f:
        stripped_line = line.strip()
        stripped_line = str(stripped_line)
        line_list = stripped_line.split()
        list_of_lists.append(stripped_line)

    f.close()
    return(list_of_lists)

def multiply_each_line(list_of_lists, filepath2):
    f = open(filepath2, "w")
    for i in list_of_lists:
        f.write(i*35) # Just an arbitrary number so I could make sure it wouldn't hit the wall
        #f.write("\n")
    f.close()


def string_to_list_of_chars(string):
    return [char for char in string]

def find_trees_and_opens(list_of_chars):
    newlist = []
    for i in list_of_chars:
        if i == "#":
            newlist.append("Tree")
        elif i == ".":
            newlist.append("Open")
        else:
            print("An error occured. Sorry.")
            quit()
    return newlist

def three_right_one_down(list_of_trees_opens):
    newlist = []
    k = 0
    for i in list_of_trees_opens:
        try:
            newlist.append(list_of_trees_opens[k])
            k = k+1085
            k = k+3
        except:
            return newlist

list_of_lists = split_into_list("day3input.txt")
multiply_each_line(list_of_lists, "day3inputmultiplied.txt")
list_of_lists = split_into_list("day3inputmultiplied.txt")
list_as_string = "".join(list_of_lists)
list_of_chars = string_to_list_of_chars(list_as_string)
list_of_trees_opens = find_trees_and_opens(list_of_chars)
list_of_slope_encounters = three_right_one_down(list_of_trees_opens)
print(list_of_slope_encounters)
print(list_of_slope_encounters.count("Tree"))
