import time

def split_into_list(file_path):
    f = open(file_path, "r")
    list_of_lists = []
    for line in f:
        stripped_line = line.strip()
        stripped_line = int(float(stripped_line))
        #line_list = stripped_line.split()
        list_of_lists.append(stripped_line)

    f.close()
    return(list_of_lists)

def add_to_each(list_of_terms, num1, num2):
    j = 0
    for i in list_of_terms:
        #print(i)
        try:
            k = j+1
            #print(k)
            l = list_of_terms[k]
            #print(l)
            j=j+1
            total = 0
            total += list_of_terms[num1]+list_of_terms[num2]+l
            #print(list_of_terms[num1])
            #print(list_of_terms[num2])
            #print(l)
            print(total)
            if (total) == 2020:
                print("equal")
                newlist = []
                newlist.append(list_of_terms[num1])
                newlist.append(list_of_terms[num2])
                newlist.append(l)
                return newlist
            else:
                print("not equal")
        except IndexError:
            print("done")

def iterate_list(list_of_terms):
    for i in range(len(list_of_terms)):
        for j in range(len(list_of_terms)):
            newlist = add_to_each(list_of_terms, i, j)
            print(newlist)
            if newlist != None:
                return newlist
            else:
                continue

list_of_terms = split_into_list("day1input.txt")

answer_nums = iterate_list(list_of_terms)
print(answer_nums)
final_answer = (answer_nums[0]*answer_nums[1]*answer_nums[2])
print(final_answer)
