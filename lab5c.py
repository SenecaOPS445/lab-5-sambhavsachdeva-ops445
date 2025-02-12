#!/usr/bin/env python3
# Author ID: ssachdeva25

def add(number1, number2):
    
    try:
        result = float(number1) + float(number2)
        return result
    except (ValueError, TypeError) as e:
        return 'error: could not add numbers'

def read_file(filename):
    
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except (FileNotFoundError, IOError) as e:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                         # works
    print(add('10', 5))                       # works
    print(add('abc', 5))                      # exception
    print(read_file('seneca2.txt'))           # works
    print(read_file('file10000.txt'))         # exception
