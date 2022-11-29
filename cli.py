import calc
import sys

totalArgs = len(sys.argv)
if totalArgs < 4 :
    print('Insufficient argumenets')
    exit
else:
    numA = int(sys.argv[2])
    numB = int(sys.argv[3])
    operationChoice = int(sys.argv[1])

    if operationChoice == 1:
        print(calc.add(numA, numB))
    
    elif operationChoice == 2:
        print(calc.multiply(numA, numB))
    
    elif operationChoice == 3:
        print(calc.subtract(numA, numB))
    
    elif operationChoice == 4:
        if numB == 0:
            print('Division by 0 - Not allowed')
        else:
            print(calc.divide(numA, numB))
    
    else:
        print('Inappropriate Operation Choice')