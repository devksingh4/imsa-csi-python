# Dev Singh, 04/04/2020, einstein.py
def get_input():
    number = 0
    try:
        number = int(input("What is the number you would like to play with?: "))
    except ValueError as e:  #tries to run some code in the try block, and if the code doesn't work, then run the except block
        print(e)
        print("Invalid Input")
        number = get_input()
    try:
        rval = list(map(lambda x: int(x), list(str(number)))) # lambda and map allow me to run a function and set the return value to the new value of the list element.
    except ValueError:
        rval = number
    return rval 
def main():
    print("""Welcome to the Albert Einstien program. \nIt is said that Albert Einstein used to take great delight in baffling friends with the puzzle below. \n I guarantee to you that I will turn any 3 digit number that you provide me within the constraints into the number 1089.  \n The number you provide me must: \n - be a 3 digit number \n - have the first and list digits differ by at least 2 \n Lets play! \n""")
    num0 = []
    int_num = 0
    while True:  
        num0 = get_input()  
        if (len(num0) == 3 and abs(num0[0] - num0[2]) > 1):  
            break  # breaks out of the while loop to go to the next line.
        else: 
            print("Invalid Input")
    int_num = int("".join(map(str, num0)))
    print("Your number is: ", int_num)
    int_num_reverse = int("".join(map(str, list(reversed(num0)))))
    print("The reverse of your number is: ", int_num_reverse)
    inter1 = list(map(lambda x: int(x), list(str(abs(int_num - int_num_reverse))))) # interim as map -> list
    inter1_num = int("".join(map(str, inter1))) # join the array into one number
    print("The difference between the entered number and the reversed number is ", inter1_num)
    inter1_num_reverse = int("".join(map(str, list(reversed(inter1))))) # join the array into one number
    print("The reversed difference is ", inter1_num_reverse)
    output = inter1_num + inter1_num_reverse
    print("The reversed difference and the difference added together is ", output)
    if (input("Type exit to quit, or press enter to play the game again: ").lower() != "exit"):
        main()
main()