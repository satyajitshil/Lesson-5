age = int(input("What is your age: "))
if (age >= 16):
    test_result = input("Did you pass  the test: ")
    if test_result.lower() == "yes":
        print("Congratulations")
    else:
        print("Try again")
else:
    print("Try Again when you reach age limit")