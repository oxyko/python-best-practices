'''
Examples of neat printing features and formatting of the code
'''
import pprint

def print_stuff():

    # Print list of items, one on separate line
    some_list = {'aasd', 'some item 2', 3}
    print("Printing a list with one element on each line:")
    print(*some_list, sep='\n')

def pretty_print():
    some_list = {'aasd', 'some item 2', 3}
    print("Pretty printing a list:")
    pprint.pprint(some_list)


if __name__ == "__main__":
    print_stuff()
    pretty_print()