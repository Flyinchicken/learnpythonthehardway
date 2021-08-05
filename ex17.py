# argv to take command line inputs and store them as diff vars
from sys import argv
script, from_file, to_file = argv
open(to_file, 'w').write(open(from_file).read())
