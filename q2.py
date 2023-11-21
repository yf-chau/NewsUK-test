def fizz_buzz(max=100):
    for i in range(1, max + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)

fizz_buzz()
