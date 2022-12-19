'''Returns a sorted, lowercase list'''
import os

def sort_file(file):
    '''Sorts .txt file alphabetically'''
    file_list = open(file, 'r', encoding = 'utf-8', errors = 'ignore').read().splitlines()
    file_list = [line.strip() for line in file_list]
    file_list = list(set(file_list)) # Gets rid of duplicates
    file_list.sort(key = str.casefold) # Sorts alphabetically

    with open(file, 'w', encoding = 'utf-8', errors = 'ignore') as txt_file:
        txt_file.write('\n'.join(file_list))
    txt_file.close()

    return file + ' is sorted.'

def get_list_lower(file):
    '''Returns lowercase list'''
    list_normal = open(file, 'r', encoding = 'utf-8', errors = 'ignore').read().splitlines()
    list_lower = [string.lower() for string in list_normal] # Makes all items lowercase
    return list_lower

os.system('cls')

sort_file('twitterFilter.txt')

with open('twitter_filter.py', 'w', encoding = 'utf-8', errors = 'ignore') as py_file:
        py_file.write('blocked_phrase_lower = ' + str(get_list_lower('twitterFilter.txt')))
py_file.close()