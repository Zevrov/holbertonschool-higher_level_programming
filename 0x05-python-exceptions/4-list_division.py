#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for i in range(0, list_length):
        try:
            math = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            math = 0
        except ZeroDivisionError:
            print("division by 0")
            math = 0
        except (TypeError, ValueError):
            print("wrong type")
            math = 0
        finally:
            newList += [math]
    return (newList)
