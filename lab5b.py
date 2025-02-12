#!/usr/bin/env python3
# Author ID: sambhav

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    f.close()
    return read_data
def read_file_list(file_name):
    a = open(file_name, 'r')
    read_data = a.read()
    nlist = read_data.split('\n')
    a.close
    new_list = []
    for lines in nlist:
        if lines != '':
            new_list.append(lines)
    return new_list
def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    b = open(file_name, 'a')
    b.write(str(string_of_lines))
    b.close()
def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    c = open(file_name, 'w')
    for item in list_of_lines:
        c.write(str(item) + '\n')
    c.close()
def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    t = open(file_name_read, 'r')
    w = open(file_name_write, 'w')
    linenum = 1
    read_datas = t.read()
    tlist = read_datas.split('\n')
    newlist = []
    for line in tlist:
        if line != '':
            newlist.append(str(linenum) + ':' + str(line))
        linenum += 1
    for listitem in newlist:
        w.write(str(listitem) + '\n')
    w.close()
    t.close()
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    print(append_file_string(file1, string1))
    print(read_file_string(file1))
    print(write_file_list(file2, list1))
    print(read_file_string(file2))
    print(copy_file_add_line_numbers(file2, file3))
    print(read_file_string(file3))