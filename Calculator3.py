#! usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv # used to input csv file

# processing command line parameters class

class Args(object):

	def __init__(self):
		try:
			self.args = sys.argv[1:]
			index_config = args.index('-c')
			self.configfile = args[index_config + 1]
			index_user = args.index('-d')
			self.userfile = args[index_user + 1]
			index_salary = args.index('-o')
			self.salaryfile = args[index_salary + 1]
		except:
			print('Parameter Error')

class Config(object):

	def __init__(self):
		self.config = self._read_config()

	def _read_config(self):
		config = {}
		arg = Args()
		with open(arg.configfile)
