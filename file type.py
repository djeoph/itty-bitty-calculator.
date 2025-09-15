


def get_filetype():

    while True:

        quest = input("file type: ").lower()

     # AN I!!!!
        if quest == "xxx" or quest == "i":
            return  quest
    # no it's an integer
        elif quest in ['integer', 'int']:
             return "integer"
    # playin wordle
        elif quest in ['text', 'txt', 't']:
            return "text"
    # i can see, every thing
        elif quest in ['image', 'picture', 'img', 'p']:
            return "image"
    # INCORRECT
        else:
            print("please enter a valid file type")


#I think beef stew would be good (main routine)

while True:

    filetype = get_filetype()

    #breaking the loop

    if filetype == "xxx":
        break

# can i see?

    if filetype == "i":
        can_see = input("press anter for integer or any button for image")
        if can_see == "":
            filetype = "integer"
        else:
            filetype = "image"

#eating with eyes

    print(f"file type: {filetype}")


