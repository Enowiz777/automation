while True:
     try:
        x = int(input("Please enter a number: "))
        if x != 5:
            raise ValueError
        break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")