num1 = 0
num2 = 0
sign = " "

while True:
    sign = input(
        "Enter the operator (+, -, / or *) that you wanna perform and if u wanna quit write 'q':\n"
    )
    num1 = int(input("Enter 1st number :\n"))
    num2 = int(input("Enter 2nd number :\n"))
    if sign == "+":
        ans = num1 + num2
        print("The sum of 2 numbers is", ans)
    elif sign == "-":
        ans = num1 - num2
        print("The subtraction of 2 numbers is", ans)

    elif sign == "*":
        ans = num1 * num2
        print("The multiplication of 2 numbers is", ans)

    elif sign == "/":
        ans = num1 / num2
        print("The division of 2 numbers is", ans)
    
    elif sign != "+" or sign != "-" or sign != "/" or sign != "*" or sign != "q":
        print("Please enter the correct sign")

    elif sign == "q":
        print("The calculator has been closed")
    break
