# Elizabeth Fuller
# Exam 2
# 4/13/2020

# import statements
import random
from Search_Methods import bubble_sort
from Search_Methods import selection_sort
from Search_Methods import insertion_sort
from Search_Methods import merge_sort
from Search_Methods import quick_sort

# using method to allow for looping
def letsSort(list):
 # ask what method user wants
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
        return
    # ask how many numbers in list
    print("How many random integers do you want in the list?")
    num = int(input("> "))
    # add random numbers to list
    x = 0
    for x in range(num):
        number = random.randint(1, 10000)
        list.append(number)
        x = x + 1

    #send list to sort method
    if choice == 1:
        list = bubble_sort(list)
    elif choice == 2:
        list = selection_sort(list)
    elif choice == 3:
        list = insertion_sort(list)
    elif choice == 4:
        list = merge_sort(list)
    elif choice == 5:
        list = quick_sort(list)
    #print list
    print(list)
    print()
    #clear list
    list.clear()

    #loop back to start
    letsSort(list)

# create list and call method
newList = []
letsSort(newList)
