from functools import reduce
def realmain():
    scores = []
    while 1 == 1: 
        try:
            scores.append(int(input("Enter a score to have the average computed of. If you would not like to enter another score, simply press enter.: ")))
        except ValueError:
            break
    avg = 0 if len(scores) == 0 else reduce(lambda z, a:z+a, scores) / len(scores)
    print("The average score is: ", avg)

def main():
    while 1 == 1:
        realmain()
        again = input("Would you like to calculate another class? [y/n]: ").lower()
        if again == "n":
            break
main()