# ==============================================================================
# PROGRAM: Simple DNA Sequences
#
# AUTHOR: Allyson Davis
# FSU MAIL NAME: aed18c
# RECITATION SECTION NUMBER: 8
# RECITATION INSTRUCTOR NAME: Kevin Yee
# CGS 3465 - Spring 2021
# PROJECT NUMBER: 5
# DUE DATE: 3/24/2021
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# First, read in a DNA sequence from a file, and store it in a Python string or
# list. Note: we will keep our sequences very short, in comparison to DNA
# sequences in real life, to make programming and grading this project simpler.
# Print the sequence you read in, to show the contents read in from the file.
# This is your original DNA sequence. 
#
# INPUT
#
# This program asks the user to input the filename they wish to use. If the file
# does not open with the filename they entered, keep asking them for a filename
# until the file does open successfully.
#
# OUTPUT
#
# The program outputs the original DNA sequence. For each operation the user
# selects, be sure to ouput the appropriate function.
#
# ASSUMPTIONS
#
# Assume that data files are not empty, do contain one DNA sequence, and do not
# contain any data errors. 
#
# ==============================================================================

import random

# ==============================================================================
# GLOBAL CONSTANTS

# max number of mutations to be made in DNA strand
MAX_MUTATIONS = 5

# ==============================================================================
def main():
    choice = 0

    # get filename and object
    filename, infile = validateFilename()

    # read in original DNA sequence
    original = readFile(infile)
    
    print("Original Sequence Read from File: " + original + '\n')

    # loop prints menu and gets choice - 4 to exit program
    while(choice != 4):
        printMenu()
        choice = getInput()
        if(choice == 1):
            getComplement(original)
        elif(choice == 2):
            mutateStrand(original)
        elif(choice == 3):
            getSubstrand(original)

    # close file object
    infile.close()
    print("Finished")
# ==============================================================================
def validateFilename():
    # function prompts user for filename and keeps prompting until user
    # enters a valid filename
    # called by main

    fileNameNotValid = True
    filename = input("Please enter a file name: ")
    
    while fileNameNotValid:
        try:
            infile = open(filename, 'r')
            fileNameNotValid = False
            break
        except IOError:
            filename = input("Cannot open file. Enter a new file name: ")
            
    return filename, infile
# ==============================================================================
def readFile(file):
    # function reads in the DNA sequence from given file
    # called by main
    
    sequence = file.readline()
    sequence = sequence.rstrip('\n')
    return sequence
# ==============================================================================
def printMenu():
    # prints menu options - called by main
    print("Enter a number 1-4")
    print("1. Find the complement of the strand")
    print("2. Mutate the DNA strand")
    print("3. Find substrand within the strand")
    print("4. Quit")
# ==============================================================================
def getInput():
    # get user input and validate the input
    # called by main
    choice = 0
    
    while(not 1 <= choice <= 4):
        choice = int(input("Enter your choice: "))
        print("-=-=-=-=-=-\n")
        
        if(not 1 <= choice <= 4):
            print("Invalid Selection\n")
            printMenu()
        
    return choice
# ==============================================================================
def getComplement(sequence):
    # option 1 - called by main
    # prints the original and complement of the given DNA sequence
    # complements: A -> T  &  C -> G
    
    complement = ""

    original_size = len(sequence)
    i = 0
    while (i < original_size):
        if(sequence[i] == 'A'):
            complement += 'T'
        elif (sequence[i] == 'T'):
            complement += 'A'
        elif(sequence[i] == 'C'):
            complement += 'G'
        elif(sequence[i] == 'G'):
            complement += 'C'
        i = i + 1
            
    print("Original  :  " + sequence)
    print("Complement:  " + complement + '\n')
# ==============================================================================
def mutateStrand(sequence):
    # option 2 - called by main
    # prints mutated strand and original strand
    # mutated strand: select 5 random positions to put 'M' in the strand
    
    maxIndex = len(sequence) - 1
    i = 0
    randIndex = 0
    mutation = list(sequence)
    
    while (i < MAX_MUTATIONS):
        randIndex = random.randint(0, maxIndex)
        mutation[randIndex] = 'M'
        i = i + 1

    mutationStr = ''.join(mutation)
    print("Original:  " + sequence)
    print("Mutation:  " + mutationStr + '\n')
# ==============================================================================
def getSubstrand(sequence):
    # option 3 - called by main
    # prompts user for substring to be searched for
    # search for substrand: if found, print the index where found string starts
    
    print("Original:  " + sequence)
    substrand = input("Please enter substring: ")
    substrand = substrand.upper()
    
    index = sequence.find(substrand)

    if (index == -1):
        print("Substrand NOT Found.\n")
    else:
        print("Found At Index:  " + str(index) + '\n')
# ==============================================================================
# call to main function
main()
# ==============================================================================
