#! usr/bin/env python3

import sys

rawList = sys.argv[1:]
salaryDict = {}

for arg in rawList:
        argList = arg.split(':')

        try:
                idNumber = int(argList[0])
                salaryAmount = int(argList[1]) 
        except: 
                print("Parameter Error")

        rawTaxPart = salaryAmount * (1 - 0.165) - 3500

        if rawTaxPart > 0:
        	taxPart = rawTaxPart
        else:
                taxPart = 0
 	
        if taxPart <= 1500: 
                tax = taxPart * 0.03
        elif 1500 < taxPart <= 4500:
                tax = taxPart * 0.1 - 105
        elif 4500 < taxPart <= 9000: 
                tax = taxPart * 0.2 - 555
        elif 9000 < taxPart <= 35000:
                tax = taxPart * 0.25 - 1005 
        elif 35000 < taxPart <= 55000:
                tax = taxPart * 0.3 - 2755
        elif 55000 < taxPart <= 80000:
                tax = taxPart * 0.35 - 5505 
        else:
                tax = taxPart * 0.45 - 13505
             
        salary = salaryAmount * (1 - 0.165) - tax
        salaryPrint = '{:.2f}'.format(salary)
        salaryDict[idNumber] = salaryPrint

for key, value in salaryDict.items():
        print(str(key) + ':' + str(value))
