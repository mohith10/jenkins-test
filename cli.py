import calc


numA = int(input('Enter first number: '))
numB = int(input('Enter second number: '))
operationChoice = int(input('Enter operation choice - 1: Addition, 2: Multiply, 3: Subtraction, 4: Division: '))

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