from string import digits, ascii_letters
from itertools import product

chars = digits + ascii_letters

for comb in product(chars, repeat=7):
    print(''.join(comb))
