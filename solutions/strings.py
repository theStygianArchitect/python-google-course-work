#! /usr/local/bin/python3
"""
    Title: strings.py

    Author: theStygianArchitect

    Description: Solution to app/strings.py
"""


def donuts(count: int) -> str:
    """Document for describing donuts solution.

    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    So donuts(5) returns 'Number of donuts: 5' and donuts(23) returns
    'Number of donuts: many'

    Args:
        count(int): The number of donuts

    Returns:
        A string with the number of donuts according to the logic above

    """
    # +++your code here+++
    if count < 10:
        return f'Number of donuts: {count}'
    else:
        return 'Number of donuts: many'


def both_ends(example: str) -> str:
    """Documentation for describing both_ends solution.

    Given a string example, return a string made of the first 2 and the
    last 2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    Args:
        example(str): The sample string to be manipulated.

    Returns:
        A string modified to match the appropriate logic above

    """
    # +++your code here+++
    if len(example) < 2:
        return ''
    first2 = example[0:2]
    last2 = example[-2:]
    return f"{first2}{last2}"


def fix_start(rand_string: str) -> str:
    """Documentation for describing fix_start solution.

    Given a string rand_string, return a string
    where all occurrences of its first character have
    been changed to '*', except do not change
    the first character itself.
    e.g. 'babble' yields 'ba**le'
    Assume that the string is length 1 or more.
    Hint: rand_string.replace(stra, strb) returns a version
    of string rand_string where all instances of stra have
    been replaced by strb.

    Args:
        rand_string(str): The sample string to be manipulated.

    Returns:
        A string modified to match the appropriate logic above

    """
    # +++your code here+++
    front = rand_string[0]
    back = rand_string[1:]
    fixed_back = back.replace(front, '*')
    return f"{front}{fixed_back}"


def mix_up(string_a: str, string_b: str) -> str:
    """Documentation for describing mix_up solution.

    Given strings string_a and string_b, return a single string with
    string_a and string_b separated by a space '<stra> <string_b>',
    except swap the first 2 chars of each string.
    e.g.
      'mix', pod' -> 'pox mid'
      'dog', 'dinner' -> 'dig donner'
    Assume string_a and string_b are length 2 or more.

    Args:
        string_a(str): First random string.
        string_b(str): Second random string.

    Returns:
        A string modified to match the appropriate logic above

    """
    # +++your code here+++
    a_swapped = string_b[:2] + string_a[2:]
    b_swapped = string_a[:2] + string_b[2:]
    return f"{a_swapped} {b_swapped}"


def verbing(rand_str: str) -> str:
    """Documentation for describing verbing solution.

    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged.
    Return the resulting string.

    Args:
        rand_str(str): The string to be manipulated

    Returns:
        A string modified to match the appropriate logic above

    """
    # +++your code here+++
    if len(rand_str) >= 3:
        if rand_str[-3:] != 'ing':
            rand_str = rand_str + 'ing'
        else:
            rand_str = rand_str + 'ly'
    return rand_str


def not_bad(rand_str: str) -> str:
    """Documentation for describing not_bad solution.

    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'.
    Return the resulting string.
    So 'This dinner is not that bad!' yields:
    This dinner is good!

    Args:
        rand_str(str): The string to be manipulated

    Returns:
        A string modified to match the appropriate logic above

    """
    # +++your code here+++
    index_n = rand_str.find('not')
    index_b = rand_str.find('bad')
    if index_n != -1 and index_b != -1 and index_b > index_n:
        rand_str = rand_str[:index_n] + 'good' + rand_str[index_b + 3:]
    return rand_str


def front_back(string_a: str, string_b: str) -> str:
    """Documentation for ddescribing front_back solution.

    Consider dividing a string into two halves.
    If the length is even, the front and back halves are the same length.
    If the length is odd, we'll say that the extra character goes in the front half.
    e.g. 'abcde', the front half is 'abc', the back half 'de'.
    Given 2 strings, a and string_b, return a string of the form
     a-front + string_b-front + a-back + string_b-back

    Args:
        string_a(str): The first string
        string_b(str): The second string

    Returns:
        A string modified to match the appropriate logic above

    """
    # +++your code here+++
    a_middle = len(string_a) // 2
    b_middle = len(string_b) // 2
    if len(string_a) % 2 == 1:  # add 1 if length is odd
        a_middle = a_middle + 1
    if len(string_b) % 2 == 1:
        b_middle = b_middle + 1
    return f"{string_a[:a_middle]}{string_b[:b_middle]}{string_a[a_middle:]}{string_b[b_middle:]}"


def validate(received, expected):
    """Rough testing function to validate above function.

    Args:
        received(str): Results of functions above
        expected(str): A string containing the answer

    Returns:
        A string that shows if everything is ok.

    """
    if received == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(f"{prefix} received: {received} expected: {expected}")


def main():
    """
        This function is used to execute the module as a standalone
        module.
    """
    print('-' * 100)
    print('donuts')
    validate(donuts(4), 'Number of donuts: 4')
    validate(donuts(9), 'Number of donuts: 9')
    validate(donuts(10), 'Number of donuts: many')
    validate(donuts(99), 'Number of donuts: many')

    print('-' * 100)
    print('both_ends')
    validate(both_ends('spring'), 'spng')
    validate(both_ends('Hello'), 'Helo')
    validate(both_ends('a'), '')
    validate(both_ends('xyz'), 'xyyz')

    print('-' * 100)
    print('fix_start')
    validate(fix_start('babble'), 'ba**le')
    validate(fix_start('aardvark'), 'a*rdv*rk')
    validate(fix_start('google'), 'goo*le')
    validate(fix_start('donut'), 'donut')

    print('-' * 100)
    print('mix_up')
    validate(mix_up('mix', 'pod'), 'pox mid')
    validate(mix_up('dog', 'dinner'), 'dig donner')
    validate(mix_up('gnash', 'sport'), 'spash gnort')
    validate(mix_up('pezzy', 'firm'), 'fizzy perm')

    print('-' * 100)
    print('verbing')
    validate(verbing('hail'), 'hailing')
    validate(verbing('swiming'), 'swimingly')
    validate(verbing('do'), 'do')

    print('-' * 100)
    print('not_bad')
    validate(not_bad('This movie is not so bad'), 'This movie is good')
    validate(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    validate(not_bad('This tea is not hot'), 'This tea is not hot')
    validate(not_bad("It's bad yet not"), "It's bad yet not")

    print('-' * 100)
    print('front_back')
    validate(front_back('abcd', 'xy'), 'abxcdy')
    validate(front_back('abcde', 'xyz'), 'abcxydez')
    validate(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
