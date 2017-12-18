#! usr/bin/env python3

import sys

print(sys.argv)

for i in sys.argu:
        print(i)

try:
        salary = int(sys.argu[1])
except:
        print("Parameter Error")

taxPart = salary - 3500

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
        
taxPrint = format(tax, ".2f")

print(taxPrint)
