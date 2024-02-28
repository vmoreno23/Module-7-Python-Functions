def unique(list):

    new_list = [] #new list for elements to be stored

    for x in list:

        if x not in new_list:

            new_list.append(x)

    return new_list

list = [1, 3, 3, 3, 6, 2, 3, 5]

print(unique(list))

#Victor Moreno
#2/27/24

#Write a Python function that takes a list of numbers and returns a new list with unique elements of the first list.  Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.
