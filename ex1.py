# Dev Singh 3/26/2020 Ex. 1
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
def get_input(input_string): 
    """Function that allows me to get the user input and force them to provide a number within the appropriate bounds. """
    response  = ""
    try:
        response = float(input(input_string)) # try to convert to float
    except:
        print("Please provide a valid input") # if it cant, then something must be wrong with the input. prompt the user to give me better input. 
        get_input(input_string)
    return response # return the value for assignment to variable. 

# %%
def createHeader(ordinal):
    """Creates the header text for each seperate subexcercise"""
    print("")
    print("---", ordinal, " program---")
    print("")
    return 0
# %%
createHeader("First")
userInput = get_input("What is the temperature in F: ") # get the input
tempC = round((userInput - 32) * (5/9),2) # convert to C, round to 2 decimal places
print("The temperature in degrees C is: ", tempC) # give user the output

# %% 
createHeader("Second")
print(
"""
    \\    |    /
       @    @ 
         *
       \\\"""/
"""
)
# %%
createHeader("Third")
def get_str_input(input_string): 
    """Function that allows me to get the user input and force them to provide a string within the appropriate bounds. """
    response  = ""
    try:
        response = input(input_string) # try to convert to float
    except:
        print("Please provide a valid input") # if it cant, then something must be wrong with the input. prompt the user to give me better input. 
        get_input(input_string)
    return response # return the value for assignment to variable. 
userColor = get_str_input("What is your favorite color?: ")
lenColor = len(userColor)
space = " " + (" " * lenColor)
print((userColor + " ") * 10)
print(userColor + space * 8 + " " + userColor) # substitute color with same length spaces
print(userColor + space * 8 + " " + userColor) # substitute color with same length spaces
print((userColor + " ") * 10)

# %%
createHeader("Fourth")
userResp = get_str_input("Do you like Python?: ") # use the same function i defined above
if userResp.lower() == "yes":
    print("That is great!")
elif userResp.lower() == "no":
    print("That is disappointing!")
else: 
    print("That is not an answer to my question.")
