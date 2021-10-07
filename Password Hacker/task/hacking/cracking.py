import itertools
import string
import sys


def brute_force(alphabet=itertools.chain(string.ascii_lowercase, map(str, range(10)))):
    """
    Generator for all possible combinations of the provided alphabet.

    Generate strings of increasing length and all possible combinations out of alphabet.
    Example: ['a', 'b'] -> 'a' 'b' 'aa' 'ab' 'ba' 'bb' 'aaa' 'aab' 'aba' ...
    :param alphabet: String iterable of the alphabet to be used
    :return: String
    """
    # List conversion, because the code will fail, if alphabet is an iterator
    alphabet = list(alphabet)
    for i in range(1, sys.maxsize):
        for combination in itertools.product(alphabet, repeat=i):
            yield "".join(combination)


def dictionary_attack(filename):
    """
    Generator for all provided passwords and their variations with case swaps.

    :param filename: Text file with a password on each new line.
    :return: Possible password
    """
    with open(filename) as password_dictionary:
        for password in password_dictionary:
            password = password.strip()
            yield password

            if password.isdigit():
                continue

            # Generate all possible index combinations
            indices = list(range(len(password)))
            change_indices = []
            for i in range(1, len(indices) + 1):
                change_indices = itertools.chain(change_indices, itertools.combinations(indices, i))

            # for every index combination, change the cases if no digit is present
            for index_tuple in change_indices:
                password_copy = list(password)
                for index in index_tuple:
                    if password_copy[index].isdigit():
                        break
                    else:
                        password_copy[index] = password_copy[index].swapcase()
                yield "".join(password_copy)
