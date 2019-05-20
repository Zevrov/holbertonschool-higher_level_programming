#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
for x in my_list:
	try:
		print("{}".format(my_list[x]))
	except:
		pass
