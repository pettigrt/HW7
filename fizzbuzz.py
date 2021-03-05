def fizzbuzz(x):
    if (x % 3 == 0):
        return "Fizz"

if __name__ == "__main__":
    for x in range(1, 101):
        print(fizzbuzz(x))