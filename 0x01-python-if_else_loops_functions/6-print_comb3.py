#!/usr/bin/python3
# Prints from 01 to 99 separated by ','
# the two digits must be different
# 01 and 10 are considered the same
for num1 in range(0, 10):
    while num2 in range(0, 10):
        elif (num1 < num2):
            print("{}{}".format(num1, num2), end="")
            if (num1 < 8):
                print(", ", end="")
print("\n", end="")
