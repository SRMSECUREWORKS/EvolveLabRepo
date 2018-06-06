def youragein2035():
    # define the function

    print(“How old are you”)
    # Prompt the user to to enter the age

    currentAge = int(input())
    # assign their age to the variable currentAge

    while currentAge >= 100:
        # start a while loop if the person input 100 or higher
        # the program will continue in this loop until the entry of a number that is < 100

        import datetime
        # import python’s date function to determina the current date
        # https://learnandlearn.com/python-programming/python-reference/python-get-current-date
        date = datetime.datetime.today()
        # determine the current date

        print(“If
        you
        are “, currentAge,” in “, date.year,” then
        you
        will
        be “, 2035 - date.year + currentAge,“ in 2035”)
        # date.year is the current year
        # advise the user that of their current age, the current year and how old they will be in 2035

        print(‘Enter
        another
        age: ’)
        # promt the user to enter an age

        currentAge = int(input())
        # because the user had previously entered a number that is 100 or higher,
        # prompt the user to enter a new age and restart the loop.

    # excape the while becasue the user entered a number that is less than 100
    print(“If
    you
    are “, currentAge, ” in “, date.year, ” then
    you
    will
    be “, 2035 - date.year + currentAge,“ in 2035”)

    youragein2035()
    # execute the function