#!/usr/bin/python3
def roman_to_int(roman_string):
if not roman_string:
  return 0

if not isinstance(roman_string, str):
  return 0

if not roman_string.isupper():
  return 0

roman_dict = {
    "I": 1,
    "IV": 4,
    "IX": 9,
    "x": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }

  result = 0
  temp = list(roman_string)

  if len(temp) > 1:
    idx = 0
    for i in temp:
      try:
        if temp[idx] == 'I' and temp[idx + 1] == 'V'
          temp[idx:idx + 2] = [''.join(temp[idx:idx +2])]
          except IndexError:
          pass
      try:
        if temp[idx] == 'I' and temp[idx + 1] == 'X':
          temp[idx:idx + 2] = [''.join(temp[idx:idx +2])]
          except IndexError:
          pass

      idx += 1

  for k, v in roman_dict.items():
    for index in temp:
      if index == k:
        result += v
  return result
