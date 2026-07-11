num = int(input("Enter the first number: "))
num1 = int(input("Enter the second number: "))

choice = input(" 1 for Add, 2 for Sub, 3 for Mult: ")

if choice == "1":
    print("Answer is", num + num1)
elif choice == "2":
    print("Answer is", num - num1)
elif choice == "3":
    print("Answer is", num * num1)
else:
    print("Error")


