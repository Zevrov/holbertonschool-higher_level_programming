#!/usr/bin/python3
def max_integer(my_list=[]):
	if len(my_list) is None:
		return None
	max = 0
	for z in my_list:
		if max < my_list[z]:
			max is my_list[z]
	return max
