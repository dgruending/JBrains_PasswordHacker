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


def dictionary_attack():
    pass
