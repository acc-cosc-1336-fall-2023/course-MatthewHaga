def get_hamming_distance(dna1,dna2):
    hamming_distance = 0
    if len(dna1) != len(dna2):
        return "Invalid, both strings are not of equal length"
    else:
        for position in range(len(dna1)):
            if dna1[position] != dna2[position]:
                hamming_distance += 1
    return hamming_distance

def get_dna_complement(dna):
    verify = verify_if_dna(dna)
    if verify == "DNA":
        complement = dna.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
        reverse_complement = complement[::-1]
        reverse_complement = reverse_complement.upper()
        return reverse_complement
    else:
        return "This sequence is not a DNA strand"

def verify_if_dna(dna):
    count = 0
    if dna == "":
        return "This is not a DNA strand"
    for i in range(len(dna)):
        if(dna[i] == "A" or dna[i] == "G" or dna[i] == "C" or dna[i] == "T"):
            count += 1
    if count != len(dna):
        return "This is not a DNA strand"
    else:
        return "DNA"

def display_menu():
    print("1-Hamming Distance")
    print("2-DNA Reverse Complement")
    print("3-Exit")

def run_menu():
    display_menu()
    option = str(input("Select option 1, 2, or 3: "))
    while (option != "1" and option != "2" and option != "3"):
        option = str(input("Option is invalid. Please select option 1, 2, or 3: "))
    select_option(option)

def select_option(option):
    if option == "1":
        option_1()
    if option == "2":
        option_2()
    if option == "3":
        option_3()

def option_1():
    print("\nYou selected Option 1, Enter Two Strings of equal length to find the Hamming Distance: ")
    y = hamming_parameters()
    while y == "Invalid, both strings are not of equal length":
        print("These Two strings are not of equal length, please try again")
        y = hamming_parameters()
    print(f"\nThe Hamming Distance between these two strings is {y}.\n")
    try_again_option_1()

def option_2():
    print("\nYou have selected Option 2, Enter a valid DNA strand to find the reverse complement")
    DNA_strand = str(input("Enter your DNA strand: "))
    y= get_dna_complement(DNA_strand)
    while y == "This is not a DNA strand":
        print("This is not a valid DNA strand")
        DNA_strand = str(input("Please enter a valid DNA strand: "))
    y= get_dna_complement(DNA_strand)
    print(f"The reverse complement of {DNA_strand} is {y}")
    try_again_option_2()

def option_3():
    while True:
        exit = input("Are you sure you want to exit: y/n: ")
        if exit == "yes" or exit == "y" or exit == "Y" or exit == "YES":
            print("\nExiting Program\n")
            break
        elif exit == "no" or exit == "n" or exit == "N" or exit == "NO":
            run_menu()
        else:
            print("Please Enter y or n")

def hamming_parameters():
    dna1 = str(input("Enter your first string: "))
    dna2 = str(input("Enter your second string: "))
    y = get_hamming_distance(dna1,dna2)
    return y

def try_again_option_1():
    while True:
        x = str(input("Press 'y' if you would like to try again. Press 'n' to return to main menu, press 3 to exit: "))
        if x == "y" or x == "yes" or x == "Y" or x == "YES":
            option_1()
            break
        if x == "n" or x == "N" or x == "no" or x == "NO":
            print("Returning to main menu")
            run_menu()
            break
        if x == "3":
            option_3()
            break
        else:
            print("Please enter 'y' or 'n' or 3: ")

def try_again_option_2():
    while True:
        x = str(input("Press 'y' if you would like to try again. Press 'n' to return to the main menu. Press 3 to exit: "))
        if x == 'y' or x == "Y" or x == "yes" or x == "YES":
            option_2()
            break
        if x == "n" or x == "N" or x == "no" or x == "NO":
            print("Returning to main menu")
            run_menu()
            break
        if x == "3":
            option_3()
            break
        else:
            print("Please enter 'y' or 'n' or 3: ")