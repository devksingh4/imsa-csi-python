# Dev Singh, 04/06/2020, Functions/Chain assignment
import sys # so that I can exit the script easily
def chain(startnum):
    """Runs the code for option 1"""
    anum = -1 
    final = [startnum]
    retstr = ""
    while anum != 1:
        anum = (startnum // 2) if startnum % 2 == 0 else ((startnum * 3) + 1) # set first number if the first staement is true, else set the second number
        final.append(anum)
        startnum = anum # run it in a chain
    for item in final:
        retstr = retstr + str(item) + " - "
    return len(final), retstr[:-3] # remove the last 3 characters since they are the chain indicator, but the last number does not chain to anything. 
def opt2(low, high):
    """Runs the code for option 2"""
    far = [] # list to store to the lens
    z = list(range(low, high)) # create an iterable in the range of numbers provided
    for i in z:
        far.append(chain(i)[0]) # runs the chain for each number within the parameter range
    return max(far), far.index(max(far)) + low  # return the max number and the number which causes it
def askContinue():
    """Ask the user if they would like to continue to play"""
    se = False if input("Would you like to play again? [y/n]: ").lower() == "n" else True
    if not se: 
        sys.exit(0) # exit the program
    else:
        main()
def main(): 
    play = True if input("We are going to practice writing functions. You will need to give me a number, please. Would you like to help me learn about functions? y/n: ").lower() == "y" else False
    if play:
        which_one = 1 if str(input("please enter 1 to find a chain for a number or 2 to the find the longest chain: ").lower()) == "1" else 2
    else:
        sys.exit(128) # exit the program with UNIX error code for invalid input
    if which_one == 1:
        num0 = 0
        while type(num0) == type(1):  # "can't just do while True" meh meh meh and could technically change
            try:
                num0 = int(input("Please enter a number between 1 and 100, inclusive: "))
            except:
                num0 = 500000 # idk that should cause it to trigger invalid input.
            if num0 > 0 and num0 < 101:  
                break  # breaks out of the while loop to go to the next line.
            else: 
                print("Invalid Input.")
        print(chain(num0)[1] + "\n" + "Your chain is " + str(chain(num0)[0]) + " numbers long")
        askContinue() # ask the user
    elif which_one == 2: 
        low = int(input("please enter the lower bound (inclusive): "))
        high = int(input("please enter the higher bound (inclusive): "))
        rval = opt2(low, high + 1)
        print("The highest chain within the range you provided is the chain of " + str(rval[1]) + " with a length of " + str(rval[0]))
        askContinue()
    else: 
        print("Invalid Option")
        main()

main()