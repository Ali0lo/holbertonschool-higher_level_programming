#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):\n    for key in sorted(a_dictionary):\n        print("{}: {}".format(key, a_dictionary[key]))
