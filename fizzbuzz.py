def fizzbuzz(x):
    if (x % 3 == 0):
        if (x % 5 == 0):
            return('FizzBuzz')
        else:
            return "Fizz"
    elif (x % 5 == 0):
        return "Buzz"

if __name__ == "__main__":
    for x in range(1, 101):
        print(fizzbuzz(x))