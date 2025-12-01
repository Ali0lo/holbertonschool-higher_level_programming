#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            try:
                result = a / b
            except TypeError:
                print("wrong type")
                result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
