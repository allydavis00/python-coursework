# ==============================================================================
# PROGRAM Conversions
#
# AUTHOR: Allyson Davis
# FSU MAIL NAME: aed18c
# RECITATION SECTION NUMBER: 8
# RECITATION INSTRUCTOR NAME: Kevin Yee
# CGS 3465 - Spring 2021
# PROJECT NUMBER: 3
# DUE DATE: 2/17/2021
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# This program asks the user to enter the command and an English unit of
# measurement, and convert the measurement to its equivalent in Metric units.
#
# INPUT
#
# All input is interactive.  The user inputs a command, and a numeric value for
# the measurement they want to convert. The program must allow the user to
# enter menu commands and numbers to convert, until they choose to stop. 
#
# OUTPUT
#
# The program prints an output menu to tell the user what the commands are and
# what they mean. Prompts and error messages are printed as needed and the
# results of the conversion that was performed.
#
# ASSUMPTIONS
#
# We assume that the user enters a valid number when asked for a number.
#
# ==============================================================================

# create constant variables - conversion fractions
INCH_TO_CENT = 2.5400
FEET_TO_METER = 0.3048
MILE_TO_KILOMETER = 1.6094
LBS_TO_KILOGRAM = 0.4536
GAL_TO_LITER = 3.7853

# create other variables
choice = 1
inputNum = 0
convertedNum = 0

# print intro program output heading and program instructions
print('Welcome to the Amazing Conversion Program!\n')

print('Please choose an option from the menu below for the type of \nconversion you wish to perform. Then enter a non-negative \nnumber and it will be converted for you. Choose the last \nmenu option (6) to quit.\n')

# print menu options
while (choice != 6):
    print('Choose a number from the menu.')
    print('1. Inhces to centimeters')
    print('2. Feet to meters')
    print('3. Miles to kilometers')
    print('4. Pounds to kilograms')
    print('5. Gallons to liters')
    print('6. Quit the program\n')

    # prompt for choice and get input
    choice = int(input('Enter your choice: '))
    
    # loop to determine if input choice is valid
    while (not(choice >=1 and choice <=6)):
        choice = int(input('\nPlease enter a choice from the menu above: '))

    # loops to get choice & do calculations
    if (choice == 1):
        # if choice is 1: convert INCHES to CENTIMETERS
        inputNum = float(input('\nPlease enter the length in inches: '))

        while (inputNum < 0):
            # check if input is valid
            print('This program does not convert negative values.')
            inputNum = float(input('Please enter the length in inches: '))
        
        convertedNum = inputNum * INCH_TO_CENT

        if (inputNum == 1):
            print(f'{inputNum:.3f} inch is equivalent to {convertedNum:.3f} centimeters.\n')
        else:
            print(f'{inputNum:.3f} inches is equivalent to {convertedNum:.3f} centimeters.\n')

    elif (choice == 2):
        # if choice is 2: convert FEET to METERS
        inputNum = float(input('\nPlease enter the length in feet: '))

        while (inputNum < 0):
            # check if input is valid
            print('\nThis program does not convert negative values.')
            inputNum = float(input('Please enter the length in feet: '))
        
        convertedNum = inputNum * FEET_TO_METER

        if(inputNum == 1):
            print(f'{inputNum:.3f} foot is equivalent to {convertedNum:.3f} meters.\n')
        else:
            print(f'{inputNum:.3f} feet is equivalent to {convertedNum:.3f} meters.\n')
        
    elif (choice == 3):
        # if choice is 3: convert MILES to KILOMETERS
        inputNum = float(input('\nPlease enter the distance in miles: '))

        while (inputNum < 0):
            # check if input is valid
            print('This program does not convert negative values.')
            inputNum = float(input('Please enter the distance in miles: '))
        
        convertedNum = inputNum * MILE_TO_KILOMETER

        if(inputNum == 1):
            print(f'{inputNum:.3f} mile is equivalent to {convertedNum:.3f} kilometers.\n')
        else:
            print(f'{inputNum:.3f} miles is equivalent to {convertedNum:.3f} kilometers.\n')

    elif (choice == 4):
        # if choice is 4: convert POUNDS to KILOGRAMS
        inputNum = float(input('\nPlease enter the weight in pounds: '))

        while (inputNum < 0):
            # check if input is valid
            print('This program does not convert negative values.')
            inputNum = float(input('Please enter the weight in pounds: '))
        
        convertedNum = inputNum * LBS_TO_KILOGRAM

        if(inputNum == 1):
            print(f'{inputNum:.3f} pound is equivalent to {convertedNum:.3f} kilograms.\n')
        else:
            print(f'{inputNum:.3f} pounds is equivalent to {convertedNum:.3f} kilograms.\n')

    elif (choice == 5):
        # if choice is 5: convert GALLONS to LITERS
        inputNum = float(input('\nPlease enter the volume in gallons: '))

        while (inputNum < 0):
            # check if input is valid
            print('This program does not convert negative values.')
            inputNum = float(input('Please enter the volume in gallons: '))
        
        convertedNum = inputNum * GAL_TO_LITER

        if(inputNum == 1):
            print(f'{inputNum:.3f} gallon is equivalent to {convertedNum:.3f} liters.\n')
        else:
            print(f'{inputNum:.3f} gallons is equivalent to {convertedNum:.3f} liters.\n')

    else:
        # if choice is 6, exit the loop
        break

# print exit statment
print('\nThank you for using the Amazing Conversion Program!')

    
