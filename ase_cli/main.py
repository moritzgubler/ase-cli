import argparse
import ase_cli.average_file
import ase_cli.convert_ase_files

def main():

    parser = argparse.ArgumentParser(description='ASE Command Line Interface')
    subparser = parser.add_subparsers(help="Command that database will execute", dest='command', required=True)

    ase_cli.average_file.parse(subparser)
    ase_cli.convert_ase_files.parse(subparser)

    main_args = parser.parse_args()
    main_args.func(main_args)

if __name__ == '__main__':
    main()