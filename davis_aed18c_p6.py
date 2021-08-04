# ==============================================================================
# PROGRAM: Contacts Class Objects List
#
# AUTHOR: Allyson Davis
# FSU MAIL NAME: aed18c
# RECITATION SECTION NUMBER: 8
# RECITATION INSTRUCTOR NAME: Kevin Yee
# CGS 3465 - Spring 2021
# PROJECT NUMBER: 6
# DUE DATE: 4/7/2021
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# Create a contact class that can hold information and perform operations with
# contact objects. Contact class has private data members and methods that
# allow other functions to alter and access these values. This program creates
# a list of 5 contacts and initializes them to default values. Then, it reads
# in contact data from a file and revises the initialized contacts list with
# relavent information.
#
# INPUT
#
# Input is from the data file. The first line of the file is the number of
# contacts in the file. Each item of contact data is given on one line in the
# file. 
#
# OUTPUT
#
# Program outputs an introduction, echo-printed input, closing termination
# message, error messages as needed, and any info messages the user may need.
# Program will print out the number of actual contacts provided in the file and
# the data for each contact. Only print contact data for the part that has
# meaningful contact information (may be fewer than 5).
#
# ASSUMPTIONS
#
# Assume that file data is completely correct and no error checking has to be
# done on the file. Assume that the number of contacts specified in the file is
# an integer between 1 and 5.
#
# ==============================================================================
# GLOBAL CONSTANTS
UNAV_STR = "unavailable"
MAX_CONTACTS = 5

# CONTACTS CLASS
class Contacts:
    # should include __init__, __str__, and methods to get/set name, address,
    # age, phone, and type

    # __init__ method
    def __init__(self):
        self.__name = UNAV_STR
        self.__address = UNAV_STR
        self.__phone = UNAV_STR
        self.__age = 0
        self.__type = "NONE"

    # set methods
    def set_name(self, n):
        self.__name = n

    def set_address(self, a):
        self.__address = a

    def set_age(self, a):
        self.__age = a

    def set_phone(self, p):
        self.__phone = p

    def set_type(self, t):
        self.__type = t

    # get methods
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    def get_type(self):
        return self.__type

    # __str__ method
    def __str__(self):
        return (f'{self.__name}\nAddress: {self.__address}\nAge: {self.__age}\nPhone: {self.__phone}\nType: {self.__type}\n')
        
# ==============================================================================
# MAIN FUNCTION
def main():
    printHeader()

    # create a list of class objects that stores 5 contacts initialized
    # by initializer method
    contacts_list = [Contacts(), Contacts(), Contacts(), Contacts(), Contacts()]

    # print values for all data membets of the objects in list
    for i in contacts_list:
        print (i)

    # open data file & read in first line containing num contacts
    infile = openFile()
    numContacts = getNumContacts(infile)
    
    # read contacts data
    i = 0
    while(i < numContacts):
        n, ad, a, p,t = getContact(infile)
        contacts_list[i].set_name(n)
        contacts_list[i].set_address(ad)
        contacts_list[i].set_age(a)
        contacts_list[i].set_phone(p)
        contacts_list[i].set_type(t)
        print (contacts_list[i])
        i += 1
            
    infile.close()
    printCloser()
# ==============================================================================
def printHeader():
    # prints program header and information
    
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("           CONTACTS")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    print("This program creates a list of 5 contacts and initializes them to")
    print("default values.\nThen, it reads in contact data from a file and")
    print("revises the initialized contacts list with relavent information.\n")

    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("      Initialized Contacts")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
# ==============================================================================
def printCloser():
    # prints any closing termination messages

    print("Thank you for using the Contacts Program! - Goodbye!")
# ==============================================================================
def getContact(file):
    # reads in each data item for the contacts in the file and returns
    # them to the main function
    
    name = (file.readline()).rstrip('\n')
    address = (file.readline()).rstrip('\n')
    age = (file.readline()).rstrip('\n')
    age = int(age)
    phone = (file.readline()).rstrip('\n')
    t = (file.readline()).rstrip('\n')
    
    return name, address, age, phone, t
# ==============================================================================    
def openFile():
    # opens given file and throws an exception if file cannot ne opened
    # called by main
    
    filename = 'contacts.txt'

    try:
        infile = open(filename, 'r')
    except IOError:
        print(f'\nAn error occurred trying to read the file \'{filename}\'\n')

    return infile
# ==============================================================================
def getNumContacts(file):
    # reads in the first number from the file & print to screen
    
    num = (file.readline()).rstrip('\n')
    num = int(num)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print(f'  Number of Contacts in File: {num}')
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
    
    return num
# ==============================================================================
main()
# ==============================================================================
