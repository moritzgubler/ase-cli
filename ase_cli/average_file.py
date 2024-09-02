import argparse
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Prints the average and standard deviation of a column in a file.')
    parser.add_argument('filename', type=argparse.FileType('r'), help='The file to average.')

    parser.add_argument("--col", type=int, help="The column to average (first column has index 1), default 1", required = False, default = 1)
    parser.add_argument("--mean", action="store_true", help="Only print the mean", required = False, default = False)
    parser.add_argument("--std", action="store_true", help="Only print the standard deviation", required = False, default = False)
    parser.add_argument("--row_wise", action="store_true", help="Average the rows instead of the columns, default false", required = False, default = False)
    parser.add_argument("--row", type=int, help="The line to average (first row has index 1), default 1", required = False, default = 1)
    parser.add_argument("--comment", type=str, help="The comment character, default #", required = False, default = "#")
    parser.add_argument("--skip", type=int, help="The number of entries to skip, default 0", required = False, default = 0)


    args = parser.parse_args()
    lines = args.filename.readlines()
    args.filename.close()
    if args.row_wise:
        data_line = lines[args.row - 1].strip().split(args.comment)[0].split()
        if len(data_line) == 0:
            raise ValueError("Requested row is empty in line: " + lines[args.row - 1])
        data = np.array([float(x) for x in data_line[args.skip:]])
    else:
        data = []
        for line in lines[args.skip:]:
            l = line.strip().split(args.comment)[0].split()
            if len(l) == 0:
                continue
            if len(l) < args.col:
                raise ValueError("Column index out of bounds in line: " + line)
            data.append(float(l[args.col - 1]))
        data = np.array(data)
    
    if args.mean:
        print(np.mean(data))
    elif args.std:
        print(np.std(data))
    else:
        print(np.mean(data), np.std(data))


