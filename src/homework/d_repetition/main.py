#print(repetition.get_factorial(4))
#print(repetition.sum_odd_numbers(7))
#repetition.factorial_while_loop()
#repetition.sum_odd_numbers_loop()

exit_clause = 'EXIT'
confirmation = 'YES'
user_selection = '0'

while user_selection.upper() != exit_clause:
    user_selection = input(' Welcome to the Homework 3 Menu:\n  Press 1 for Factorial Analysis\n  Press 2 for Sum of Odd Numbers Analysis\n  Type EXIT to exit\n\t>>> ')

    if user_selection == '1':
        repetition.factorial_while_loop()
        user_selection = input(' Would you like to exit? Enter Yes, all other selections will return you to the menu.\n\t>>> ')
        user_selection = repetition.basic_exit_loop(user_selection)
    elif user_selection == '2':
        repetition.sum_odd_numbers_loop()
        user_selection = input(' Would you like to exit? Enter Yes, all other selections will return you to the menu.\n\t>>> ')
        user_selection = repetition.basic_exit_loop(user_selection)
    elif user_selection.isnumeric() and user_selection not in [1,2]:
        print(' Invalid Selection')
    elif user_selection.upper() != exit_clause and user_selection.upper() != exit_clause[0:1:1] and user_selection.upper() != exit_clause[0:2:1] and user_selection.upper() != exit_clause[0:3:1]:
        print(' Invalid Selection')
    else: user_selection = repetition.exit_loop(user_selection)

    import repetition

repetition.run_menu()