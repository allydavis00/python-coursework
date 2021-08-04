# ==============================================================================
# PROGRAM Software Sales
#
# AUTHOR: Allyson Davis
# FSU MAIL NAME: aed18c
# RECITATION SECTION NUMBER: 8
# RECITATION INSTRUCTOR NAME: Kevin Yee
# CGS 3465 - Spring 2021
# PROJECT NUMBER: 2
# DUE DATE: 2/3/2021
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# This program asks the user to enter the number of units sold (whole num) and
# calculates the total cost of the purchase. Output the cost per unit after the
# discount is calculated, as well as the total price of the whole sale.
#
# INPUT
#
# All input is interactive.  The user inputs the quantity as an integer. Make
# sure the number is greater than zero. If it is less than or equal to zero, do
# not calculate a discount or a cost, and exit the program
#
# OUTPUT
#
# The program prints an output title, echoprints the user's input in
# a readable fashion, and then prints out the calculated results.
#
# ASSUMPTIONS
#
# We assume that all input data is a valid integer and correctly entered by the user.
# The program is therefore not guaranteed to work correctly if bad data
# is entered.

# ==============================================================================

# create variables: name constants
UNIT_COST = 99.00 # package retail price
DISCOUNT_20 = 0.2
DISCOUNT_30 = 0.3
DISCOUNT_40 = 0.4
DISCOUNT_50 = 0.5

unitsSold = 0
discount = 0.0
discountedPrice = 0.0
totalCost = 0.0

# print introductory program output heading
print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('Welcome to the Software Sales Calculator')
print ('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

# read the quatity of units sold
unitsSold = int(input('How many units were sold? '))

# determine if greater than zero
if unitsSold > 0 :
    # determine discount amount based on units sold
    if (unitsSold >= 10 and unitsSold <= 19) :
        discount = DISCOUNT_20
    elif (unitsSold >= 20 and unitsSold <= 49) :
        discount = DISCOUNT_30
    elif (unitsSold >= 50 and unitsSold <= 99) :
        discount = DISCOUNT_40
    elif unitsSold >= 100 :
        discount = DISCOUNT_50

    # calculate and print effective cost per unit and total cost
    discountedPrice = UNIT_COST - (UNIT_COST * discount)
    totalCost = unitsSold * discountedPrice
    
    print ('Your effective cost per unit is $%.2f' % discountedPrice)
    print ('The total cost of the purchase is $%.2f' % totalCost)
    
else :
    # if input is bad data, print error message
    print('Units sold must be greater than zero. Ending program run.')

# print closing message
print ('\nExecution Terminated Normally')

# ==============================================================================
#                              END OF PROGRAM
# ==============================================================================
