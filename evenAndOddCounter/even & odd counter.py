# This program is meant to count the numbers you enter then divide them into two sectors
# EVEN & ODD numbers...

number = input("Enter a positive number (or press Enter key to finish: ): ")

evenCounter = 0
oddCounter = 0

if number == "":
    print("No positive number was entered.")
else:
    while number != "":
        if int(number) % 2 == 0:
            evenCounter = evenCounter + 1
            number = input("Enter a positive number (or press Enter key to finish: ): ")
        else:
            oddCounter = oddCounter + 1
            number = input("Enter a positive number (or press Enter key to finish: ): ")
    print("You entered ", oddCounter, " odd and ", evenCounter, " even numbers")

# -------------------------------------------
# ------------------[DONE]-------------------
# -------------------------------------------
