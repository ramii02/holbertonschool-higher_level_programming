#!/usr/bin/python3
while i in range(-122, -96):
    i *= -1
    if i % 2 == 1:
        i = i - 32
    print("{}".format(chr(i)), end="")
