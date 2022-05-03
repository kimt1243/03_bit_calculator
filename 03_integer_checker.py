#checks input is a number more tham zero
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter a integer that is more than " "(or equal to) {}".format(low)
      

        try:

            response = int(input(question))

            if response >= low:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)


#Main Routine goes here


keep_going =""
while keep_going == "": 
    print()
    # ask user for an integer (must be more than / qual to 0)
    var_integer = num_check("Enter an integer: ", 0)
    print ()

    # ask for width & height of an image
    # (must be more than / equal to 1)
    image_width = num_check("Image width? ", 1)
    print()
    image_height = num_check("Image height? ", 1)