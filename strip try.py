filename = '/home/shiyanlou/test.txt'
file = open(filename)
for line in file:
	print(line, end = '')
	fileLine = line.split('=')
	print(fileLine)
	for element in fileLine:
		elementStr = str(element)
		print(elementStr.strip(' /n'))
