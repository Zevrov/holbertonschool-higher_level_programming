#!/usr/bin/python3


class Base:
	def __init__(self, id=None):
	__nb_objects = 0
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = base.__nb_objects
