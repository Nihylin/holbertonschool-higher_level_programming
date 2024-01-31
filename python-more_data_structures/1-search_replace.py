#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = [replace if idx == search else idx for idx in my_list]
    return result
