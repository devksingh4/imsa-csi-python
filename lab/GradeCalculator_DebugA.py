#Learning Company
#Grade Calculator
#Spring 2020 (CSI Lab)
#Dev Singh edits
def directions():
     print("This is program will calculate your average test score")
     print("Note: This calculator will not be considering extra credit.")
     print("Only scores from 0 - 100 are accepted.")



def inputNumberTests():
     numTests = input("How many test scores do you want to average? ")
     while not(numTests.isdigit()) or int(numTests) < 0 or int(numTests) > 100:
          numTests = input("\nPlease enter a valid number of tests: ")

     return int(numTests)
                    
     
def validateInput(numScores):
     testScores = []
     for i in range(1, numScores + 1): # range does not include the last number, so go +1
          score = input("Enter test score " + str(i) + ": ") # convert to string
          while not(score.isdigit()) or float(score) < 0 or float(score) > 100:
                score = input("\nPlease enter a valid test " + str(i) + " score between 0 - 100: ")
          testScores.append(float(score))
     return testScores


def calculatePercent(scoreList, numTests):
     percent = (sum(scoreList) / numTests) # misspelled variable
     return percent # return the percent not the number of tests


def assignGrade(percent):
     if percent >= 90 and percent <= 100:
        return "an A"
     elif percent >= 80 and percent < 90: # fractional needs to match to a B
        return "a B"
     elif percent>= 70 and percent < 80:
        return "a C"

     elif percent >= 60 and percent < 70:
        return "a D"

     else:
        return "an F"


def main():
     directions()
     response = input("Would you like to calculate your grades? y/n ")
     response = response.lower() # not .lowercase(), just .lower()
     while response == "y":
          numTests = inputNumberTests()      
          scoreList = validateInput(numTests)
          percent = calculatePercent(scoreList, numTests)
          letterGrade = assignGrade(percent)
            
          print("Your earned", letterGrade, "with", "{:.2f}".format(percent),"%.") #truncate to two decimal points without introducing floating point errors. 
          print("---------------------------------------------------------------")
          response = input("Would you like to calculate your grades again? y/n ") # should assign to response and not to answer to finish

     input("Thank you for playing. Press enter key to end.") # you can't press any key, you have to press enter. 

main()