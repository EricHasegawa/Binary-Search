def binarySearch():
    while True : # Ensures user input is an integer 
        try:
            target = int(input("Enter an integer: "))
            break
        except ValueError:
            print("You did not enter an integer , try again.")
            
    numberlist = open('numberlist.txt') #allows program to open text document       
    split_list = numberlist.read().split(", ") #reads through the text, splitting each number into a separate string
    print(split_list, "HELLO")
    results = list(map(int, split_list)) # converts the list of strings into a list of integers
    sorted_results = sorted(results) # sorts results low to high
        
    high = len(sorted_results) - 1 # Sets the top parameter of the loop to the highest elem. in the array 
    low = 0 # Sets low value to zero 

    while (high > low): # Checks list to detect if the user selected target is present
        middle = ((high + low)//2) 
        if (target == sorted_results[middle]) : 
            print ("Target found")
            break
        elif (middle == low)  :
            print ("Target not found") 
            break
        elif (target > sorted_results[middle]) :
            low = middle
        elif (target < sorted_results[middle]) :
            high = middle

    while True : # Allows the user to optionally test for another value
        yn = input("Would you like to test another number? (y/n): ")
        if (yn == 'y'):
            binarySearch()
            break
        elif (yn == 'n') :
            print("Roger Dodger")
            break
        else :
            print("You did not enter y or n, try again.") 

binarySearch() 
