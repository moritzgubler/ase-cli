import argparse
from ase.io import read, write
import os

def parse(subparser):
    parser = subparser.add_parser("supercell", help="Creates a supercell of a file.")
    parser.add_argument('filename', type=argparse.FileType('r'), help='The file to create a supercell of.')
    parser.add_argument('repeats', type=int, nargs=3, help='The number of repeats in each direction.')
    parser.add_argument('--output', type=str, help='The output file. Default: input file with _supercell appended.', required=False)
    # Set the function to be called when this command is used
    parser.set_defaults(func=main)

def main(args):
    atoms = read(args.filename, index =':')
    args.filename.close()
    
    for ats in atoms:
        ats.repeat(args.repeats)

    if args.output is None:
        output = os.path.splitext(args.filename.name)[0] + "_supercell" + os.path.splitext(args.filename.name)[1]
    else:
        output = args.output
    write(output, atoms)