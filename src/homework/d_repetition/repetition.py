def get_factorial(num):    
    if num == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return factorial


def sum_odd_numbers(num):
    sum_odd = 0
    start_number = 1

    while start_number <= num:
        if start_number % 2 != 0:
            sum_odd += start_number
        start_number += 1

    return sum_odd

def display_menu():
    print("Homework 3 Menu")
    print("1 - Factorial")
    print("2 - Sum Odd Numbers")
    print("3 - Exit")

def run_menu():
    display_menu()
    choice = input("Make your choice, 1, 2, or 3: ")
    run_menu_option(choice)

def run_menu_option(choice):
    if(choice == '1'):
        choice_1_selected()
    if(choice == '2'):
        choice_2_selected()
    if(choice == '3'):
        option_3_selected()
    if(choice != '1', '2', '3'):
        print("The option you input is not valid, Please select from 1-3: ")

        run_menu()

def choice_1_selected():
    num = 0
    while num < 1 or num > 9:
        while True:
            try:
                num = int(input("Enter a number ranging from 1 to 9: "))
                break
            except ValueError:
                print("Letters and symbols are not valid choices, please input a numerical choice that ranges from 1 to 9: ")

    factorial = get_factorial(num)
    print("The factorial of ",num,"is equal to: ",factorial)

    exit_menu()

def choice_2_selected():
    num = 0
    while num < 1 or num > 99:
        while True:
            try:
                num = int(input("Enter a numeric value that is greater then 0 and less than 100: "))
                break
            except ValueError:
                print("Letters and symbols are not valid choices, please input a numerical value that ranges from 1 to 99: ")
    sum = sum_odd_numbers(num)
    print("The sum of odd numbers for",num, "is:",sum)

    exit_menu()

def option_3_selected():
    while True:
        exit = input("Do you wish to continue?: Y or N: ")
        if exit == "n" or exit == "N":
            print("Exited Program")
            break
        elif exit == "y" or exit == "Y":
            run_menu()
            break
        else:
            print("Enter Y or N")

def exit_menu():
    while True:
        continued = input("Do you want to continue Y or N: ")
        if continued == "Y" or continued == 'y':
            run_menu()
            break
        if continued == "N" or continued == "n":
            print("Exiting Program")
            break
        else:
            print("Enter either Y or N")