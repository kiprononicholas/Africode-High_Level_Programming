import calculator

operation = input()
if operation == "1":
    num1 = input("enter first code: ")
    num2 = input("enter second code: ")
    print("the sum is " + str(int(num1)+ int(num2)))
elif operation == "2":
    num1 = input("enter first code: ")
    num2 = input("enter second code: ")
    print("the diffrence is " + str(int(num1) - int(num2)))
elif  operation == "3":
    num1 = input("enter first code: ")
    num2 = input("enter second code: ")
    print("the product is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("enter first code: ")
    num2 = input("enter second code: ")
    print("the result is " + str(int(num1) / int(num2)))


else:
    print("ivalid entry")