filename = '/home/shiyanlou/test.txt'
file = open(filename)

configDict = {}

for line in file:
	print(line, end = '')
	fileLine = line.split('=')
	print(fileLine)
	i = 0
	for element in fileLine:
		elemStr = str(element)
		if i == 0:
			dictKey = elemStr.strip(' \n')
			i += 1
		else:
			dictValue = elemStr.strip(' \n')
	configDict[dictKey] = dictValue

print(configDict)

file.close()
