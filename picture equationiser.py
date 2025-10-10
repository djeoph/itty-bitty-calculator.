def int_check(question, low):
    error = "please enter a number that is over zero"

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
    height = int_check(question="integer: ", low=1)

    stew = width * height

    mixin = stew * 24

    answer = f"image pixels = {width} x {height} = {stew}" \
             f". image bits = {stew} x 24 = {mixin}"

    return answer


# second mate routine

macncheese = image_calc()

print(macncheese)
