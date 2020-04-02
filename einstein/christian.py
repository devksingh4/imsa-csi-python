while 1 > 0: #Still can't just write while true
    num = input("\nIt is said that Albert Einstein used to take great delight in baffling friends with the puzzle below.\n\nFirst, write the number 1089 on a piece of paper, fold it, and hand it to a friend for safekeeping.\nWhat you wrote down is not to be read until you have completed your amazing mental feat.\nNext, ask your friend to write down any three-digit number, emphasizing that the first and last\ndigits must differ by at least two. Close your eyes or turn your back while this is being done.\nBetter still, have someone blindfold you.\n> Number: ")
    if num.isnumeric() and len(num) == 3 and int(num) > 0 and abs(int(num[0]) - int(num[2])) >= 2:
        break
    print("\n>>> Y'all didn't follow the rules or something")
reversed = num[2] + num[1] + num[0]
result = abs(int(reversed) - int(num))
reversed2 = str(result)[2] + str(result)[1] + str(result)[0]
print("\nAfter your friend has written down the three-digit number, ask him to reverse it, then subtract the\nsmaller from the larger.\n>", reversed if int(reversed) > int(num) else num, "-", num if int(reversed) > int(num) else reversed, "=", result,"\nNext ask your friend to add the new number and its reverse together.\n>", reversed2 if int(reversed2) > result else result, "+", result if int(reversed2) > result else reversed2, "=", result + int(reversed2))