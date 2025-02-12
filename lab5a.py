#!/usr/bin/env python3
# Author ID: ssachdeva25

def read_file_string(file_name):
    
    file = open(file_name, 'r')
    return file.read()
    


def read_file_list(file_name):
    
    
    file = open(file_name, 'r')
    return [line.strip() for line in file.readlines()]
    
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
