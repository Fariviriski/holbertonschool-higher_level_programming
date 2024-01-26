#!/usr/bin/python3
def fizzbuzz():
    for f in range(101):
        if f % 3 == 0 and f % 5 == 0:
            print("FizzBuzz", end=" ")

        elif f % 3 == 0:
            print("Fizz", end=" ")

        elif f % 5:
            print("Buzz", end=" ")

    else:
        print(f, end=" ")
