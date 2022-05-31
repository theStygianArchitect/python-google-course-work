#! /usr/local/bin/python3
"""
    Title: lists.py

    Author: theStygianArchitect

    Description: Solutions manual
"""
import operator
from typing import Any


def match_ends(words: list) -> int:
    """Document for describing match_ends solution.

    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    Note: python does not have a ++ operator, but += works.

    Args:
        words(list): The list of strings.

    Returns:
        The count according to the logic above.

    """
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count


def front_x(words: list) -> list:
    """Document for describing front_x solution.

    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    ie. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

    Hint: This can be done by making 2 lists and sorting each of them
            before combining them.

    Args:
        words(list): The given list of strings.

    Returns:
        The list of words sorted according to the logic above.

    """
    x_list = []
    other_list = []
    for word in words:
        if word.startswith('x'):
            x_list.append(word)
        else:
            other_list.append(word)
    return sorted(x_list) + sorted(other_list)


def sort_last(tuples: list) -> list:
    """Document for describing sort_last solution.

    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    ie. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

    Hint: Use a custom key= function to extract the last element form
            each tuple.

    Args:
        tuples(list): The list of non-empty tuples

    Returns:
        The list of tuples sorted according to the logic above.

    """
    return sorted(tuples, key=operator.itemgetter(-1))

def remove_adjacent(nums: list) -> list:
    """Document for describing remove_adjacent solution.

    Given a list of numbers, return a list where all equaling adjacent
    elements have been reduced to a single element.
    ie. [1, 2, 2, 3] returns [1, 2, 3].

    Hint: You may create a new list or modify the passed in list.

    Args:
        nums(list): The given list of numbers.

    Returns:
        A list of numbers according to the logic above.

    """
    result = []
    for num in nums:
        if len(result) == 0 or num != result[-1]:
            result.append(num)
    return result


def linear_merge(list1: list, list2: list) -> list:
    """Document for describing linear_merge solution.

    Given two lists sorted in increasing order, create and return a
    merged list of all the elements in sorted order. You may modify the
    passed in lists.

    Ideally, the solution should work in "linear" time, making a single
    pass of both lists.

    Args:
        list1(list): The first given list.
        list2(list): The second given list.

    Returns:
        A list according to the logic above.

    """
    list1.extend(list2)
    return sorted(list1)


def validate(received: Any, expected: Any):
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
    print('match_ends')
    validate(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    validate(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    validate(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print('-' * 100)
    print('front_x')
    validate(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    validate(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    validate(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple',
                                                                      'mix'])

    print('-' * 100)
    print('sort_last')
    validate(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    validate(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    validate(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

    print('-' * 100)
    print('remove_adjacent')
    validate(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    validate(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    validate(remove_adjacent([]), [])

    print('-' * 100)
    print('linear_merge')
    validate(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    validate(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']), ['aa', 'bb', 'cc', 'xx', 'zz'])
    validate(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']), ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
