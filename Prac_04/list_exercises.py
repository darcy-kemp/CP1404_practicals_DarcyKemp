"""CP1404 | prac_04 list exercises | Darcy Kemp
list exercises
"""
def main():
    numbers = []

    for i in range(0, 5):
        user_number = int(input("Enter a number"))
        numbers.append(user_number)

    print(f"the first number is: {numbers[1]}")
    print(f"the last number is: {numbers[-1]}")
    print(f"the smallest number is: {min(numbers)}")
    print(f"the largest number is: {max(numbers)}")
    print(f"the average of the numbers is: {sum(numbers)/len(numbers)}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("please input your username")

    if username in usernames:
        print("access granted")
    else:
        print("access denied")

main()
