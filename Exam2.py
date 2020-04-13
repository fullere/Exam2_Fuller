# Elizabeth Fuller
# Exam 2

#import random
newList = []
cont = True
while cont is True:
 # ask what method use wants
    print("""How would you like to sort the list:
Bubble Sort [1]
Selection Sort [2]
Insertion Sort [3]
Merge Sort [4]
Quick Sort [5]
Quit [6]
""")
    choice = input("> ")
    choice = int(choice)
    # check choice for quit option
    if choice == 6:
        print("Quiting")
    # ask how many numbers in list
    print("How many random integers do you want in the list?")
    num = int(input("> "))
    # add random numbers to list
    for num in newList:


    # send list to sort method
    #print list
    #clear list
    #loop back to start

