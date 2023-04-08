
import unittest

def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 4:
        return "IV"
    elif decimal == 5:
        return 'V'
    elif decimal == 6:
        return "VI"
    elif decimal >= 6 and decimal <= 8:
        return "V" + "I" * (decimal - 5)
    elif decimal == 9:
        return "IX"
    else:
        return "X"



if __name__ == '__main__':
    unittest.main()