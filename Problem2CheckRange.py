def checkRange(user_num):

    if user_num in range(1,10):
        print("Number is in range")
    else:
        print("Number is not in range")

user_num = int(input("Enter a number to check if its in range: "))

checkRange(user_num)

#Victor Moreno
#2/27/24

#Write a Python function to check whether a number is in a given range. Use range(1,10). Print whether the number is in or not in the range.
