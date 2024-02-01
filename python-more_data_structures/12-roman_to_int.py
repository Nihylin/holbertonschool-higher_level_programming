#!/usr/bin/python3
# def roman_to_int(roman_string):
#     if roman_string is None or type(roman_string) is not str:
#         return 0
#     else:
#         roman = {
#             'I': 1,
#             'V': 5,
#             'IX': 9,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
#         i = 0
#         num = 0
#         while i < len(roman_string):
#             if i + 1 < len(roman_string) and roman_string[i:i + 2] in roman:
#                 num += roman[roman_string[i:i + 2]]
#                 i += 2
#             else:
#                 num += roman[roman_string[i]]
#                 i += 1
#         return num

def value(roman_numeral):
    if (roman_numeral == 'I'):
        return 1
    if (roman_numeral == 'V'):
        return 5
    if (roman_numeral == 'X'):
        return 10
    if (roman_numeral == 'L'):
        return 50
    if (roman_numeral == 'C'):
        return 100
    if (roman_numeral == 'D'):
        return 500
    if (roman_numeral == 'M'):
        return 1000
    return -1


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    else:
        result = 0
        idx = 0

        while (idx < len(roman_string)):
            # Getting value of symbol s[i]
            symbol = value(roman_string[idx])
            if (idx + 1 < len(roman_string)):
                # Getting value of symbol s[i + 1]
                next_symbol = value(roman_string[idx + 1])
                # Comparing both values
                if (symbol >= next_symbol):
                    # Value of current symbol is greater
                    # or equal to the next symbol
                    result = result + symbol
                    idx = idx + 1
                else:
                    # Value of current symbol is greater
                    # or equal to the next symbol
                    result = result + next_symbol - symbol
                    idx = idx + 2
            else:
                result = result + symbol
                idx = idx + 1
        return result
