# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:47:26 2024

@author: dell
"""

FILEPATH = "todos_item.txt"

def get_todos(filepath = FILEPATH):
    """
    Parameters
    ----------
    filepath : String TYPE , optional = No
        DESCRIPTION. The default is FILEPATH.
    
    Description: Read text file and return list of todo items

    Returns
    -------
    returns todos list

    """
    with open(filepath,'r') as lcl_file:
        lcl_todos = lcl_file.readlines()

    return lcl_todos

def write_todos(todos_arg, filepath=FILEPATH):
    """
    Parameters
    ----------
    todos_arg : TYPE
        DESCRIPTION.
    filepath : String TYPE, optional
        DESCRIPTION. The default is FILEPATH.
    Description: Write new todos in file.
    Returns
    -------
    None.

    """
    with open(filepath,'w') as lcl_file:
        lcl_file.writelines(todos_arg)
    
if __name__ == "__main__":
    print("Hello")
    