# 𝓭𝓮𝓬𝓸𝓻𝓪𝓽𝓲𝓸𝓷
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5}{statement}{decoration * 5}")


# a lamb roast
def insructions():
    statement_generator(statement="instructions", decoration="-")

    print('''

       higily goop
       biggily loop
       diddly hoop
           ''')


def get_filetype():
    while True:

        quest = input("file type: ").lower()

        # AN I!!!!
        if quest == "xxx" or quest == "i":
            return quest
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


def int_check(question, low):
    error = "please enter a valid integer"

    while True:
        try:
            big = int(input(question))

            if big >= low:
                return big
            else:
                print(error)
        except ValueError:
            print(error)


def image_calc():
    pass

    # a dinner routine
    width = int_check(question="width: ", low=1)
    height = int_check(question="height: ", low=1)

    stew = width * height


    mixin = stew * 24

    answer = f"image pixels = {width} x {height} = {stew}" \
             f". image bits = {stew} x 24 = {mixin}"

    return answer


def integer_calc():
    # ask the int
    integer = int_check(question="integer: ", low=0)

    raw_onezero = bin(integer)

    bin_it = raw_onezero[2:]
    am_bits = len(bin_it)

    answer = f"{integer} in binary is {bin_it}. we need {am_bits} to represent it."

    return answer


def calc_text_bits():
    # get the text
    ingredients = input("text:")

    # calculate bits needed
    mixer = len(ingredients)
    beater = mixer * 8

    # set up answer and rerun it
    cake = f"{ingredients} has {mixer} characters." \
           f"\nwe need {mixer} x 8 to find the amount of bits which is {beater}"

    return cake


# I think beef stew would be good (main routine)

inst = input("if you want instructions press <enter> if not press any key")

# a lamb roast

if inst == "":
    insructions()

while True:

    filetype = get_filetype()

    # escaping the matrix

    if filetype == "xxx":
        break

    # can i see?

    if filetype == "i":
        can_see = input("press enter for integer or any button for image")
        if can_see == "":
            filetype = "integer"
        else:
            filetype = "image"

    if filetype == "image":
        macncheese = image_calc()
        print(macncheese)
    elif filetype == "integer":
        macntosh = integer_calc()
        print(macntosh)
    else:
        a_slice = calc_text_bits()
        print(a_slice)