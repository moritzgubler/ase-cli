from ase.io import read, write
import argparse
import numpy as np
import os

def parse(subparser):
    parser = subparser.add_parser("rattle", help="Rattle the atoms in a file.")
    parser.add_argument('filename', type=argparse.FileType('r'), help='The file to rattle.')
    parser.add_argument('std', type=float, help='The standard deviation of the rattle.')
    parser.add_argument('--output', type=str, help='The output file. Default: input file with _rattled appended.', required=False)
    parser.add_argument('--seed', type=int, help='The seed for the random number generator.', required=False)
    parser.add_argument('--cell', action='store_true', help='Rattle the cell and the atoms.', required=False)
    parser.set_defaults(func=main)


def main(args):
    atoms = read(args.filename, index=':')
    args.filename.close()
    
    if args.seed is not None:
        np.random.seed(args.seed)
    
    for ats in atoms:
        if args.cell:
            ats.set_cell(ats.get_cell() + np.random.normal(0, args.std, (3,3)), scale_atoms=True)
        ats.rattle(args.std)
    
    if args.output is None:
        output = os.path.splitext(args.filename.name)[0] + "_rattled" + os.path.splitext(args.filename.name)[1]
    else:
        output = args.output
    write(output, atoms)