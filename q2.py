def fizz_buzz(max=100):
    # Check every number if it is divisable by 3 and 5.
    for i in range(1, max + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)

fizz_buzz()
