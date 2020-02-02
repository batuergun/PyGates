import PyGates

lg = PyGates.Gates

number1 = input("Please write the first variable. \n-> ")

while number1 != "1" and number1 != "0":

    number1 = input("Please write the first variable in boolean format. \n-> ")
    if number1 == "1" or number1 == "0":
        break
    else:
        print("Input must be on boolean format.")

number2 = input("Please write the second variable \n-> ")
        
while number2 != "1" and number2 != "0":

    number2 = input("Please write the second variable in boolean format. \n-> ")
    if number2 == "1" or number2 == "0":
        break
    else:
        print("Input must be on boolean format.")


gate = input("Please choose logic gate: \n 1.AND \n 2.NAND \n 3.NOR \n 4.OR \n 5.XOR \n 6.XNOR \n ->")

        
print("The result is;")

number1 = int(number1)
number2 = int(number2)

if gate == "1":
    print(lg.AND(number1, number2))
elif gate == "2":
    print(lg.NAND(number1, number2))
elif gate == "3":
    print(lg.NOR(number1, number2))
elif gate == "4":
    print(lg.OR(number1, number2))
elif gate == "5":
    print(lg.XOR(number1, number2))
elif gate == "6":
    print(lg.XNOR(number1, number2))



