#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    for i in range(x):
	try:
	    print("{}".format(my_list[i]), end="")
	    index += 1
	except:
	    break
    print()
    return(index)
