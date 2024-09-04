import argparse
import ase_cli.average_file
import ase_cli.convert_ase_files
import ase_cli.rattle
import ase_cli.supercell

def main():

    parser = argparse.ArgumentParser(description='ASE Command Line Interface')
    subparser = parser.add_subparsers(help="Command that database will execute", dest='command', required=True)

    ase_cli.average_file.parse(subparser)
    ase_cli.convert_ase_files.parse(subparser)
    ase_cli.supercell.parse(subparser)
    ase_cli.rattle.parse(subparser)

    main_args = parser.parse_args()
    main_args.func(main_args)

if __name__ == '__main__':
    main()