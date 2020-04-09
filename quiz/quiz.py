from functools import reduce
def main():
    scores = []
    while 1 == 1: 
        try:
            scores.append(int(input("Enter a score to have the average computed of. If you would not like to enter another score, simply press enter.: ")))
        except ValueError:
            break
    avg = 0 if len(scores) == 0 else reduce(lambda z, a:z+a, scores) / len(scores)
    print("The average score is: ", avg)

main()