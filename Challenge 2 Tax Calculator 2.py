#! /usr/bin/env python3
  2 
  3 import sys
  4 
  5 rawList = sys.argv[1:]
  6 
  7 for arg in rawList:
  8         argList = arg.split(':')
  9 
 10         try:    
 11                 idNumber[i] = int(argList[0])
 12                 salaryAmount[i] = int(argList[1])
 13         except: 
 14                 print("Parameter Error")
 15         taxPart = salaryAmount * (1 - 0.165) - 3500
 16         
 17         if taxPart <= 1500:
 18                 tax = taxPart * 0.03
 19         elif 1500 < taxPart <= 4500:
 20                 tax = taxPart * 0.1 - 105
 21         elif 4500 < taxPart <= 9000:
 22                 tax = taxPart * 0.2 - 555
 23         elif 9000 < taxPart <= 35000:
 24                 tax = taxPart * 0.25 - 1005
 25         elif 35000 < taxPart <= 55000:
 26                 tax = taxPart * 0.3 - 2755
 27         elif 55000 < taxPart <= 80000: 
 28                 tax = taxPart * 0.35 - 5505
 29         else:
 30                 tax = taxPart * 0.45 - 13505
