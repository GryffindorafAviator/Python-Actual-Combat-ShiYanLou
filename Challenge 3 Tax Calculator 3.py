#! usr/bin/env python3

class Config:

	def __init__(self, configfile):
		self._config = {}
		with open(configfile) as file:
			for line in file：
				fileLine = line.split('=')
				print(fileLine)
				i = 0
				
				for elem in fileLine:
					elemStr = str(elem)
					if i = 0:
						dictKey = elem.strip( /n)
						i += 1
					else:
						dictValue = elem
				
				self._config[dictKey] = dictValue
