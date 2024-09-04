from ase.io import read, write
import argparse
from os.path import basename

def parse(subparser):

    parser = subparser.add_parser("convert", help='Converts a file from one ASE format to another.')
    parser.add_argument('input', type=argparse.FileType('r'), nargs="+", help='The file(s) to convert.')
    parser.add_argument('--output', type=str, help='The output file. Only makes sense if only one input file is provided', required=False)
    parser.add_argument("--input_format", type=str, help="The input format. Default: ase will choose format based on ending", required = False, default = "")
    parser.add_argument("--index", type=str, help="The index of the file to convert, default 0", required = False, default = "0")
    parser.add_argument("--format", type=str, help="The output format. Is superseded by the output option. Default: extxyz", required = False, default = "extxyz")
    parser.set_defaults(func=main)

def main(args):
    
    if args.output is not None and len(args.input) > 1:
        raise ValueError("Specifying output file only makes sense if only one input file is provided.")
    
    for i, f in enumerate(args.input):
        if args.output is not None:
            out = args.output
        else:
            out = basename(f.name) + "." + args.format
        if len(args.input) > 0:
            atoms = read(f, index=args.index, format=args.input_format)
        else:
            atoms = read(f, index = args.index)
        f.close()
        write(out, atoms, format=args.format)
