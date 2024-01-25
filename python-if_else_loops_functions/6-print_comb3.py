#!/usr/bin/python3
for numz in range (0,10):
  for numy in range(numz + 1, 10):
    if numz != 8:
      print("{}{}".format(numz, numy), end=", ")

    else:
      print("{}{}".format(numz, numy))
