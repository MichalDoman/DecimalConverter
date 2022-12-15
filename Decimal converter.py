def main():
    print('-----------------------------------')
    print(' Welcome to the Decimal Converter!')
    print('-----------------------------------')

    while True:
        input_value = input('Type in a decimal number: ')
        if not integer_test(input_value):
            print('This is not a number! Try again: ')
            continue
        print(decimal_to_binary(int(input_value), 2))


def integer_test(number):
    """Checks if the parameter is a digit.

    :param: an element to be checked.
    :return: returns a boolean whether the element is a digit or not.
    """

    if number.isdigit():
        return True
    else:
        return False


def conversion_test(number, outcome, numeral_system):
    total = 0
    for i in range(1, len(outcome) + 1):
        if outcome[int(i) - 1] == '1':
            total += (numeral_system ** (int(i) - 1))  # Works only for binary
    if total == number:
        return True
    else:
        return False


def decimal_to_binary(number, numeral_system):
    i = 0
    total = 0
    binary = []

    while (numeral_system ** i) <= number:
        i += 1

    length = i
    for digit in range(length - 1):
        binary.append('0')
    binary.append('1')
    total += (numeral_system ** (i - 1))
    diff = number - total
    binary_str = ''.join(binary)
    while not conversion_test(number, binary_str, numeral_system):
        if diff == 0:
            return binary_str
        else:
            i = 0
            while (numeral_system ** i) <= diff:
                i += 1
            total += (numeral_system ** (i - 1))
            print(total)
            print(diff)
            binary[i - 1] = '1'
            binary_str = ''.join(binary)
    return binary_str

if __name__ == '__main__':
    main()
