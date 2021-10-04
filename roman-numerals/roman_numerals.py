number_roman = {
    1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C',  500: 'D', 1000: 'M', 10000: '-'
            }


def roman(number):
    if number == 0:
        return ''
    denominators = [1000, 100, 10, 1]
    for denominator in denominators:
        if number >= denominator:
            biggie, smalls = number // denominator, number % denominator
            if biggie <= 3:
                return biggie * number_roman[denominator] + roman(smalls)
            elif biggie == 4:
                return number_roman[denominator] + number_roman[5 * denominator] + roman(smalls)
            elif biggie == 5:
                return number_roman[5 * denominator] + roman(smalls)
            elif biggie <= 8:
                return number_roman[5 * denominator] + (biggie - 5) * number_roman[denominator] + roman(smalls)
            else:
                return number_roman[denominator] + number_roman[10 * denominator] + roman(smalls)
