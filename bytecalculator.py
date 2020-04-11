import re
from datetime import datetime
import sys


def calculate_byte_size(line):
    '''calculates and returns the total byte size '''
    temp_str_int=''
    for character in line[-2:0:-1]:
        if character.isdigit():
            temp_str_int=temp_str_int+character
            flag=True
        else:
            break

    temp_str_int=temp_str_int[::-1]
    if temp_str_int.isdigit():
        return int(temp_str_int)
    else:
        return 0


def verify(line):
    '''verifies the time condition'''
    match = re.search(':\d{2}:\d{2}:\d{2}',line)
    time_stamp= datetime.strptime(match.group(),':%H:%M:%S').time()

    match1 = re.search(':\d{2}:\d{2}:\d{2}', ':10:40:00')
    time_limit= datetime.strptime(match1.group(), ':%H:%M:%S').time()
    if time_stamp>time_limit:
        return True
    else:
        return False


def print_list(lines_list):
    '''prints the whole log on console'''
    for line in lines_list:
        print(line)


def operation(filename,mode):
    '''function which performs the whole operation and returns the byte size as per the rules'''
    with open(file=filename,mode=mode) as my_file:
        lines_list=my_file.readlines()
        if '\n' not in lines_list[len(lines_list)-1]:
            lines_list[len(lines_list)-1]=lines_list[len(lines_list)-1]+'\n'
        total_byte_size=0
        for line in lines_list:

            if 'phpMyAdmin' in line and verify(line):
                total_byte_size+=calculate_byte_size(line)
        print_list(lines_list)
        return total_byte_size












if __name__=='__main__':
    filename=sys.argv[1]
    mode='r+'
    total_byte_size=operation(filename,mode)
    print(f'Total Bytes = {total_byte_size}')
