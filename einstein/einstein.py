# Dev Singh, 04/01/2020, Einstein program
def get_input():
    number = 0
    try:
        number = int(input("What is the number you would like to play with?: "))
    except:
        print("Invalid Input")
        get_input()
    return list(map(lambda x: int(x), list(str(number))))
def main():
    print("Welcome to the Albert Einstien program.")
    print("""
    It is said that Albert Einstein used to take great delight in baffling friends with the puzzle below.
    I guarantee to you that I will turn any 3 digit number that you provide me within the constraints into the number 1089. 
    The number you provide me must:
        - be a 3 digit number
        - have the first and list digits differ by at least 2
    Lets play!
    """)
    num0 = []
    int_num = 0
    while True:  
        num0 = get_input()  
        if(len(num0) == 3 and abs(num0[0] - num0[2]) > 1):  
            break  
        else: 
            print("Invalid Input")
    int_num = int("".join(map(str, num0)))
    print("Your number is: ", int_num)
    num0.reverse()
    int_num_reverse = int("".join(map(str, num0)))
    print("The reverse of your number is: ", int_num_reverse)
    inter1 = list(map(lambda x: int(x), list(str(abs(int_num - int_num_reverse))))) 
    inter1_num = int("".join(map(str, inter1)))
    print("The difference between the entered number and the reversed number is ", inter1_num)
    inter1.reverse()
    inter1_num_reverse = int("".join(map(str, inter1)))
    print("The reversed difference is ", inter1_num_reverse)
    output = inter1_num + inter1_num_reverse
    print("The reversed difference and the difference added together is ", output)
main()