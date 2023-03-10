from math import floor


def main():
    print('-----------------------------------')
    print(' Welcome to the Decimal Converter!')
    print('-----------------------------------')

    while True:
        input_value = input('*** Type in a decimal (and natural) number to be converted: ')
        numeral_system = input(
            '''Choose a natural number (greater than 1) as the base of the numeral system,\nto which you want to convert (e.g. \'2\' for binary): ''')
        if not input_test(input_value) or not input_test(numeral_system) or numeral_system == '1':
            print('This is not a valid entry! Try again: ')
            print()
            continue
        print()

        if numeral_system == '10':
            print(f'It is what you have just typed in: "{input_value}". Should\'t be a surprise though...')
            print()
        else:
            converted_num_lst = convert_decimals(int(input_value), int(numeral_system))
            print(f'"{proper_display(converted_num_lst, int(numeral_system))}"')
            print()


def input_test(number):
    """Checks if the parameter is a natural number.

    :param number: an element to be checked.
    :return: returns a boolean whether the element is a natural number or not (excluding 0).
    """

    if number.isdigit() and number != '0':
        return True
    else:
        return False


def conversion_test(number, outcome, numeral_system):
    """Checks if a given outcome (a number in different numeral system) is correct,
    by recalculating it back to decimal and comparing it to the searched number.

    :param number: An input number (in decimal system).
    :param outcome: A number in a given numeral system to which "number" is compared. Has to be reversed.
    :param numeral_system: A numeral system of the "outcome".
    :return: Returns True or False depending on whether an "outcome" with a base of "numeral_system" equals to "number".
    """
    total = 0
    for i in range(1, len(outcome) + 1):
        if outcome[int(i) - 1] != '0':
            total += ((numeral_system ** (int(i) - 1)) * int(outcome[int(i) - 1]))
    if total == number:
        return True
    else:
        return False


def convert_decimals(number, numeral_system):
    """Converts a number from decimal to a giver numeral system.

    :param number: A number to be converted.
    :param numeral_system: A number system to which the number is to be converted.
    :return: A list of numbers in reversed order, that are ones, tens, hundreds etc. of the converted number.
    """
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
    while not conversion_test(number, new_digits, numeral_system):
        i = 0
        while (numeral_system ** i) <= diff:
            i += 1
        digit = str(floor(diff / (numeral_system ** (i - 1))))
        total += (numeral_system ** (i - 1)) * int(digit)
        diff = number - total
        new_digits[i - 1] = digit

    return new_digits


def proper_display(new_digits, numeral_system):
    """Displays a number in any numeral system in a proper form.

    :param new_digits: A list of reversed digits of a converted number.
    :param numeral_system: A numeral base of a converted number.
    :return: A converted number in a proper form, depending on the numeral base.
    """
    new_str = ''

    if numeral_system > 9:
        for digit in new_digits[::-1]:
            if len(digit) == len(str(numeral_system)):
                new_str += digit
            else:
                new_str += ('0' * (len(str(numeral_system)) - len(digit))) + str(digit)
            new_str += ' ; '
        new_str = new_str.strip(' ; ')

    else:
        str_part = ''
        temp = ''
        for digit in new_digits:
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
