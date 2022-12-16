from math import floor


def main():
    print('-----------------------------------')
    print(' Welcome to the Decimal Converter!')
    print('-----------------------------------')

    while True:
        input_value = input('Type in a decimal number: ')
        if not input_test(input_value):
            print('This is not a valid entry! Try again: ')
            print()
            continue
        # print(convert_decimals(int(input_value), 3))
        print()
        proper_display('0')
        proper_display('01')
        proper_display('012')
        proper_display('0123')
        proper_display('01234')
        proper_display('012345')
        proper_display('0123456')


def input_test(number):
    """Checks if the parameter is a natural number.

    :param: an element to be checked.
    :return: returns a boolean whether the element is a natural number or not.
    """

    if number.isdigit() and number != '0':
        return True
    else:
        return False


def conversion_test(number, outcome, numeral_system):  # takes only reversed numbers
    total = 0
    for i in range(1, len(outcome) + 1):
        if outcome[int(i) - 1] != '0':
            total += ((numeral_system ** (int(i) - 1)) * int(outcome[int(i) - 1]))
    if total == number:
        return True
    else:
        return False


def convert_decimals(number, numeral_system):
    total = 0
    new_digits = []

    i = 0
    while (numeral_system ** i) <= number:
        i += 1

    number_length = i
    for digit in range(number_length - 1):
        new_digits.append('0')

    digit = str(floor(number / (numeral_system ** (i - 1))))
    new_digits.append(digit)
    total += (numeral_system ** (i - 1)) * int(digit)
    diff = number - total
    new_digits_str = ''.join(new_digits)

    while not conversion_test(number, new_digits_str, numeral_system):
        i = 0
        while (numeral_system ** i) <= diff:
            i += 1
        digit = str(floor(diff / (numeral_system ** (i - 1))))
        total += (numeral_system ** (i - 1)) * int(digit)
        diff = number - total

        new_digits[i - 1] = digit
        new_digits_str = ''.join(new_digits)
    return new_digits_str


def proper_display(number_str):
    new_str = ''
    str_part = ''
    temp = ''

    for digit in number_str:
        str_part += digit
        temp += digit
        if len(str_part) % 3 == 0:
            temp = ''
            str_part += ' '
            new_str += str_part
            str_part = ''
    new_str += temp
    new_str = new_str[::-1].strip()

    return new_str


if __name__ == '__main__':
    main()
