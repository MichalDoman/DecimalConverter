def main():
    print('-----------------------------------')
    print(' Welcome to the Decimal Converter!')
    print('-----------------------------------')

    while True:
        input_value = input('Type in a decimal number: ')
        if not integer_test(input_value):
            print('This is not a number! Try again: ')
            continue
        decimal_to_binary(int(input_value), 2)


def integer_test(number):
    """Checks if the parameter is a digit.

    :param: an element to be checked.
    :return: returns a boolean whether the element is a digit or not.
    """

    if number.isdigit():
        return True
    else:
        return False


def decimal_to_binary(number, numeral_system):
    i = 0
    total = 0
    binary = ''
    while (numeral_system ** i) <= number:
        i += 1
    binary += '1'
    total += (numeral_system ** (i - 1))
    print(total)
    print(binary)


if __name__ == '__main__':
    main()
