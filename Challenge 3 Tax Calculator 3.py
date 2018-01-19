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

arg = Args()

class Config(object):

	def __init__(self):
		self.config = self._read_config()

	def _read_config(self):
		config = {}

		try:
			with open(arg.configfile) as file：
				while True:
					fileLine = file.readline()
					if fileLine == None:
						break
					fileReplace = fileLine.replace(' ', '')
					fileDictList = fileReplace.split('=')
					config[fileDict[0]] = fileDict[1]
		except:
			print('Parameter Error')

class UserData(object):

	def __init__(self):
		self.userdata = self._read_users_data()

	def _read_users_data(self):
		userdata = []

		try:
			with open(arg.userfile) as file:
				while True:
					fileLine = file.readline()
				if fileLine == None:
					break
				i = 0
				fileTupleList = fileLine.split(',')
				userTuple = (fileTupleList[0], fileTupleList[1])
				userdata[i] = userTuple
				i += 1
		except:
			print('Parameter Error')

class IncomeTaxCalculator(object):
	
	def calc_for_all_userdata(self):
		
		

