import argparse
from typing import TextIO
from commands import *
from constants import *


"""
Program to automate the process of adding and removing software packages. This program generates an output text
in response to an input file containing a set of instructions

"""
__author__ = "Jorge Arévalo"
__version__ = "0.1.0"
__maintainer__ = "Jorge Arévalo"
__email__ = "jorgeas80@gmail.com"
__status__ = "Alpha"


def handle_args():
    """
    Handle input arguments
    """
    parser = argparse.ArgumentParser(
        description="Dependency manager"
    )
    parser.add_argument(
        dest="file_name",
        type=str,
        help="Input file path"
    )

    return parser.parse_args()


def freadline(fp: TextIO, cb: CommandBuilder, fixed_length=FIXED_LINE_LENGTH) -> BaseCommand:
    """
    Function to read a row from the source file and transform it in a command plus an optional list of arguments.
    @param fp: File pointer
    @returns a command instance
    """
    line_read = fp.readline().split()

    if not line_read:
        raise StopIteration

    if len(line_read) > fixed_length:
        line_read = line_read[0:fixed_length]

    # No type validation here, command should include type validation
    command_name = line_read[0]
    command_item = line_read[1]
    command_args = line_read[2:] if len(line_read) > 2 else None

    # Build the command
    cmd = cb(command_name, command_item, command_args)

    return cmd


class CommandFileReader:
    """
        Reader over a file with the expected command syntax. Built as iterator, to avoid problems with big files
    """

    def __init__(self, fp, **kwargs):
        self.fp = fp
        self.cb = kwargs.get('cb') or CommandBuilder()

    def __iter__(self):
        return self

    def _freadline(self):
        return freadline(self.fp, self.cb)

    def __next__(self):
        """
            Here we generate:
                * Echoed input
                * Extra input if needed (example: success or error msg)
        """
        input_line = self._freadline()
        extra_output = ''

        return str(input_line) + extra_output


if __name__ == "__main__":
    args = handle_args()

    fp = open(args.file_name, "r")
    command_file_reader = CommandFileReader(fp)

    for command_result in command_file_reader:
        print(command_result)

    fp.close()

